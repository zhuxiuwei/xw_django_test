# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from app1.models import Question, Choice


def index(request):
    """问题列表"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    # 或者直接：
    # return render(request, 'polls/index.html', context)
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    """单个问题详情"""
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    """提交投票"""
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST['choice']: 从detail.html的post数据的name里获取data
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
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
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))