from django import forms
from ckeditor.widgets import CKEditorWidget   #widget which adds rich text editor without image uploader
from .models import *


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ("maquinaria", "marca", "usuario", "imagen", "detalle")
