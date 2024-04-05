from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from lending.forms import RespondentForm
from lending.models import Respondent, Object
from volunteer.forms import RespondentSearchForm, UserProfileEditForm


def respondent_search_view(request):
    if request.user.is_authenticated and request.user.groups.all():
        if request.method == 'POST':
            form = RespondentSearchForm(request.POST)

            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                surname = form.cleaned_data.get('surname')
                patronymic = form.cleaned_data.get('patronymic')
                birthdate = form.cleaned_data.get('birthdate')
                sex = form.cleaned_data.get('sex')

                if birthdate:
                    respondents = Respondent.objects.filter(
                        first_name__icontains=first_name,
                        surname__icontains=surname,
                        patronymic__icontains=patronymic,
                        birthdate=birthdate,
                        sex=sex
                    )
                else:
                    respondents = Respondent.objects.filter(
                        first_name__icontains=first_name,
                        surname__icontains=surname,
                        patronymic__icontains=patronymic,
                        sex=sex
                    )

                return render(request, 'volunteer/respondent_search_results.html', {'respondents': respondents, 'form': form})
        else:
            form = RespondentSearchForm()

        return render(request, 'volunteer/respondent_search.html', {'form': form})
    return redirect('login')


def respondent_edit_view(request, pk):
    if request.user.is_authenticated and request.user.groups.all():
        respondent = get_object_or_404(Respondent, pk=pk)
        if request.method == "POST":
            form = RespondentForm(request.POST, instance=respondent)
            if form.is_valid():
                respondent = form.save()
                return redirect('respondent_detail', pk=respondent.pk)
        else:
            form = RespondentForm(instance=respondent)
        return render(request, 'volunteer/respondent_edit.html', {'form': form})

    return redirect('login')

def volunteer_cabinet(request):
    if request.user.is_authenticated:
        if request.POST:
            print("TODO: Изменить данные пользователя")
            # TODO: Изменить данные пользователя

        return render(request, 'volunteer/volunteer.html', {'form': UserProfileEditForm, 'user': request.user})

    return redirect('login')

def data_panel(request):
    if request.user.is_authenticated and request.user.groups.all():
        if request.POST:
            print("TODO: Вывод данных")
            # TODO: Изменить данные пользователя
        objects = Object.objects.all()
        return render(request, 'volunteer/show_data.html', {'user': request.user, 'objects': objects})

    return redirect('login')