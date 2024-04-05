from django.contrib import admin
from lending.models import Object, Respondent, ChangeLog, SelectedObject, Annotation, PhotoCarousel, TextMainInfo

class ObjectAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'image', 'price', 'description', 'number_of_votes'
    )
    search_fields = (
        'title', 'image', 'price', 'description', 'number_of_votes'
    )


Object._meta.verbose_name = 'Объект'
Object._meta.verbose_name_plural = 'Объекты'


class RespondentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'surname', 'patronymic', 'birthdate', 'sex', 'suggestions', 'created_date'
    )
    search_fields = (
        'first_name', 'surname', 'patronymic', 'birthdate', 'sex', 'suggestions', 'created_date'
    )


Respondent._meta.verbose_name = 'Респондент'
Respondent._meta.verbose_name_plural = 'Респонденты'


class ChangeLogAdmin(admin.ModelAdmin):
    list_display = (
        'respondent', 'editor', 'reason_for_change', 'create_date'
    )
    search_fields = (
        'respondent', 'editor', 'reason_for_change', 'create_date'
    )


ChangeLog._meta.verbose_name = 'Изменение (лог)'
ChangeLog._meta.verbose_name_plural = 'Изменения (логи)'


class SelectedObjectAdmin(admin.ModelAdmin):
    list_display = (
        'coordinate', 'respondent', 'object'
    )
    search_fields = (
        'coordinate', 'respondent', 'object'
    )
    list_filter = (
        'coordinate', 'respondent', 'object'
    )


SelectedObject._meta.verbose_name = 'Выбранный объект'
SelectedObject._meta.verbose_name_plural = 'Выбранные объекте'


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'photo', 'modal_photo', 'text'
    )
    search_fields = (
        'title', 'photo', 'modal_photo', 'text'
    )
    list_filter = (
        'title', 'photo', 'modal_photo', 'text'
    )


Annotation._meta.verbose_name = 'Аннотация'
Annotation._meta.verbose_name_plural = 'Аннотации'


class PhotoCarouselAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'photo',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'title',
    )


PhotoCarousel._meta.verbose_name = 'Карусель фото'
PhotoCarousel._meta.verbose_name_plural = 'Карусель фото'


admin.site.register(Object, ObjectAdmin)
admin.site.register(Respondent, RespondentAdmin)
admin.site.register(ChangeLog, ChangeLogAdmin)
admin.site.register(SelectedObject, SelectedObjectAdmin)
admin.site.register(Annotation, AnnouncementAdmin)
admin.site.register(PhotoCarousel, PhotoCarouselAdmin)
admin.site.register(TextMainInfo)

