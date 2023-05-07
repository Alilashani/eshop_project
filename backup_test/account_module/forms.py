from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class Register_Form(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ],
        # error_messages={
        #     'لطفا ایمیل خود را وارد کنید!!!'
        # }
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if confirm_password == password:
            return confirm_password
        raise ValidationError('رمز عبور نادرست است ')


class Login_Form(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ],
        # error_messages={
        #     'لطفا ایمیل خود را وارد کنید!!!'
        # }
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


class Forget_Password_Form(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ],
        # error_messages={
        #     'لطفا ایمیل خود را وارد کنید!!!'
        # }
    )


class Reset_Password_Form(forms.Form):
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
