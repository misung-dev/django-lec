from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 뷰 함수를 views.py 파일에 정의하고 index로 매핑
    # 다른 URL 패턴과 뷰 함수를 추가로 등록 가능
]
