from .models import Question
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'titleqs my-2  widtha','placeholder':"e.g. Is there an R function for finding the index of an element in a vector?"}),
            'content': forms.Textarea(attrs={'class': 'bodyqs widtha'}),
        }