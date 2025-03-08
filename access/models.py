from django.utils.translation import gettext_lazy as _
from django.db import models
from common.models import AbstractModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):

    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **kwargs):
        kwargs["is_admin"] = False
        return self._create_user(email,password, **kwargs)
    
    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs["is_admin"] = True
        return self._create_user(email, password, **kwargs)



class User(AbstractModel, AbstractBaseUser):
    
    email = models.EmailField(
        _("Email"),
        max_length=128,
        unique=True,
        db_index=True,
    )

    name = models.CharField(_("Name"), max_length=32, blank=True)   
    password = models.CharField(_("Password"), max_length=128)
    is_active = models.BooleanField(
        _("Active"),
        help_text=_("Designates whether this user can access into their account."),
        default=True,
    )
    is_admin = models.BooleanField(
        _("Admin"),
        help_text=_("Designates whether the user can log into this admin site."),
        default=False,
    )
    is_staff = models.BooleanField(
        _("Staff"),
        help_text=_("Designates whether the user can log into this admin site."),
        default=False,
    )
    is_superuser = models.BooleanField(
        _("Superuser"),
        help_text=_("Designates whether the user has all permissions without explicitly assigning them."),
        default=False,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return f"{self.email} ({self.name})"
    
    
    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_admin
    
    def has_module_perms(self, app_label):
        return self.is_active and self.is_admin
    
    def get_all_permissions(self, obj=None):
        return []
    
    class Meta(AbstractModel.Meta):
        verbose_name = _("User")
        verbose_name_plural = _("Users")