from django.db import models
from django.contrib.auth.models import AbstractUser

class Solution(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
    original_date = models.DateTimeField(auto_now=True)
    upload_date = models.DateTimeField(auto_now=True)
    
class myUser(AbstractUser):
    username = models.CharField(max_length=64,verbose_name = '사용자명', unique=True)
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')
    
    def __str__(self):
        return self.username  

    class Meta:
        db_table = 'test_user'
class Problem (models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    userid = models.IntegerField()
