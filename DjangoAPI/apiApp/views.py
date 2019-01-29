from django.shortcuts import render
from rest_framework import viewsets
from apiApp.models import Test
from apiApp.serializers import TestSerializers


class TestViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = Test.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = TestSerializers