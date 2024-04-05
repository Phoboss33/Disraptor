from django.contrib import admin
from lending.models import Object, Respondent, ChangeLog, SelectedObject, Annotation, PhotoCarousel, TextMainInfo

admin.site.register(Object)
admin.site.register(Respondent)
admin.site.register(ChangeLog)
admin.site.register(SelectedObject)
admin.site.register(Annotation)
admin.site.register(PhotoCarousel)
admin.site.register(TextMainInfo)