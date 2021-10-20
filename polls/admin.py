from django.contrib import admin
from .models import *
class ChoiceInline(admin.StackedInline):
    model = ChoiceModel

class QuestionAdmin(admin.ModelAdmin):
    list_display=['text']
    inlines = [ChoiceInline]

admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Question,QuestionAdmin)
admin.site.register(ChoiceModel)

# Register your models here.
