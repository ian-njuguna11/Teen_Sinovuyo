# Generated by Django 4.0.2 on 2022-05-05 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0017_alter_ovchivmanagement_substitution_firstline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 23, 36, 42, 815956)),
        ),
        migrations.AlterField(
            model_name='ovcprevsinovyoteenevaluation',
            name='bd_class',
            field=models.CharField(default='No Schl', max_length=100),
        ),
    ]
