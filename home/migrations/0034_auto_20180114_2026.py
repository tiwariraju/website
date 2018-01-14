# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-14 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20180114_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorapproval',
            name='mentor_foss_contributions',
            field=models.CharField(default='No contributions to either the team or the FOSS community', help_text='What contributions have you made to this team and the FOSS community who is funding this internship? If none, what contributions have you made to other FOSS communities?', max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentorapproval',
            name='mentorship_style',
            field=models.CharField(default="I don't know what my mentorship style is", help_text='What is your mentorship style? Do you prefer short daily standups, longer weekly reports, or informal progress reports? Are you willing to try pair programming when your intern gets stuck? Do you like talking over video chat or answering questions via email? Give the applicants a sense of what it will be like to work with you during the internship.', max_length=800),
            preserve_default=False,
        ),
    ]
