import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from .models import Object, Annotation, SelectedObject, PhotoCarousel, TextMainInfo
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
        text_main_info = TextMainInfo.objects.all()
        try:
            text_main_info = text_main_info[0]
        except Exception as e:
            text_main_info.title = "Информация"
            text_main_info.text = "Информация о нас"
    return render(request, 'lending/index.html', {'form': form, 'objects': objects, 'annotations': annotations,
                                                  'carousel_items': carousel_items, 'text_main_info': text_main_info})

class LendingView(View):
    template_name = "lending/index.html"
    context = {
        'title': '',
        'objects': Object.objects.all(),
        'form': RespondentForm(),
        'form_submitted': False,  # Флаг для отслеживания успешной отправки формы
    }

    def get(self, request):
        objects = Object.objects.all()
        form = RespondentForm()
        # context = {
        #     'title': '',
        #     'objects': objects,
        #     'form': form,
        #     'form_submitted': False,  # Флаг для отслеживания успешной отправки формы
        # }
        self.context.update({'form_submitted': False})
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = RespondentForm(request.POST)
        if form.is_valid():
            form.instance.is_verificated = False
            responder = form.save(commit=False)
            responder.created_date = timezone.now()
            responder.save()


            selectedObjects = request.POST.get('selectedObjects')
            selectedObjects = json.loads(selectedObjects)  # Преобразование строки JSON в список Python

            if not selectedObjects:
                return HttpResponse("Форма заполнена неправильно", status=400)

            for objectId in selectedObjects:
                # Создаем экземпляр SelectedObject для каждого выбранного объекта
                selected_object = Object.objects.get(id=objectId)
                selectedObject = SelectedObject.objects.create(
                    respondent=responder, selected_object=selected_object, coordinate=None
                )
                selectedObject.save()

            # Устанавливаем флаг успешной отправки формы в True
            self.context.update({'form_submitted': True})
            self.context.update({'form': RespondentForm()})
            return render(request, self.template_name, self.context)
        else:
            # Если форма не прошла валидацию, возвращаем ее с ошибками
            # context = {'form': form, 'form_submitted': False}
            self.context.update({'form_submitted': False})
            self.context.update({'form': form})
            return render(request, self.template_name, self.context)

def valera_view(request):
    objects = Object.objects.all()
    return render(request, 'lending/lending.html', {'objects': objects})

