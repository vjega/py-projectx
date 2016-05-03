# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('slno', models.CharField(max_length=45)),
                ('center_code', models.CharField(max_length=45)),
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=20)),
                ('short_code', models.CharField(max_length=10)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('qualification', models.CharField(max_length=40)),
                ('year_of_passing', models.CharField(max_length=40)),
                ('sex', models.CharField(max_length=6)),
                ('marital_status', models.CharField(max_length=7)),
                ('department', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=70)),
                ('client_name1', models.CharField(max_length=50)),
                ('project_name', models.CharField(max_length=70)),
                ('passport_no', models.CharField(max_length=70)),
                ('passport_doi', models.DateField()),
                ('passport_doe', models.DateField()),
                ('bc_verfication', models.IntegerField()),
                ('bc_remarks', models.TextField()),
                ('blood_group', models.CharField(max_length=70)),
                ('appointment_type', models.CharField(max_length=8)),
                ('doj', models.DateField()),
                ('dol', models.DateField()),
                ('leaving_reason', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=100)),
                ('emergency_contact_name', models.CharField(max_length=70)),
                ('emergency_contact_phone', models.CharField(max_length=70)),
                ('secondary_contact_name', models.CharField(max_length=70)),
                ('secondary_contact_phone', models.CharField(max_length=70)),
                ('primary_contact_name', models.CharField(max_length=70)),
                ('primary_contact_phone', models.CharField(max_length=70)),
                ('mobile', models.CharField(max_length=70)),
                ('msys_email', models.CharField(max_length=70)),
                ('msys_email_2', models.CharField(max_length=70)),
                ('location', models.CharField(max_length=30)),
                ('reporting_to', models.CharField(max_length=70)),
                ('reporting_to_name', models.CharField(max_length=70)),
                ('user_id', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=250)),
                ('forgot_password', models.CharField(max_length=250)),
                ('forgot_pass_ts', models.DateTimeField(blank=True, null=True)),
                ('forgot_password_used', models.IntegerField()),
                ('msys_reference', models.CharField(max_length=70)),
                ('temp_address', models.CharField(max_length=150)),
                ('temp_city', models.CharField(max_length=100)),
                ('temp_state', models.CharField(max_length=45)),
                ('perm_address', models.CharField(max_length=150)),
                ('perm_city', models.CharField(max_length=45)),
                ('perm_state', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
                ('tel_no_field', models.CharField(db_column='tel_no_', max_length=15)),
                ('email_id', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('is_chairman_list', models.IntegerField()),
                ('bank_branch', models.CharField(max_length=100)),
                ('bank_account_no', models.CharField(blank=True, max_length=30, null=True)),
                ('pan_number', models.CharField(max_length=50)),
                ('pf_no_field', models.CharField(db_column='pf_no_', max_length=45)),
                ('appraisal_month', models.CharField(max_length=240)),
                ('uan_no', models.CharField(max_length=240)),
                ('ctc', models.IntegerField()),
                ('photo', models.CharField(max_length=255)),
                ('skill_set', models.TextField()),
                ('data_log', models.TextField()),
                ('is_manager', models.IntegerField(blank=True, null=True)),
                ('avail_cl', models.IntegerField()),
                ('is_resourse', models.IntegerField()),
                ('blocked', models.IntegerField()),
                ('not_employee', models.IntegerField()),
                ('active_user', models.IntegerField()),
                ('ts', models.DateTimeField()),
            ],
            options={
                'db_table': 'employee',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('priority', models.IntegerField()),
                ('name', models.CharField(max_length=200, unique=True)),
                ('caption', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('folder', 'folder'), ('card', 'card'), ('list', 'list'), ('report', 'report')], max_length=6)),
                ('parent_code', models.IntegerField()),
                ('module', models.CharField(max_length=100)),
                ('access_level', models.IntegerField()),
                ('active', models.IntegerField()),
            ],
            options={
                'db_table': 'sys_menu',
                'managed': True,
            },
        ),
    ]
