# Generated by Django 4.0.2 on 2022-05-01 07:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0009_alter_ovchivmanagement_substitution_firstline_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 1, 10, 5, 10, 491125)),
        ),
        migrations.AlterField(
            model_name='ovcprevsinovyoteenevaluation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_forms.ovcpreventiveevents'),
        ),
    ]
