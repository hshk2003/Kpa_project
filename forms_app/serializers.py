# forms_app/serializers.py

from rest_framework import serializers
from .models import BogieChecksheetForm, WheelSpecificationForm

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheetForm
        fields = '__all__'

class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecificationForm
        fields = '__all__'
