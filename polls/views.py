from django.shortcuts import render, get_object_or_404
#404에러는 페이지가 없을때 생기는 에러
from django.http import HttpResponse
#http요청받을걸 뿌리고 싶다
from .models import Question, Choice


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# #여긴 py파일이니까 html을 적는건 좋지 않아(따로 파일을 써서 연결을 해야지) 그런데 돌아가긴 하거든?
# #그런데 먼저 연습용으로 써보려고 해 // 인터넷에 반환되는 걸 확인하기 위해서!
# def index(request):
#     html = """
#     <html>
#     <head>
#         <title>투표 사이트</title>
#         <style>
#             body {
#                 font-family: Arial, sans-serif;
#                 background-color: #c6c6c6;
#                 padding: 2em;
#             }
           
#             h1 {color: #ffffff;}
#             .box  {
#             background: #b951a6;
#             padding: 1.5em;
#             border-radius: 28px;
#             box-shadow: 0 0 10px rgb(0 0 0);
#             max-width: 600px;
#             margin: auto;
#         }
#         </style>
#     </head>

#     <body>
#         <div class="box">
#             <h1>안녕하세요!</h1>
#             <p>여기는 <strong>설문조사(polls)</strong>사이트의 메인 페이지입니다.</p>
#             <p>관리자는 설문을 추가하고, 사용자는 투표할 수 있습니다. </p>
#         </div>
#     </body>

#     </html>
#     """
#     return HttpResponse(html)

# index(최신글 list)
def index(request):
	
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	context = {"latest_question_list": latest_question_list}
	return render(request, "polls/index.html", context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.") 
