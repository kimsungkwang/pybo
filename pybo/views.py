from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm , AnswerForm
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    """
    pybo 목록 출력
    """
    # <SELECT문 실행>
    # order_by() 정렬
    # get() 하나만
    # filter() 특정조건만
    
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지
    
    # 조회
    question_list = Question.objects.order_by('-create_date') # SELECT
    
    # 페이징처리
    total_count = Question.objects.count()
    paginator = Paginator(question_list, 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list':page_obj,
               'total_count' : total_count}
    

    return render (request, 'pybo/question_list.html', context)



# Create your views here.

def detail(request, question_id):
    """
    pybo 목록 출력
    """
    # <SELECT문 실행>
    # order_by() 정렬
    # get() 하나만
    # filter() 특정조건만
    question = get_object_or_404(Question, pk=question_id) # SELECT
    context = {'question' : question}
    return render (request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    
    question = get_object_or_404(Question, pk=question_id)
    # content = request.POST['content'] 
    # content key가 없으면 예외 발생
    # content = request.POST.get['content']
    # content key가 없으면 - none리턴
    content=request.POST.get('content')
    question.answer_set.create(create_date=timezone.now())
    
    # Answer 생성
    # 방법 1
    # answer = Answer(question = question,
    #                 content = content, 
    #                 create_date = timezone.now())
    # answer.save()
    
    # 방법 2 ForeignKey 관계인경우
    
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    
    context ={'form': form}
    return render(request, 'pybo/question_form.html', context)

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method =="POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
        context = {'question': question, 'form' : form}
        return render(request, 'pybo/question_detail.html', context)

