from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, get_object_or_404
#404에러는 페이지가 없을때 생기는 에러
from django.http import HttpResponse
#http요청받을걸 뿌리고 싶다
from django.http import HttpResponseRedirect
from .models import Question, Choice

from django.urls import reverse_lazy


# def index(request):
	
# 	latest_question_list = Question.objects.order_by("-pub_date")[:5]
# 	context = {"latest_question_list": latest_question_list}
# 	return render(request, "polls/index.html", context)

# def detail(request, question_id):
# 	try:
# 		question = get_object_or_404(Question, pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Htt404("Question does not exit")
# 	return render(request, "polls/detail.html", {"question": question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

# def vote(request, question_id):
#     return HttpResponse(f"You're voting on question {question_id}.") 

# 메인 페이지 (질문 목록)
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

# 질문 상세 페이지
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "question"

# 결과 페이지
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name = "question"

# 투표 처리 로직
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message":"You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


class QuestionCreateView(generic.CreateView):
    model=Question
    fields=["question_text","pub_date"]
    template_name="polls/question_form.html"
    success_url=reverse_lazy("polls:index") #reverse_lazy 메서드

class QuestionUpdateView(generic.UpdateView):
    pass

class QuestionDeleteView(generic.DeleteView):
    pass