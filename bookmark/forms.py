from django import forms
from .models import Bookmark

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['name', 'url', 'thumbnail_image_url']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance