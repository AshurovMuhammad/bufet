from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Nomi', max_length=50)
    slug = models.SlugField(max_length=60)
    icon = models.ImageField(upload_to="category/icons/")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField("Nomi", max_length=255)
    description = models.TextField("Tasnifi")
    image = models.ImageField("Rasm")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    is_draft = models.BooleanField("Qoralama", default=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"

    def __str__(self):
        return self.title

