from django.contrib.auth.models import (
    BaseUserManager
)


class MyUserManager(BaseUserManager):
    def create_user(self,first_name,last_name ,email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not first_name:
            raise ValueError('First name required')

        if not last_name:
            raise ValueError('Last name required')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.first_name=first_name
        user.last_name=last_name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user