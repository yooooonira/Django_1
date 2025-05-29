from django.urls import path
from . import views #현재 위치의 views.py를 import해 온다. 
# . == 현재 위치 (현재위치에 views.py가 없으면 만들면 됨)

urlpatterns = [
    path("", views.index, name="index"),
     #"" --> 127.0.01:8000 / polls
     #views.index ---> index함수라는 것 ex) def index
     #name="index" ---> templet어쩌고인데 아직은 안 배움. 
]