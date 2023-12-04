from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(max_length=50, label="Password", widget=forms.PasswordInput)


class EditUserForm(forms.Form):
    password = forms.CharField(max_length=50, label="Old Password", widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=50, label="New Password", widget=forms.PasswordInput)
    new_password_reentered = forms.CharField(max_length=50, label="New Password Again", widget=forms.PasswordInput)
