from django import forms
from . models import blog

class blog_from(forms.ModelForm):
    class Meta :
        model=blog

        fields=["blog_name","blog_info","blog_detail","blog_pic"]
        widgets = {
            'blog_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your Blog name'}),
            'blog_info': forms.Textarea(
                attrs={'class': 'form-control', 'rows':2 }),
            'blog_detail': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'blog_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

