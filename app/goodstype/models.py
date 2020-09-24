# -*- encoding: utf-8 -*-


from django.db import models

# Create your models here.

class GoodsType(models.Model):
    # id = models.BigAutoField('id', primary_key=True)
    goods_type = models.CharField('goods_type', max_length=50, unique=True, default=None, help_text='goods type name')
    temp_min = models.IntegerField('temp_min', default=0, help_text='minimum temperature threshold in celcius')
    temp_max = models.IntegerField('temp_max', default=0, help_text='maximum temperature threshold in celcius')

    class Meta:
        ordering = ['goods_type']

    def __str__(self):
        return self.goods_type