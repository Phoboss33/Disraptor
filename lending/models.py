from django.conf import settings
from django.db import models
from django.utils import timezone


class Object(models.Model):
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    number_of_votes = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.price}\n{self.description}"


class Respondent(models.Model):
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField()
    sex = models.CharField()

    suggestions = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.surname} {self.first_name} {self.patronymic}"


class ChangeLog(models.Model):
    respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reason_for_change = models.TextField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Респондент: {self.respondent.surname} {self.respondent.first_name} {self.respondent.patronymic}"


class SelectedObject(models.Model):
    coordinate = models.CharField(max_length=5)
    respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
    selected_object = models.OneToOneField(Object, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.respondent.surname} {self.respondent.first_name}\n" \
               f"{self.selected_object.title}"
