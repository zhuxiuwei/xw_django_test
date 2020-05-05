# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class NoMigrateTable(models.Model):
    """测试不手工执行Migrate ok不ok"""
    class Meta:
        db_table = u'nomigratetable'  # 不使用默认table名: <app_name>_<modle_name>
    hello_text = models.CharField(max_length=200)