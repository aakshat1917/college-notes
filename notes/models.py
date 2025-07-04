from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)  # Linked to the logged-in user
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    tags = models.CharField(max_length=300)
    file = models.FileField(upload_to='notes/')  # Uploads will go to media/notes/
    is_paid = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
