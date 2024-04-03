from django import forms
from lending.models import Respondent


class RespondentSearchForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False)
    surname = forms.CharField(max_length=30, required=False)
    patronymic = forms.CharField(max_length=30, required=False)
    birthdate = forms.DateField(required=False)
    sex = forms.ChoiceField(choices=[('male', 'Мужской'), ('female', 'Женский')], required=False)

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

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        surname = cleaned_data.get('surname')
        patronymic = cleaned_data.get('patronymic')
        birthdate = cleaned_data.get('birthdate')
        sex = cleaned_data.get('sex')

        if not any([first_name, surname, patronymic, birthdate, sex]):
            raise forms.ValidationError("Укажите хотя бы один критерий поиска.")

        return cleaned_data
