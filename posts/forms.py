from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce import TinyMCE
from .models import Post, Comment


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
  
  
class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )
    class Meta:
        model = Post
        fields = ('title', 'overview', 'content','thumbnail', 'categories',
        'featured', 'previous_post', 'next_post')

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs = {
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
    # CommentForm.Meta.fields cannot be a string. Did you mean to type: ('content',)? 
        model = Comment
        fields = ('content',)