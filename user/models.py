# import uuid
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('username number is required.')

#         user = self.model(username=username, **extra_fields)
#         if password:
#             user.set_password(password)  # Hash the password before saving
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(username=username, password=password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     class Meta:
#         db_table = 'auth_user'

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     mobile = models.CharField(max_length=15, unique=True, blank=True, null=True)
#     username = models.CharField(max_length=30, unique=True, blank=True, null=True)
#     password = models.CharField(max_length=255, blank=True, null=True)  # Removed unique=True
#     email = models.EmailField(blank=True, null=True)
#     created_by = models.ForeignKey(
#         'self',
#         default=None,
#         null=True,
#         blank=True,
#         on_delete=models.DO_NOTHING,
#         related_name='created_user'
#     )
#     is_deleted = models.BooleanField(default=False)
#     app_version = models.TextField(default="v0.0.0")
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='customuser_set',
#         blank=True,
#         verbose_name='groups',
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#     )

#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='customuser_set',
#         blank=True,
#         verbose_name='user permissions',
#         help_text='Specific permissions for this user.',
#     )

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'  # Use 'mobile' as the unique identifier for authentication
#     REQUIRED_FIELDS = []  # No additional required fields

#     def _str_(self):
#         return str(self.id) or self.username or self.mobile