from django.db import models

from .common import BaseModel


class testContent(BaseModel):  # 필드와 그 옵션을 정의합니다.
    title = models.CharField(
        max_length=20,
        verbose_name="테스트 제목",
        help_text="테스트 제목 입니다."
    )
    description = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="테스트 설명",
        help_text="테스트 설명 입니다."
    )
    author = models.CharField(
        max_length=10,
        verbose_name="테스트 작성자",
        help_text="테스트 작성자를 나타냅니다."
    )

    class Meta:
        verbose_name = '테스트 리스트'
        verbose_name_plural = '테스트 리스트(들)'
        ordering = ['-created_at']