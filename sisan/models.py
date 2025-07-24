from django.db import models
# Create your models here.

class Sisan(models.Model):
    user = models.ForeignKey(to='accounts.User', verbose_name="管理者",on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=100, verbose_name='資産名')
    sisan_id = models.CharField(max_length=100, verbose_name='資産管理番号')
    name = models.CharField(max_length = 100, verbose_name='型式番号')
    buy_date = models.DateField(verbose_name='取得年月日')
    remove_date = models.DateField(verbose_name='除却年月日', null=True, blank=True)
    price = models.IntegerField(verbose_name='取得価格')
    place = models.CharField(max_length=100, verbose_name='保管場所')


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='学科名')

    def __str__(self):
        return self.name
