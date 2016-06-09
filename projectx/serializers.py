from rest_framework import serializers
from projectx.models import Menus, Employee, Candidate, Assetmaster, Documents, Projects, Courses, Circulars, Reporting, Location, CompanySettings, User, Group, EmpDocuments

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = ('priority','name','caption','type','parent_code','module')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('center_code','emp_id','id','name','middle_name','surname','short_code','father_name','mother_name','dob','qualification','year_of_passing','sex','marital_status','department','designation','client_name','client_name1','project_name','passport_no','passport_doi','passport_doe','blood_group','doj')

class CandidateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Candidate
		fields = ('slno','center_code','id','name','middle_name','surname','father_name','mother_name','dob','qualification','year_of_passing','sex','designation','is_selected','is_rejected')

class AssetsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Assetmaster
		fields = ('slno','code','name','assets_slno','date_of_purchase','brand','model_no',)

class DocumentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Documents
		fields = ('slno','code','doc_type','name')

class ProjectsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Projects
		fields = ('slno','code','name')

class CoursesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Courses
		fields = ('slno','code','doc_type','name')

class CircularsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Circulars
		fields = ('slno','date','title','description','location','priority',)

class ReportingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reporting
		fields = ('slno','emp_id','project','name')

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ('slno','code','name','org_name','logo','logo_header','report_logo','other_details','company_short_name','address','address_2','address_3','pin_code','city','state','mail_id','phone_no','fax_no','bank_name','bank_acc_no','bank_address','service_tax_no','tax_type','vat_tin_no','cst_tin_no','pan_no','ward_no','ts',)

class CompanySettingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = CompanySettings
		fields = ('slno','id','company_name','company_address','company_time_zone','company_url','company_theme','company_date_format','company_name2','company_other_details','company_logo','company_header_logo','company_report_logo','company_short_name','office_calender','cal_year','calender_year')


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('slno','location','user_id','user_name','user_email','user_password','user_type','user_home','user_theme','user_level','user_level_value','last_session','group_id','menu_type','is_temp_user','last_login','current_session','deleted')


class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('slno','group_name','group_id','status')

class EmpDocumentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = EmpDocuments
		fields = ('slno','code','name','course','emp_id','line_no_field','doc_type','doc_file','upload_date','remarks','hr_remarks','in_hand','return_date','verified','returned')