# Generated by Django 4.0.2 on 2022-05-05 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0011_alter_ovchivmanagement_substitution_firstline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 15, 46, 12, 813826)),
        ),
    ]
