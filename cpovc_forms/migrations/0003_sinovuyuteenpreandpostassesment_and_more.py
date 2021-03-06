# Generated by Django 4.0.2 on 2022-04-30 07:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cpovc_registry', '0001_initial'),
        ('cpovc_ovc', '0001_initial'),
        ('cpovc_forms', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SinovuyuTeenPreAndPostAssesment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assment_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 30, 10, 41, 11, 363876)),
        ),
        migrations.CreateModel(
            name='OVCPrevSinovyoTeenEvaluation',
            fields=[
                ('evaluation_id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('ASSESSMENT_TYPE', models.CharField(max_length=10)),
                ('assessment_date', models.DateField(default=django.utils.timezone.now)),
                ('bd_age', models.CharField(max_length=10)),
                ('bd_sex', models.CharField(max_length=10)),
                ('bd_read', models.CharField(max_length=10)),
                ('bd_education_level', models.CharField(max_length=10)),
                ('bd_class', models.CharField(max_length=10)),
                ('bd_bd_boarding_status', models.CharField(max_length=10)),
                ('bd_biological_children', models.CharField(max_length=10)),
                ('bd_live_bilogical_mother', models.CharField(max_length=10)),
                ('bd_live_biological_father', models.CharField(max_length=10)),
                ('bd_disability', models.CharField(max_length=10)),
                ('bd_money_essentials', models.CharField(max_length=10)),
                ('bd_violence', models.CharField(max_length=10)),
                ('bd_adult_unwell', models.CharField(max_length=10)),
                ('bd_child_unwell', models.CharField(max_length=10)),
                ('bd_miss_school', models.CharField(max_length=10)),
                ('bd_hiv_status', models.CharField(max_length=10)),
                ('bd_hiv_prevention', models.CharField(max_length=10)),
                ('bd_two_meals', models.CharField(max_length=10)),
                ('bd_missing_meal', models.CharField(max_length=10)),
                ('rc_discuss_child_needs', models.CharField(max_length=10)),
                ('rc_discipline', models.CharField(max_length=10)),
                ('rc_tells_bothering', models.CharField(max_length=10)),
                ('rc_involve_decisions', models.CharField(max_length=10)),
                ('cb_child_obedient', models.CharField(max_length=10)),
                ('cb_figths_children', models.CharField(max_length=10)),
                ('dc_often_discipline', models.CharField(max_length=10)),
                ('dc_physical_discipline', models.CharField(max_length=10)),
                ('dc_upset_child', models.CharField(max_length=10)),
                ('sp_physical_punish', models.CharField(max_length=10)),
                ('fs_unhappy', models.CharField(max_length=10)),
                ('fs_too_tired', models.CharField(max_length=10)),
                ('fs_hopeful', models.CharField(max_length=10)),
                ('fmp_pre_grouping_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestamp_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('sync_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('person', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'db_table': 'ovc_prev_sinovuyo_teen_evaluation',
            },
        ),
        migrations.CreateModel(
            name='OVCPreventiveEvents',
            fields=[
                ('event', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('event_type_id', models.CharField(max_length=10)),
                ('event_counter', models.IntegerField(default=0)),
                ('event_score', models.IntegerField(default=0, null=True)),
                ('date_of_event', models.DateField(default=django.utils.timezone.now)),
                ('date_of_previous_event', models.DateTimeField(null=True)),
                ('created_by', models.IntegerField(default=404, null=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('sync_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('app_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('house_hold', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpovc_ovc.ovchousehold')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'db_table': 'ovc_preventive_events',
            },
        ),
        migrations.CreateModel(
            name='NewGraduationMonitoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_id', models.IntegerField(max_length=3)),
                ('bench_mark_1', models.IntegerField(default=0)),
                ('bench_mark_2', models.IntegerField(default=0)),
                ('bench_mark_3', models.IntegerField(default=0)),
                ('bench_mark_4', models.IntegerField(default=0)),
                ('bench_mark_5', models.IntegerField(default=0)),
                ('bench_mark_6', models.IntegerField(default=0)),
                ('bench_mark_7', models.IntegerField(default=0)),
                ('bench_mark_8', models.IntegerField(default=0)),
                ('bench_mark_9', models.IntegerField(default=0)),
                ('date_of_event', models.DateField(default=django.utils.timezone.now)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestamp_updated', models.DateTimeField(auto_now=True)),
                ('care_giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_forms.ovccareevents')),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_ovc.ovchousehold')),
            ],
            options={
                'db_table': 'new_graduation_monitoring',
            },
        ),
    ]
