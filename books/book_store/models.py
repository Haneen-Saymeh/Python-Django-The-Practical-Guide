from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name= models.CharField(max_length=50)
    code= models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "countries"

class Address(models.Model):
    street= models.CharField(max_length=80)
    post_code = models.CharField(max_length=5)
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city} {self.street}"
    
    class Meta:
        verbose_name_plural = "address entries"


class Author(models.Model):
    firstName= models.CharField(max_length=100)
    lastName= models.CharField(max_length=100)
    address= models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Book(models.Model):
    title=models.CharField(max_length=50)
    rating= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author= models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE, null = True)
    is_bestSelling= models.BooleanField(default=False)
    slug= models.SlugField(default="", blank= True,null=False, db_index=True)
    countries= models.ManyToManyField(Country, related_name="books")


    def get_absolute_url(self):
        return reverse("one_book", args=[self.id])

    def save(self, *args, **kwargs):
        self.slug= slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

