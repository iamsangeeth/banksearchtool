from rest_framework import serializers
from .models import *

class BankSerializers(serializers.ModelSerializer):
	class Meta:
		model = BankData
		fields = ('__all__')