
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from sisan.models import Department

# Create your models here.

class UserManager(BaseUserManager):
    """
    Create and save user with email
    """
    use_in_migrations = True

    def _create_user(self, username, email, department_id, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        department = Department.objects.get(id=department_id)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, department=department, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, department=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, department, **extra_fields)

    def create_superuser(self, username, email, department, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, department, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='ユーザー名',
        # help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        help_text='この項目は必須です。全角文字、半角英数字、@/./+/-/_ で50文字以下にしてください。',
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        verbose_name='メールアドレス',
        help_text='この項目は必須です。メールアドレスは公開されません。',
        blank=False
    )
    department = models.ForeignKey(
        to="sisan.Department",
        verbose_name="所属学科",
        on_delete=models.PROTECT,
        help_text='所属している学科を選択できます',
        blank=True,
    )

    is_staff = models.BooleanField(
        _('管理者権限'),
        default=False,
        help_text='管理者権限を付与するか選択します',
    )
    
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text='ユーザがアクティブかどうか選択します。',
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'department']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        # abstract = True
        abstract = False

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
