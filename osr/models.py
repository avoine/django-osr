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

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode

CHOICE_TYPE = (
    ('mp3', 'mp3'),
    ('ogg', 'ogg'),
    ('nsv', 'nsv'),
    ('aac', 'aac'),
)

class Source(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    url = models.CharField(_('url'),
      max_length=200,
      unique=True,
      help_text=u'%s: %s, %s' % (smart_unicode(_('Example')),
        u'http://icy1.abacast.com/radiocanada-premierechaine-64.m3u',
        u'http://www.example.com:8038'))
    description = models.TextField(_('description'), null=True, blank=True)
    type = models.CharField(max_length=3, blank=True, null=True,
                            default='mp3', choices=CHOICE_TYPE)

    class Meta:
        verbose_name = _('source')
        verbose_name_plural = _('sources')
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class Recording(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    source = models.ForeignKey(Source)
    start = models.DateTimeField(_('Start time'), null=True, blank=True)
    duration = models.IntegerField(_('Duration'), default=60,
            help_text=u'The duration is in minutes')
    onair = models.BooleanField(_('On air'), default=False)
    finish = models.BooleanField(_('Finish'), default=False)

    class Meta:
        verbose_name = _('recording')
        verbose_name_plural = _('recordings')
        ordering = ('name',)

    def __unicode__(self):
        return self.name

