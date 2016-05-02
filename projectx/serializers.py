from rest_framework import serializers
from projectx.models import Menus

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = ('priority','name','caption','type','parent_code','module')