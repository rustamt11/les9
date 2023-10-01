from django.db import models
from django.urls import reverse

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})
