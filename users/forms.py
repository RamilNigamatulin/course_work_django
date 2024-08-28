from users.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from mailing.forms import StyleFormMixin


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)
        #fields = '__all__'
        #exclude = ('',)


class PasswordResetForm(forms.Form):
    email = forms.EmailField()


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'avatar', 'phone', 'country',)
        # exclude = ('token',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
