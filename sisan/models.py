from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sisan(models.Model):
    user = models.ForeignKey(User, verbose_name="ユーザー",on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=100, verbose_name='資産名')
    sisan_id = models.CharField(max_length=100, verbose_name='資産管理番号')
    name = models.CharField(max_length = 100, verbose_name='型式番号')
    buy_date = models.DateField(verbose_name='取得年月日')
    remove_date = models.DateField(verbose_name='除却年月日', null=True, blank=True)
    price = models.IntegerField(verbose_name='取得価格')
    place = models.CharField(max_length=100, verbose_name='保管場所')    
