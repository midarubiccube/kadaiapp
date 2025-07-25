from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}), label="ユーザー名")

    password = forms.CharField(
        label="パスワード",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": (
            "正しい ユーザー名 とパスワードを入力してください。"
        ),
        "inactive": ("このアカウントはアクティブではありません"),
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

class UserInfoChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            # 'last_name',
            # 'first_name',
        ]

    def __init__(self, email=None, first_name=None, last_name=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        if email:
            self.fields['email'].widget.attrs['value'] = email
        if first_name:
            self.fields['first_name'].widget.attrs['value'] = first_name
        if last_name:
            self.fields['last_name'].widget.attrs['value'] = last_name

    def update(self, user):
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'department')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super().__init__(*args, **kwargs)

class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
    
    # def save(self, commit=True):
    #     user = User.objects.create_user(
    #         self.cleaned_data["name"],
    #         self.cleaned_data["email"],
    #         self.cleaned_data["password1"],
    #     )
    #     return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'