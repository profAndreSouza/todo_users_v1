import hashlib
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserEntity(AbstractUser):
    
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='media/profiles/',
        null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.password = hashlib.md5(self.password.encode()).hexdigest()
        super().save(*args, **kwargs)

# pbkdf2_sha256
# pbkdf2_sha1
# argon2
# bcrypt_sha256
# bcrypt
# scrypt
# md5