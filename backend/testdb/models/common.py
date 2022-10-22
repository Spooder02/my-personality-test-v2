from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
        verbose_name="생성 일시",
        help_text="데이터가 생성된 날짜입니다."
    )
    
    class Meta:
        abstract = True