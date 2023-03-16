from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _


class UserCacheMixin:
    user_cache = None


class SignIn(UserCacheMixin, forms.Form):
    password = forms.CharField(label=_(''), help_text=_("Password"), strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if settings.USE_REMEMBER_ME:
            self.fields['remember_me'] = forms.BooleanField(label=_('Remember me'), required=False)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise ValidationError(_('You entered an invalid password.'))

        return password


class SignInViaUsernameForm(SignIn):
    username = forms.CharField(label=_(''), help_text=_("Username"), max_length=150)

    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['username', 'password', 'remember_me']
        return ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']

        user = User.objects.filter(username=username).first()
        if not user:
            raise ValidationError(_('You entered an invalid username.'))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user

        return username


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label=_(''), help_text=_("Password"), strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label=_(''), help_text=_("Password confirmation"), strip=False,
                                widget=forms.PasswordInput)
    username = forms.CharField(label=_(''), help_text=_("Username"), max_length=150)
    first_name = forms.CharField(label=_(''), help_text=_("First name"), max_length=30, required=False)
    last_name = forms.CharField(label=_(''), help_text=_("Last name"), max_length=150, required=False)

    class Meta:
        model = User
        fields = settings.SIGN_UP_FIELDS


class ChangeProfileForm(forms.Form):
    first_name = forms.CharField(label=_(''), help_text=_("First name"), max_length=30, required=False)
    last_name = forms.CharField(label=_(''), help_text=_("Last name"), max_length=150, required=False)


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_(''), help_text=_("Old password"), strip=False, widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=_(''), help_text=_("New password"), strip=False, widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=_(''), help_text=_("New password confirmation"), strip=False,
                                    widget=forms.PasswordInput)
