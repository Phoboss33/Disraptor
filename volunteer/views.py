
from django.shortcuts import render, get_object_or_404, redirect
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from datetime import datetime, date  # Импортируем date из datetime
import io
import urllib, base64
from django.db.models import Count
from django.http import HttpResponse

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
        matplotlib.use('agg')

        # Получение данных из модели
        respondents = Respondent.objects.all()

        if not respondents:
            # Если данных нет, верните сообщение или выполните другие действия
            return HttpResponse("No data available")

        # Вычисление возраста каждого респондента
        today = date.today()
        ages = [(today - respondent.birthdate).days // 365 for respondent in respondents]

        # Создание DataFrame для удобства анализа
        import pandas as pd
        data = {
            'Age': ages,
            'Sex': [respondent.sex for respondent in respondents]
        }
        df = pd.DataFrame(data)

        # Проверка наличия данных перед построением графика
        if df.empty:
            return HttpResponse("No data available")

        # Создание графика
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x='Age', hue='Sex', multiple='stack')
        plt.xlabel('Возраст')
        plt.ylabel('Количество')
        plt.title('Распределение голосовавших по возрасту и полу')
        plt.tight_layout()

        # Преобразование графика в изображение
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        # Преобразование изображения в строку base64
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')

        plt.close()

        objects = Object.objects.all()

        return render(request, 'volunteer/show_data.html', {'user': request.user, 'objects': objects, 'graphic': graphic})

    return redirect('login')
