from django import forms
from lending.models import Respondent
from users.models.users import User


class RespondentSearchForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Введите имя или'
                                 }), )
    surname = forms.CharField(max_length=30, required=False,
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'Введите фамилию или'
                              }), )
    patronymic = forms.CharField(max_length=30, required=False,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Введите Отчество или'
                                 }), )
    birthdate = forms.DateField(required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите дату рождения или',
            'type': 'date'
        })
    )
    sex = forms.ChoiceField(required=False,
        choices=[('male', 'Мужской'), ('female', 'Женский')],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Respondent
        fields = ['first_name', 'surname', 'patronymic', 'birthdate', 'sex']

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


class UserProfileEditForm(forms.ModelForm):
    surname = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите вашу фамилию'
        }),
    )

    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваше имя'
        }),
    )

    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'form-control',
            'placeholder': 'Введите ваш email'
        }),
    )

    class Meta:
        model = User
        fields = (
            'username', 'surname', 'first_name', 'email',
        )
