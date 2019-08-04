from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .pagination import *
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
import json
from django.http import HttpResponseNotFound

# Create your views here.
def custom404(request, exception=None):
    return HttpResponseNotFound(json.dumps({"details": "Page Not found."}), content_type="application/json")

class Bank(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		bank_name = request.query_params.get('bank_name')
		city = request.query_params.get('city')
		kwargs_filters = {}
		if bank_name:
			kwargs_filters['bank_name'] = bank_name
		if city:
			kwargs_filters['city'] = city
		bank_obj_list = BankData.objects.filter(**kwargs_filters)
		pagination_class = LimitOffsetPagination()
		result_page = pagination_class.paginate_queryset(bank_obj_list, request)
		bank_serializer = BankSerializers(result_page, many=True)
		return pagination_class.get_paginated_response(bank_serializer.data)

class BankDetails(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request, ifsc):
		try:
			bank_obj = BankData.objects.get(ifsc=ifsc)
			bank_serializer = BankSerializers(bank_obj)
		except:
			return Response(status=404)
		return Response(bank_serializer.data, status=200)