from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Book(models.Model):

    title = models.CharField(max_length=70, verbose_name="заголовок")
    description = models.TextField(verbose_name="описание")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="продукты", null=True)

    class Meta:
        verbose_name = "Книги"
        verbose_name_plural = "Книга"

