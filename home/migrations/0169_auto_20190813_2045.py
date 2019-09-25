# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-13 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0168_auto_20190813_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenteligibility',
            name='us_national_or_permanent_resident',
            field=models.BooleanField(help_text='Outreachy is open to applicants around the world. This question is only to determine which tax form you will need to fill out.', verbose_name='Are you a citizen, national, or permanent resident of the United States of America?'),
        ),
        migrations.AlterField(
            model_name='timecommitmentsummary',
            name='enrolled_as_student',
            field=models.BooleanField(help_text='Will you be enrolled in a university or college? Please state yes even if only a few days overlap with the Outreachy internship period.', verbose_name='Are you (or will you be) a university or college student?'),
        ),
    ]