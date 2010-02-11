# -*- coding: utf8 -*-
# SDAPS - Scripts for data acquisition with paper based surveys
# Copyright (C) 2008, Christoph Simon <christoph.simon@gmx.eu>
# Copyright (C) 2008, Benjamin Berg <benjamin@sipsolutions.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ugettext import ugettext, ungettext
_ = ugettext

import script
import model

@script.register
@script.logfile
@script.doc(_(u'''

	The cover is a title page for the pile of questionnaires.

	creates cover.odf
	'''))
def cover (survey_dir) :
	import template

	survey = model.survey.Survey.load(survey_dir)

	story = template.story_title(survey)
	subject = []
	for key, value in survey.info.iteritems():
		subject.append(u'%(key)s: %(value)s' % {'key': key, 'value': value})
	subject = u'\n'.join(subject)

	doc = template.DocTemplate(
		survey.path('cover.pdf'),
		_(u'sdaps questionnaire'),
		{
			'title' : survey.title,
			'subject' : subject
		}
	)
	doc.build(story)
