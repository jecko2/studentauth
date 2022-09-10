from multiprocessing.dummy import Value
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomeUserManager(BaseUserManager):
    """
    create user by the email
    Args:
        BaseUserManager (email): 
        pass in email as the default authorization
    """
    def create_user(self, email, password, **kwargs):
        
        if not email:
            raise ValueError(_("Email must be set"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)
        
        if kwargs.get("is_staff") is not True:
            raise ValueError(_("superuser must be set to is_staff=True"))

        if kwargs.get("is_superuser") is not True:
            raise ValueError(_("superuser must be set to is_superuser=True"))

        if kwargs.get("is_active") is not True:
            raise ValueError(_("superuser must be set to is_active=True"))
        
        return self.create_user(email, password, **kwargs)
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomeUserManager()
    
    def get_short_name(self):
        email = self.email.strip()
        return email[:email.index("@")]

    def __str__(self):
        return self.email