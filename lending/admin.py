from django.contrib import admin
from lending.models import Object, Respondent, ChangeLog, SelectedObject

admin.site.register(Object)
admin.site.register(Respondent)
admin.site.register(ChangeLog)
admin.site.register(SelectedObject)