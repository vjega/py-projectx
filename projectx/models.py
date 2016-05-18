from __future__ import unicode_literals

from django.db import models

# Create your models here.

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Menus(models.Model):
	TREE_TYPES = (
		('folder','folder'),
		('card','card'),
		('list','list'),
		('report','report'),
    )
	code = models.AutoField(primary_key=True)
	priority = models.IntegerField()
	name = models.CharField(max_length=200, unique=True)
	caption = models.CharField(max_length=200)
	type = models.CharField(max_length=6, choices=TREE_TYPES)
	parent_code =models.IntegerField()
	module = models.CharField(max_length=100)
	access_level =models.IntegerField()
	active = models.IntegerField()

	class Meta:
		managed = True
		db_table = 'sys_menu'

class Employee(models.Model):
    slno = models.AutoField(primary_key=True)
    center_code = models.CharField(max_length=45)
    emp_id = models.CharField(unique=True, max_length=20)
    id = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=20)
    short_code = models.CharField(max_length=10)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    dob = models.DateField()
    qualification = models.CharField(max_length=40)
    year_of_passing = models.CharField(max_length=40)
    sex = models.CharField(max_length=6)
    marital_status = models.CharField(max_length=7)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    client_name = models.CharField(max_length=70)
    client_name1 = models.CharField(max_length=50)
    project_name = models.CharField(max_length=70)
    passport_no = models.CharField(max_length=70)
    passport_doi = models.DateField()
    passport_doe = models.DateField()
    bc_verfication = models.IntegerField()
    bc_remarks = models.TextField()
    blood_group = models.CharField(max_length=70)
    appointment_type = models.CharField(max_length=8)
    doj = models.DateField()
    dol = models.DateField()
    leaving_reason = models.CharField(max_length=50)
    religion = models.CharField(max_length=100)
    emergency_contact_name = models.CharField(max_length=70)
    emergency_contact_phone = models.CharField(max_length=70)
    secondary_contact_name = models.CharField(max_length=70)
    secondary_contact_phone = models.CharField(max_length=70)
    primary_contact_name = models.CharField(max_length=70)
    primary_contact_phone = models.CharField(max_length=70)
    mobile = models.CharField(max_length=70)
    msys_email = models.CharField(max_length=70)
    msys_email_2 = models.CharField(max_length=70)
    location = models.CharField(max_length=30)
    reporting_to = models.CharField(max_length=70)
    reporting_to_name = models.CharField(max_length=70)
    user_id = models.CharField(max_length=70)
    password = models.CharField(max_length=250)
    forgot_password = models.CharField(max_length=250)
    forgot_pass_ts = models.DateTimeField(blank=True, null=True)
    forgot_password_used = models.IntegerField()
    msys_reference = models.CharField(max_length=70)
    temp_address = models.CharField(max_length=150)
    temp_city = models.CharField(max_length=100)
    temp_state = models.CharField(max_length=45)
    perm_address = models.CharField(max_length=150)
    perm_city = models.CharField(max_length=45)
    perm_state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    tel_no_field = models.CharField(db_column='tel_no_', max_length=15)  # Field renamed because it ended with '_'.
    email_id = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    is_chairman_list = models.IntegerField()
    bank_branch = models.CharField(max_length=100)
    bank_account_no = models.CharField(max_length=30, blank=True, null=True)
    pan_number = models.CharField(max_length=50)
    pf_no_field = models.CharField(db_column='pf_no_', max_length=45)  # Field renamed because it ended with '_'.
    appraisal_month = models.CharField(max_length=240)
    uan_no = models.CharField(max_length=240)
    ctc = models.IntegerField()
    photo = models.CharField(max_length=255)
    skill_set = models.TextField()
    data_log = models.TextField()
    is_manager = models.IntegerField(blank=True, null=True)
    avail_cl = models.IntegerField()
    is_resourse = models.IntegerField()
    blocked = models.IntegerField()
    not_employee = models.IntegerField()
    active_user = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'employee'

class Candidate(models.Model):
    slno = models.AutoField(primary_key=True)
    center_code = models.CharField(max_length=45)
    id = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=20)
    short_code = models.CharField(max_length=10)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    dob = models.DateField()
    qualification = models.CharField(max_length=40)
    year_of_passing = models.CharField(max_length=40)
    sex = models.CharField(max_length=6)
    marital_status = models.CharField(max_length=7)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    client_name = models.CharField(max_length=70)
    client_name1 = models.CharField(max_length=50)
    project_name = models.CharField(max_length=70)
    passport_no = models.CharField(max_length=70)
    passport_doi = models.DateField()
    passport_doe = models.DateField()
    bc_verfication = models.IntegerField()
    bc_remarks = models.TextField()
    blood_group = models.CharField(max_length=70)
    appointment_type = models.CharField(max_length=8)
    doj = models.DateField()
    dol = models.DateField()
    leaving_reason = models.CharField(max_length=50)
    religion = models.CharField(max_length=100)
    emergency_contact_name = models.CharField(max_length=70)
    emergency_contact_phone = models.CharField(max_length=70)
    secondary_contact_name = models.CharField(max_length=70)
    secondary_contact_phone = models.CharField(max_length=70)
    primary_contact_name = models.CharField(max_length=70)
    primary_contact_phone = models.CharField(max_length=70)
    mobile = models.CharField(max_length=70)
    msys_email = models.CharField(max_length=70)
    msys_email_2 = models.CharField(max_length=70)
    location = models.CharField(max_length=30)
    reporting_to = models.CharField(max_length=70)
    reporting_to_name = models.CharField(max_length=70)
    user_id = models.CharField(max_length=70)
    password = models.CharField(max_length=250)
    forgot_password = models.CharField(max_length=250)
    forgot_pass_ts = models.DateTimeField(blank=True, null=True)
    forgot_password_used = models.IntegerField()
    msys_reference = models.CharField(max_length=70)
    temp_address = models.CharField(max_length=150)
    temp_city = models.CharField(max_length=100)
    temp_state = models.CharField(max_length=45)
    perm_address = models.CharField(max_length=150)
    perm_city = models.CharField(max_length=45)
    perm_state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    tel_no_field = models.CharField(db_column='tel_no_', max_length=15)  # Field renamed because it ended with '_'.
    email_id = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    is_chairman_list = models.IntegerField()
    bank_branch = models.CharField(max_length=100)
    bank_account_no = models.CharField(max_length=30, blank=True, null=True)
    pan_number = models.CharField(max_length=50)
    pf_no_field = models.CharField(db_column='pf_no_', max_length=45)  # Field renamed because it ended with '_'.
    appraisal_month = models.CharField(max_length=240)
    uan_no = models.CharField(max_length=240)
    ctc = models.IntegerField()
    photo = models.CharField(max_length=255)
    skill_set = models.TextField()
    data_log = models.TextField()
    is_manager = models.IntegerField(blank=True, null=True)
    avail_cl = models.IntegerField()
    is_resourse = models.IntegerField()
    blocked = models.IntegerField()
    is_employee = models.IntegerField()
    is_selected = models.IntegerField()
    is_rejected = models.IntegerField()
    performance_bonus = models.IntegerField()
    relocation_expenses = models.IntegerField()
    retension_bonus = models.IntegerField()
    joining_bonus = models.IntegerField()
    performance_bonus_amount = models.IntegerField()
    relocation_expenses_amount = models.IntegerField()
    retention_bonus_amount = models.IntegerField()
    joining_bonus_amount = models.IntegerField()
    remarks = models.CharField(max_length=240)
    rejected_by = models.CharField(max_length=240)
    ts = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'candidate'


class Assetmaster(models.Model):
    slno = models.AutoField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=240)
    assets_slno = models.IntegerField()
    date_of_purchase = models.DateField()
    brand = models.CharField(max_length=240)
    model_no = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'assets_master'

class Documents(models.Model):
    slno = models.AutoField(primary_key=True)
    code = models.IntegerField()
    doc_type =  models.CharField(max_length=240)
    name = models.CharField(max_length=240)
    ts = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'documents'

class Courses(models.Model):
    slno = models.AutoField(primary_key=True)
    code = models.IntegerField()
    doc_type =  models.CharField(max_length=240)
    name = models.CharField(max_length=240)
    ts = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'courses'

class Projects(models.Model):
    slno = models.AutoField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=240)
    ts = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'projects'

class Circulars(models.Model):
    slno = models.AutoField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=240)
    description = models.CharField(max_length=240)
    location = models.CharField(max_length=240)
    priority = models.CharField(max_length=240)
    ts = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'circulars'


class Reporting(models.Model):
    slno = models.AutoField(primary_key=True)
    project = models.CharField(max_length=240)
    emp_id = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=240)
    ts = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'projects_reporting'

class Location(models.Model):
    slno = models.AutoField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=20)
    org_name = models.CharField(max_length=20)
    logo = models.CharField(max_length=20)
    logo_header = models.CharField(max_length=20)
    report_logo = models.CharField(max_length=20)
    other_details = models.CharField(max_length=20)
    company_short_name = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    address_2 = models.CharField(max_length=40)
    address_3 = models.CharField(max_length=40)
    pin_code = models.IntegerField() 
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mail_id = models.CharField(max_length=20)
    phone_no = models.IntegerField()
    fax_no = models.IntegerField()
    bank_name = models.CharField(max_length=10)
    bank_acc_no = models.IntegerField()
    bank_address = models.CharField(max_length=20)
    service_tax_no = models.IntegerField()
    tax_type = models.CharField(max_length=10)
    vat_tin_no = models.IntegerField()
    cst_tin_no = models.IntegerField()
    pan_no = models.IntegerField()
    ward_no = models.IntegerField()
    ts = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'sys_location'


class CompanySettings(models.Model):
    slno = models.AutoField(primary_key=True)
    id = models.IntegerField()
    company_name = models.CharField(max_length=10)
    company_address = models.CharField(max_length=20)
    company_time_zone = models.CharField(max_length=10)
    company_url = models.CharField(max_length=10)
    company_theme = models.CharField(max_length=10)
    company_date_format = models.DateField()
    company_name2 = models.CharField(max_length=10)
    company_other_details = models.CharField(max_length=20)
    company_logo = models.CharField(max_length=10)
    company_header_logo = models.CharField(max_length=10)
    company_report_logo = models.CharField(max_length=10)
    company_short_name = models.CharField(max_length=10)
    office_calender = models.CharField(max_length=10)
    cal_year = models.CharField(max_length=10)
    calender_year = models.CharField(max_length=10)
    ts = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'sys_company'


class User(models.Model):
    slno = models.AutoField(primary_key=True)
    location = models.CharField(max_length=10)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=10)
    user_email = models.CharField(max_length=10)
    user_password = models.CharField(max_length=10)
    user_type = models.CharField(max_length=10)
    user_home = models.CharField(max_length=10)
    user_theme = models.CharField(max_length=10)
    user_level = models.CharField(max_length=10)
    user_level_value = models.CharField(max_length=10)
    last_session = models.DateTimeField()
    group_id = models.IntegerField()
    menu_type = models.CharField(max_length=10)
    is_temp_user = models.CharField(max_length=10)
    last_login = models.DateTimeField()
    current_session = models.DateTimeField()
    deleted = models.CharField(max_length=10)
    ts = models.DateTimeField()


    class Meta:
        managed = True
        db_table = 'sys_user'

class Group(models.Model):
    slno = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=10)
    group_id = models.IntegerField()
    status = models.CharField(max_length=10)
    ts = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'sys_group'


