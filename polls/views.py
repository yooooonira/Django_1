from django.shortcuts import render
from django.http import HttpResponse
#http요청받을걸 뿌리고 싶다

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# Create your views here. 



#여긴 py파일이니까 html을 적는건 좋지 않아(따로 파일을 써서 연결을 해야지) 그런데 돌아가긴 하거든?
#그런데 먼저 연습용으로 써보려고 해 // 인터넷에 반환되는 걸 확인하기 위해서!
def index(request):
    html = """
    <html>
    <head>
        <title>투표 사이트</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #c6c6c6;
                padding: 2em;
            }
           
            h1 {color: #ffffff;}
            .box  {
            background: #b951a6;
            padding: 1.5em;
            border-radius: 28px;
            box-shadow: 0 0 10px rgb(0 0 0);
            max-width: 600px;
            margin: auto;
        }
        </style>
    </head>

    <body>
        <div class="box">
            <h1>안녕하세요!</h1>
            <p>여기는 <strong>설문조사(polls)</strong>사이트의 메인 페이지입니다.</p>
            <p>관리자는 설문을 추가하고, 사용자는 투표할 수 있습니다. </p>
        </div>
    </body>

    </html>
    """
    return HttpResponse(html)

