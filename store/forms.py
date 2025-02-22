from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	phone = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
	# last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'phone', 'email', 'password1', 'password2')
		exclude = ('first_name', 'last_name')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class UserImg(UserCreationForm):
    image = forms.ImageField(label='')
    class Meta:
        model = User
        fields = ['image']
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from .models import Profile

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
#     phone = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))

#     class Meta:
#         model = User
#         fields = ('username', 'phone', 'email', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['username'].widget.attrs['placeholder'] = 'User Name'
#         self.fields['username'].label = ''
#         self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['placeholder'] = 'Password'
#         self.fields['password1'].label = ''
#         self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

#         self.fields['password2'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
#         self.fields['password2'].label = ''
#         self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

    # def save(self, commit=True):
    #     user = super(SignUpForm, self).save(commit=False)
    #     if commit:
    #         user.save()
    #         phone = self.cleaned_data.get('phone')
    #         Profile.objects.create(user=user, phone=phone)
    #     return user

