from django import forms
from .models import Post, Category, Comment

# choices = [('coding', 'coding'), ('python', 'python'), ('django', 'django')]
choices = Category.objects.all().values_list('name', 'name')
choices_list = []
for choice in choices:
    choices_list.append(choice)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter Your Title Blog Post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'user', 'type': 'hidden'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Give a title for post.'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body', 'by')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'by': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
        }