from django import forms

from .models import Comment, Post, User


class UserForm(forms.ModelForm):
    '''Модель формы для пользователя.'''

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


class PostForm(forms.ModelForm):
    '''Модель формы для поста.'''

    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'image', 'location', 'category')
        widgets = {
            'post': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'format': '%m/%d/%y %H:%M'}),
        }


class CommentForm(forms.ModelForm):

    '''Модель формы для комментария.'''
    text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('text',)
