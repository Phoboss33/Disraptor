from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Respondent, Object, SelectedObject, ChangeLog

class RespondentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30,
            widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваше имя'
        }),)
    surname = forms.CharField(max_length=30,
            widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите вашу фамилию'
        }),)
    patronymic = forms.CharField(max_length=30, required=False,
            widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваше Отчество'
        }),)
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите вашу дату рождения',
            'type': 'date'
        })
    )
    sex = forms.ChoiceField(
        choices=[('male', 'Мужской'), ('female', 'Женский')],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Respondent
        fields = ['first_name', 'surname', 'patronymic', 'birthdate', 'sex', 'suggestions']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вашу фамилию'
            }),
            'patronymic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше Отчество'
            }),
            'birthdate': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вашу дату рождения',
                'type': 'date'
            }),
            'sex': forms.Select(attrs={
                'class': 'form-control'
            }),
            'suggestions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Введите ваши предложения или пожелания для проекта'
            })
        }

    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        if birthdate and birthdate > timezone.now().date():
            raise ValidationError("Дата рождения не может быть в будущем.")
        return birthdate

