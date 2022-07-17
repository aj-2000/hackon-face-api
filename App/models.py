
from djongo import models
from djongo.models.indexes import Co

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=1024)
    full_name = models.CharField(max_length=255)
    img_url = models.URLField()
    encoding = models.CharField(max_length=5000)

    class Meta:
        indexes = [
            TextIndex(fields=['username', 'password'])
        ]
    


