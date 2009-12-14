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

from django.db.models import Q
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.translation import ugettext as _
from django.views.generic.list_detail import object_list, object_detail
from django.http import Http404
from django.conf import settings

from osr.models import Recording

def recording_list(request):
    rec = Recording.objects.all()

    return render_to_response('osr/recording_list.html',\
                              {'recordings': rec, 'OSR_URL': settings.OSR_URL})


def recording_detail(request, slug_or_id):
    try:
        slug_or_id = int(slug_or_id)
        rec = Recording.objects.get(id=slug_or_id)
    except ValueError:
        try:
            rec = Recording.objects.get(slug=slug_or_id)
        except Recording.DoesNotExist:
            raise Http404
    except Recording.DoesNotExist:
        raise Http404



    return render_to_response('osr/recording_detail.html',\
                              {'recording': rec, 'OSR_URL': settings.OSR_URL})
