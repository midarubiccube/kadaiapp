from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": (
            "正しい ユーザー名 とパスワードを入力してください。"
            "フィールドでは大文字と小文字が区別される場合があります。"
        ),
        "inactive": ("このアカウントはアクティブではありません"),
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)