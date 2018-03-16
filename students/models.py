from django.db import models

# Create your models here.


# 定义student模型
from grades.models import Grade


class Student(models.Model):
    name = models.CharField(max_length=32,verbose_name='姓名')
    gender = models.BooleanField(verbose_name='性别')
    age = models.PositiveIntegerField(verbose_name='年龄')
    info = models.CharField(max_length=200,verbose_name='简介')
    is_deleted = models.BooleanField(default=False)
    # 关联外键
    grade = models.ForeignKey(Grade)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '学生'