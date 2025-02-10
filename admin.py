from django import forms
from django.contrib import admin
from .models import Test, Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'correct_answer', 'question_type', 'choices']
    
    def clean_choices(self):
        choices = self.cleaned_data.get('choices')
        if choices:
            return [choice.strip() for choice in choices.split(',')]
        return []

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    list_display = ('question_text', 'question_type', 'correct_answer')
    list_filter = ('question_type',)


class TestAdmin(admin.ModelAdmin):
    list_display = ('title',)  
    search_fields = ('title',)  

admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)