from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice

def index(request):
    son_sual_listi = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": son_sual_listi}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Choice seçilməyibsə, detail səhifəsinə səhv mesajı ilə geri dön
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Siz seçim etməmisiniz.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Nəticələr səhifəsinə yönləndir
        return redirect('polls:results', question_id=question.id)
