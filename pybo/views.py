from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from django.utils import timezone
from django.core.paginator import Paginator

from .forms import QuestionForm, AnswerForm

def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    # 조회
    question_list = Question.objects.order_by('-create_date')
    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}

    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # question  = Question.objects.get(id = question_id)
    question  = get_object_or_404(Question, pk=question_id)
    context = { 'question': question}
    return render(request, 'pybo/quesiton_detail.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question  = get_object_or_404(Question, pk=question_id)
    
    # content = request.POST['content'] # 'content' 키가 없으면 - 예외가 발생.
    content = request.POST.get('content')  # 'content' 키가 없으면 - None리턴

    # Answer 생성, 저장
    # 방법1]
    # answer = Answer(question = question, 
    #               content = content,
    #               create_date = timezone.now())
    # answer.save()

    # 방법2] ForeignKey 관계인경우
    # question.answer_set.create(content = content,
    #               create_date = timezone.now())

    # return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/quesiton_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)




# def login(request, template_name):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
            
#             return redirect(LOGIN_REDIRECT_URL)
#     else:
#         form = LoginForm()

#     context = {'form': form}
#     return render(request, template_name, context)




