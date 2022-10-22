from django.db import models

from .common import BaseModel

class Todo(BaseModel):
    title = models.CharField(
        max_length=20,
        verbose_name="테스트 제목",
        help_text="테스트 제목입니다."
    )
    description = models.CharField(
        max_length=64,
        null=False,
        blank=True,
        verbose_name="테스트 설명",
        help_text="테스트 설명입니다."
    )
    author = models.CharField(
        max_length=10,
        verbose_name="테스트 제작자",
        help_text="테스트 제작자를 나타냅니다."
    )

    class Meta:
        verbose_name = '테스트'
        verbose_name_plural = '테스트(들)'
        ordering = ['created_at']

    def __str__(self):
        return f"Testdata-{self.author}-{self.created_at}"