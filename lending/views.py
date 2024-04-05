import json

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Object, Annotation, SelectedObject, PhotoCarousel
from .forms import RespondentForm

from django.http import JsonResponse

def lending_view(request):
    if request.method == 'POST':
        responder_form = RespondentForm(request.POST)

        if responder_form.is_valid():
            responder= responder_form.save(commit=False)
            responder.created_date = timezone.now()
            responder.save()

            # Получаем данные из JavaScript
            selected_objects = request.POST.get('selectedObjects')
            selected_objects = json.loads(selected_objects)  # Преобразование строки JSON в список Python

            if not selected_objects:
                return HttpResponse("Форма заполнена неправильно", status=400)

            for objectId in selected_objects:
                object_from_base = Object.objects.get(id=objectId)
                object_from_base.number_of_votes += 1
                object_from_base.save()
                selected_objects = SelectedObject(coordinate=None, object=object_from_base, respondent=responder)
                selected_objects.save()

            return HttpResponse("Успешно!", status=200)
        else:
            return HttpResponse("Форма заполнена неправильно", status=400)
    else:
        form = RespondentForm()
        objects = Object.objects.all()
        annotations = Annotation.objects.all()
        carousel_items = PhotoCarousel.objects.all()
    return render(request, 'lending/index.html', {'form': form, 'objects': objects, 'annotations': annotations,
                                                  'carousel_items': carousel_items})


def valera_view(request):
    objects = Object.objects.all()
    return render(request, 'lending/lending.html', {'objects': objects})

