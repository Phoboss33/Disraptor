import json

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Object, Annotation, SelectedObject
from .forms import RespondentForm

from django.http import JsonResponse

def lending_view(request):
    if request.method == 'POST':
        responder_form = RespondentForm(request.POST)

        if responder_form.is_valid():
            responder = responder_form.save(commit=False)
            responder.created_date = timezone.now()
            responder.save()

            # Получаем данные из JavaScript
            selectedObjects = request.POST.get('selectedObjects')
            selectedObjects = json.loads(selectedObjects)  # Преобразование строки JSON в список Python

            print(selectedObjects)
            for objectId in selectedObjects:
                print(objectId)
                # Создаем экземпляр SelectedObject для каждого выбранного объекта
                selected_object = Object.objects.get(id=objectId)
                selectedObject = SelectedObject.objects.create(
                    respondent=responder, selected_object=selected_object, coordinate=None
                )
                selectedObject.save()

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

