from django import forms

from .models import Respondent, Object, SelectedObject, ChangeLog

class RespondentForm(forms.ModelForm):

    class Meta:
        model = Respondent
        fields = ('surname', 'first_name', 'patronymic', 'birthdate', 'sex', 'suggestions')