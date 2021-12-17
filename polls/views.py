from django.shortcuts import render, get_object_or_404   # 지름길 render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Question, Choice
from django.template import loader
from django.urls import reverse


# Create your views here.


# render() 함수는 request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으며, context 사전형 객체를 세번째 선택적(optional) 인수로 받습니다.
# 인수로 지정된 context로 표현된 템플릿의 HttpResponse 객체가 반환됩니다.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


# 이 코드는 polls/index.html 템플릿을 불러온 후, context를 전달합니다.
# context는 템플릿에서 쓰이는 변수명과 Python 객체를 연결하는 사전형 값입니다.
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')   # template 파일 불러오기
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))


# get_object_or_404() 함수는 Django 모델을 첫번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘깁니다.
# 만약 객체가 존재하지 않을 경우, Http404 예외가 발생합니다.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상적으로 처리하였으면,
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
    # return HttpResponse("You're voting on question %s." % question_id)
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

