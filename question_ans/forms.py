from .models import Question,Answer
from django import forms
from tinymce.widgets import TinyMCE

class QuestionForm(forms.ModelForm):
    class Meta:
        content = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows':30}))
        model = Question
        fields = ['title', 'tags', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': ' w-full bg-white my-2 rounded border border-gray-300 focus:border-green-500 dark:text-gray-200 dark:bg-gray-600 dark:focus:bg-gray-700 dark:border-gray-600 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out','placeholder':"Enter your question title",'name':'title'}),
            'tags': forms.TextInput(attrs={'class': ' w-full bg-white my-2 rounded border border-gray-300 focus:border-green-500 dark:text-gray-200 dark:bg-gray-600 dark:focus:bg-gray-700 dark:border-gray-600 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out','placeholder':"Enter a tag like e.g. C++ JAVA PYTHON",'name':'tags'}),
        }

class AnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
    class Meta:
        answer = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows':30}),label='')
        model = Answer
        fields = ['answer']