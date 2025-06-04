# view와 연결
from django.urls import path
from . import views #현재 위치의 views.py를 import해 온다. 
# . == 현재 위치 (현재위치에 views.py가 없으면 만들면 됨)

# urlpatterns = [
#     path("", views.index, name="index"),
#      #"" --> 127.0.01:8000 / polls
#      #views.index ---> index함수라는 것 ex) def index
#      #name="index" ---> templet어쩌고인데 아직은 안 배움. 
# ]


app_name = "polls" # 네임스페이스 지정

urlpatterns = [
    # path("", views.index, name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # #detail은 숫자와 연결
    # path("<int:question_id>/results/", views.results, name="results"),
    # #result는 숫자/results/ 와 연결
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    # #전선의 개념으로 짝을 맞춰줘야 한다.


    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    

]
