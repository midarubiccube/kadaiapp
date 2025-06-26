from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


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
            "フィールドでは大文字と小文字が区別される場合があります。"
        ),
        "inactive": ("このアカウントはアクティブではありません"),
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)