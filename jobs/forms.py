from django import forms
from .models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = '__all__'
        # labels = {
        #     'title': 'Alias from da wae',
        #     'art': 'Message for da wae',
        # }
        # help_texts = {
        #     'title': ('(Username)'),
        #     'art': ('Message you want to send to the masses'),
        # }