from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Object, Annotation
from .forms import RespondentForm

def lending_view(request):
    if request.method == 'POST':
        responder_form = RespondentForm(request.POST)

        # TODO: Проверка JSON с данными по карте

        if responder_form.is_valid():
            responder = responder_form.save(commit=False)
            responder.created_date = timezone.now()
            responder.save()
            return HttpResponse("Успешно!", status=200)
        else:
            return HttpResponse("Форма заполнена неправильно", status=400)
    else:
        form = RespondentForm()
        objects = Object.objects.all()
        annotations = Annotation.objects.all()
    return render(request, 'lending/index.html', {'form': form, 'objects': objects, 'annotations': annotations})

def valera_view(request):
    objects = Object.objects.all()
    return render(request, 'lending/lending.html', {'objects': objects})