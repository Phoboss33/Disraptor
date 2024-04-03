from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Respondent, Object, SelectedObject, ChangeLog

class RespondentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    patronymic = forms.CharField(max_length=30, required=False)
    birthdate = forms.DateField()
    sex = forms.ChoiceField(choices=[('male', 'Мужской'), ('female', 'Женский')])

    class Meta:
        model = Respondent
        fields = ['first_name', 'surname', 'patronymic', 'birthdate', 'sex', 'suggestions']
        labels = {
            'first_name': 'Имя',
            'surname': 'Фамилия',
            'patronymic': 'Отчество',
            'birthdate': 'Дата рождения',
            'sex': 'Пол',
            'suggestions':'Что бы вы хотели предложить',
        }

    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        if birthdate and birthdate > timezone.now().date():
            raise ValidationError("Дата рождения не может быть в будущем.")
        return birthdate

