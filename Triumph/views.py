from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django import views
from .models import Triumphbike

from rest_framework.serializers import ModelSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


class ListSerializer_kuna(ModelSerializer):
    class Meta:
        model = Triumphbike
        fields = ["modelname", "year", "price"]


class Triumph_post_get(views.View):
    def get(self, request):
        list_data = []
        Triump_data = Triumphbike.objects.all()
        for each in Triump_data:
            list_data.append([each.modelname, each.year, each.price])
        return JsonResponse({"Triumph data": list_data})

    def post(self, request):
        return JsonResponse("Post method")


class Trimph_save(GenericAPIView):
    serializer_class = ListSerializer_kuna
    queryset = Triumphbike.objects.all()

    def get(self, request):
        Triumph_data = Triumphbike.objects.all()
        serial_data = ListSerializer_kuna(Triumph_data, many=True)
        return Response(serial_data.data)

    def post(self, request):
        serial_data = ListSerializer_kuna(data=request.data)
        if serial_data.is_valid():
            serial_data.save()
        return Response(serial_data.data)
