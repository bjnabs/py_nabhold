from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border border-primary rounded-0'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border border-primary rounded-0'}),
            'body': forms.Textarea(attrs={'class': 'form-control border border-primary rounded-0'})
        }


class SearchForm(forms.Form):
    query = forms.CharField()
