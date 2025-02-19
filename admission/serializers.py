from rest_framework import serializers
from .models import Admission

class AdmissionSerializer(serializers.ModelSerializer):
    form_fee = serializers.IntegerField(min_value=0)
    new_admission_fee = serializers.IntegerField(min_value=0)
    old_admission_fee = serializers.IntegerField(min_value=0)
    new_total_fee = serializers.IntegerField(min_value=0)
    old_total_fee = serializers.IntegerField(min_value=0)
    additional_fee = serializers.IntegerField(min_value=0, required=False, allow_null=True)
    monthly_fee = serializers.IntegerField(min_value=0, required=False, allow_null=True)
    
    class Meta:
        model = Admission
        fields = ['id', 'ClassName', 'class_level', 'form_fee', 'new_admission_fee', 'old_admission_fee', 'new_total_fee', 'old_total_fee', 'additional_fee', 'monthly_fee', 'admission_start_date', 'admission_end_date', 'required_documents', 'admission_notes', 'seat_availability', 'admission_created', 'admission_updated']