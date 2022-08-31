from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')

    def clean_text(self):
        data = self.cleaned_data['text']
        if not len(data):
            raise forms.ValueError('Введите новый текст')
        return data

    def clean_group(self):
        group = self.cleaned_data['group']
        return group
