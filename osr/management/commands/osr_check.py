#
# Copyright (C) 2009 Patrick Hetu <patrick@koumbit.org>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this library; see the file COPYING.LIB. If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301, USA.
#
from subprocess import Popen
from datetime import datetime, timedelta

from django.core.management.base import NoArgsCommand
from django.conf import settings

from osr.models import Source, Recording

class Command(NoArgsCommand):
    help = 'Check if Recordings must be start in the next 5 minutes'

    def handle_noargs(self, **options):
        try:
            directory = settings.OSR_DIR
        except:
            print 'Destination directory is not set in the settings file.'
            print 'Example: OSR_DIR = /var/www/streams/'
            return

        now = datetime.now()
        recordings = Recording.objects.filter(
                    start__gt = now,
                    start__lt = now + timedelta(minutes=5),
                    onair = False)

        if recordings:
            for recoding in recordings:
                recoding.onair=True
                recoding.save()
                pid = Popen(['streamripper', str(recoding.source.url),
                            '-a', str(recoding.id), '-s', '-A',\
                            '-l', str(recoding.duration * 60), '--quiet',\
                            '-d', settings.OSR_DIR]).pid

        now = datetime.now()
        recordings = Recording.objects.filter(
                    start__lt = now,
                    onair = True)

        if recordings:
            for recoding in recordings:
                recoding.onair=False
                recoding.finish=True
                recoding.save()
