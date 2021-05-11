from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):

    def created_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email address.")

        user = self.model(
            email=self.normalize_email(email),

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.created_user(
            email=self.normalize_email(email),
            password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, filename):
    return f'profiles_images/{self.pk}/{"profile_image.png"}'


def get_default_profile_image():
    return "projectimages/010.jpg"


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True,null=False)
    # username = models.CharField(max_length=30, unique=True)
    data_Joined = models.DateTimeField(verbose_name="data Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True,
                                      default=get_default_profile_image)
    # hide_email = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profiles_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_superuser

