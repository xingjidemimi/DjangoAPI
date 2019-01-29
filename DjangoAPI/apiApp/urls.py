from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from apiApp import views
from rest_framework.documentation import include_docs_urls


API_TITLE = 'API Documents'
API_DESCRIPTION = 'API Information'


# 定义路由地址
route = routers.DefaultRouter()

# 注册新的路由地址
route.register(r'test', views.TestViewSet)

# 注册上一级的路由地址并添加
urlpatterns = [
    path('', include(route.urls)),
    # 接口文档路由
    path(r'docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION, authentication_classes=[], permission_classes=[]))
]
