from rest_framework import serializers
from projectx.models import Menus, Employee

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = ('priority','name','caption','type','parent_code','module')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('center_code','emp_id','id','name','middle_name','surname','short_code','father_name','mother_name','dob','qualification','year_of_passing','sex','marital_status','department','designation','client_name','client_name1','project_name','passport_no','passport_doi','passport_doe','blood_group','doj')