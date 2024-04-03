from django.shortcuts import render

# Create your views here.
from lending.models import Respondent
from volunteer.forms import RespondentSearchForm


def respondent_search_view(request):
    if request.method == 'POST':
        form = RespondentSearchForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            surname = form.cleaned_data.get('surname')
            patronymic = form.cleaned_data.get('patronymic')
            birthdate = form.cleaned_data.get('birthdate')
            sex = form.cleaned_data.get('sex')

            respondents = Respondent.objects.filter(
                first_name__icontains=first_name,
                surname__icontains=surname,
                patronymic__icontains=patronymic,
                birthdate=birthdate,
                sex=sex
            )

            return render(request, 'volunteer/respondent_search_results.html', {'respondents': respondents, 'form': form})
    else:
        form = RespondentSearchForm()

    return render(request, 'volunteer/respondent_search.html', {'form': form})