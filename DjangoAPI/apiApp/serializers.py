from rest_framework import serializers
from apiApp.models import Test


class TestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Test  # 指定的模型类
        fields = ('pk', 'name', 'sex', 'age',)  # 需要序列化的属性