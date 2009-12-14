#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

import os
import unittest
import time
from datetime import datetime, timedelta

from django.test.client import Client

from osr.management.commands import osr_check
from osr.models import Source, Recording

class ATestInterfaceTestCase(unittest.TestCase):
    def testEmptyRecording(self):
        c = Client()
        response = c.get('/')
        self.assertEquals(str(response),\
"""Vary: Accept-Language, Cookie
Content-Type: text/html; charset=utf-8
Content-Language: en

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">
<html>
<head>
<title>List of recording</title>
</head>
<body>

<h1>List of recording</h1>



There is no recorded stream available.



</body>
</html>
""")

    def testNoneExistingRecord(self):
        c = Client()
        response = c.get('/1/')
        self.assertEquals(response.status_code, 404)

class SourceTestCase(unittest.TestCase):

    def testAACreateObjects(self):
        self.radiocan = Source.objects.create(
            name=u"Radio-Canada: La première chaîne",
            slug=u"radio-canada-la-premiere-chaine",
            url=u"http://icy1.abacast.com/radiocanada-premierechaine-64.m3u",
            type=u"mp3",
        )

        self.cat = Recording.objects.create(
                    name="sample", slug="sample", 
                    start=datetime.now() + timedelta(minutes=2),
                    duration=1, source_id=1)

    def testGetById(self):
        c = Client()
        response = c.get('/1/')
        self.assertEquals(response.status_code, 200)

    def testGetBySlug(self):
        c = Client()
        response = c.get('/sample/')
        self.assertEquals(response.status_code, 200)

    def testRecording(self):
        comm = osr_check.Command()
        comm.handle_noargs()
        rec1 = Recording.objects.get(id=1)
        self.assertEquals(rec1.onair, True)
        # be sure that the download is finish
        time.sleep(120)
        comm.handle_noargs()
        rec2 = Recording.objects.get(id=1)
        self.assertEquals(rec2.onair, False)
        self.assertEquals(rec2.finish, True)

        self.assertTrue('1.mp3' in os.listdir('media/audio/'))
        os.unlink('media/audio/1.mp3')
        os.unlink('media/audio/1.cue')
        self.assertEquals(os.listdir('media/audio/'), [])

