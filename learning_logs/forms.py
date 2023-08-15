from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """ Make the form for new topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    """ Make form for new Entries"""
    class Meta:
        model = Entry
        fields = ['texts']
        labels = {'texts': ''}
        widgets = {'texts': forms.Textarea(attrs={"cols": 80})}
