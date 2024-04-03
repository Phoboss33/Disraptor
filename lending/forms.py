from django import forms

from .models import Respondent, Object, SelectedObject, ChangeLog

class RespondentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    patronymic = forms.CharField(max_length=30, required=False)
    birthdate = forms.DateField()
    sex = forms.ChoiceField(choices=[('male', 'Мужской'), ('female', 'Женский')])

    class Meta:
        model = Respondent
        fields = ['first_name', 'surname', 'patronymic', 'birthdate', 'sex']
        labels = {
            'first_name': 'Имя',
            'surname': 'Фамилия',
            'patronymic': 'Отчество',
            'birthdate': 'Дата рождения',
            'sex': 'Пол'
        }
