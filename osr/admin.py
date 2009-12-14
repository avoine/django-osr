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

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _ 
from osr import models

class SourceAdmin(admin.ModelAdmin):
    list_display = ('url', 'name')
    prepopulated_fields = {"slug": ("name",)}

class RecordingAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'duration', 'onair', 'finish')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(models.Source, SourceAdmin)
admin.site.register(models.Recording, RecordingAdmin)
