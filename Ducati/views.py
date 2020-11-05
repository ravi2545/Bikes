from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django import views
from .models import DucatiBike

from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class ListSerializer_ducati(ModelSerializer):
    class Meta:
        model = DucatiBike
        fields = ["modelName", "year", "price"]


class Ducati_post_get(views.View):
    def get(self, request):
        list_data = []
        Ducati_data = DucatiBike.objects.all()
        for each in Ducati_data:
            list_data.append([each.modelName, each.year, each.price])
        return JsonResponse({"Data": list_data})

    def post(self, request):
        return JsonResponse("This is my Post Method")


class Ducati_save(GenericAPIView):
    serializer_class = ListSerializer_ducati
    queryset = DucatiBike.objects.all()

    def get(self, request):
        Ducati_data = DucatiBike.objects.all()
        serial_data = ListSerializer_ducati(Ducati_data, many=True)
        return Response(serial_data.data)

    def post(selfself, request):
        serial_data = ListSerializer_ducati(data=request.data)
        if serial_data.is_valid():
            serial_data.save()
        return Response(serial_data.data)
