# Generated by Django 4.0.2 on 2022-05-05 20:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0020_alter_ovchivmanagement_substitution_firstline_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 23, 43, 37, 142994)),
        ),
    ]
