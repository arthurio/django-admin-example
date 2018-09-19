from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.db.models import Q


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey('Author',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)


class Signature(models.Model):
    value = models.CharField(max_length=30)
    author = models.OneToOneField('Author', on_delete=models.CASCADE)


class City(models.Model):
    author = models.ManyToManyField('Author')


class Author(get_user_model()):
    class Manager(BaseUserManager):
        def get_queryset(self):
            user_queryset = super(Author.Manager, self).get_queryset()
            return user_queryset.filter(Q(book__isnull=False))

    class Meta:
        proxy = True

    objects = Manager.from_queryset(models.QuerySet)()

    def sign(self, book):
        print('To you my friend. {}'.format(book.title))
