from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64)
    weight = models.PositiveSmallIntegerField(default=100)


class Topping(PublishedModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64)


class Wrapper(PublishedModel):
    name = models.CharField(max_length=256)


class IceCream(PublishedModel):
    is_on_main = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    description = models.TextField()
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
    )
    toppings = models.ManyToManyField(Topping)
