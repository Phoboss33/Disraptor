from django.conf import settings
from django.db import models
from django.utils import timezone


class Object(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)
    number_of_votes = models.IntegerField(blank=True, default=0)

    def get_id(self):
        return str(self.id)

    def get_price(self):
        if self.price == 0:
            return "Цена: Реализуется за счёт заказчика"
        elif self.price >= 1000000:
            formatted_price = round(self.price / 1000000, 3)
            if formatted_price % 1 == 0:
                return f"Цена: {int(formatted_price)} млн"
            else:
                return f"Цена: {formatted_price:.3f} млн"
        else:
            formatted_price = round(self.price / 1000, 0)
            return f"Цена: {formatted_price:.0f} тыс."

    def show_votes(self):
        return f"Количество голосов: {self.number_of_votes}"

    def __str__(self):
        return f"{self.title} \n{self.description}"


class Respondent(models.Model):
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField()
    sex = models.CharField()

    suggestions = models.TextField(max_length=500, blank=True, default="")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.surname} {self.first_name} {self.patronymic}"


class ChangeLog(models.Model):
    respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reason_for_change = models.TextField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)


class SelectedObject(models.Model):
    coordinate = models.JSONField(null=True, blank=True)
    # respondent_json = models.JSONField(null=True, blank=True)
    respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE)
    # object_json = models.JSONField(null=True, blank=True)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)

    def __str__(self):
        return f"SelectedObject {self.id}"

class Annotation(models.Model):
    photo = models.ImageField()
    modal_photo = models.ImageField()
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)

    def __str__(self):
        return str(self.id)


class PhotoCarousel(models.Model):
    photo = models.ImageField()
    title = models.CharField(blank=True)

