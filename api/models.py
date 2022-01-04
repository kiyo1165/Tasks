from django.db import models
from django.core.validators import MinValueValidator
import uuid
from config import settings

class Category(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item

class Task(models.Model):

    STATUS = (
        ('1', '未完了'),
        ('2', '実行中'),
        ('3', '完了'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    criteria = models.CharField(max_length=100)
    status = models.CharField(max_length=40, choices=STATUS, default='1')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #0以上の整数を受け取る
    estimate = models.ImageField(validators=[MinValueValidator(0)])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='responsible')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.task


