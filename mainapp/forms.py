__author__ = 'zz'


from django import forms
from django.core.exceptions import ValidationError


def validate_studentid(value):

    def is_all_digit(string):

        for ch in string:
            if not '0' <= ch <= '9':
                return False
        return True

    if len(value) != 10 or not is_all_digit(value):
        raise ValidationError('please input school id')


class LoginForm(forms.Form):
    schoolid = forms.CharField(max_length=10, validators=[validate_studentid, ])
    password = forms.CharField(widget=forms.PasswordInput)


class CreateNicknameForm(forms.Form):
    nickname = forms.CharField(max_length=14)

