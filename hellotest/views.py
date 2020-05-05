# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View

from hellotest.models import NoMigrateTable


def add(request):
    return render(request, 'hello/add.html', {})


class HelloView(View):
    def post(self, request):
        hello_text = request.POST['hello_text']
        print('add text: %s' % hello_text)
        r = NoMigrateTable(hello_text=hello_text)
        r.save()

        #返回列表页
        hello_text_list = NoMigrateTable.objects.all()
        context = {
            'hello_text_list': hello_text_list,
        }
        return render(request, 'hello/index.html', context)

    def get(self, request):
        """hello text列表"""
        hello_text_list = NoMigrateTable.objects.all()
        print hello_text_list
        context = {
            'hello_text_list': hello_text_list,
        }
        return render(request, 'hello/index.html', context)
