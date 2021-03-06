from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

#사용자 생성폼
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('nickname', 'email', 'date_of_birth', 'is_seller')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
        #패스워드1과 패스워드2가 일치하는지 검사

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

#사용자 수정폼
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField() #사용자 암호를 화면에 표시

    class Meta:
        model = User
        fields = ('nickname', 'email', 'date_of_birth', 'is_seller')

    def clean_password(self): #패스워드를 그대로 다시 저장
        return self.initial["password"]