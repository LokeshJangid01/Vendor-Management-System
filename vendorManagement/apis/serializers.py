from rest_framework import serializers
from .models import Vendor, Purchase



class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    details = VendorDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Purchase
        fields = '__all__'