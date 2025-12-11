from django.db import models
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", help_text="Введите заголовок")
    text = models.TextField(verbose_name="Текст", help_text="Введите текст")
    image_url = models.ImageField(blank=True, null=True, verbose_name="Изображение", help_text="Добавьте изображение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name="Автор поста", help_text="Введите автора поста")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="Пост", help_text="Введите пост")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="Автор", help_text="Введите автора")
    text = models.TextField(verbose_name="Текс", help_text="Введите текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
