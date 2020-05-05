# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls2/index.html'
    # 指定context变量。否则template(index.html)里使用默认的question_list。（因为index.html里使用的是'latest_question_list'，这里才需要指定。）
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # 告诉generic view 使用哪个model
    model = Question
    # 告诉generic view 使用哪个template。否则使用默认template: <app name>/<model name>_detail.html（不存在）。
    template_name = 'polls2/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls2/results.html'


def vote(request, question_id):
    """提交投票"""
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST['choice']: 从detail.html的post数据的name里获取data
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls2/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # 注意，polls: 匹配的是urls.py里的app_name = 'polls'。是namespace。
        return HttpResponseRedirect(reverse('polls2:results2', args=(question.id,)))