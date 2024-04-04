from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Object, Respondent
from .forms import RespondentForm

def send_data(request):
    if request.method == 'POST':
        responder_form = RespondentForm(request.POST)

        if responder_form.is_valid():
            responder = responder_form.save(commit=False)
            responder.author = request.user
            responder.created_date = timezone.now()
            responder.save()
            return HttpResponse("Успешно!", status=200)
        else:
            return HttpResponse("Форма заполнена неправильно", status=400)
    else:
        responder_form = RespondentForm()

    # TODO: Редирект на основную страницу

def lending_view(request):

    return render(request, 'lending/index.html')

def valera_view(request):
    objects = Object.objects.all()
    return render(request, 'lending/lending.html', {'objects': objects})