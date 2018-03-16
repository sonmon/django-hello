from django.db import models

# Create your models here.


# 班级模型类
class Grade(models.Model):
    # 定义字段
    name = models.CharField(max_length=32,verbose_name='班级')
    created_time = models.DateTimeField(verbose_name='创建时间')
    girl_num = models.PositiveIntegerField(verbose_name='女生人数')
    boy_num = models.PositiveIntegerField(verbose_name='男生人数')
    description = models.CharField(max_length=256,verbose_name='描述')
    # 布尔值,判断是否删除
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '班级'




