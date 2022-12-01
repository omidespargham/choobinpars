from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User, RGScode

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=11,validators=[])

    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"]
        # start with validation added
        if phone[0:2] != "09":
            raise ValidationError([ValidationError("شماره تلفن نامعتبر است",code="invalid"),ValidationError("تلفن باید با 09 شروع شود",code="required")])
        try:
            code = RGScode.objects.get(phone_number=phone)
            code.delete()
        except RGScode.DoesNotExist:
            pass
        return phone
class LoginVerifyForm(forms.Form):
    code = forms.IntegerField()

    def clean_code(self):
        code = self.cleaned_data["code"]
        try:
            the_code = RGScode.objects.get(code=code)
            the_code.delete()
            return code
        except RGScode.DoesNotExist:
            raise ValidationError("کد نامعتبر است.")
class UserCreationForm(forms.ModelForm):
    # password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number', "password")

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
    #         raise ValidationError('password dont match')
    #     return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you can change password using <a href=\"../password/\">this form</a>")

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'last_login')
