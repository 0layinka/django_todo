from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, default=None, null=False)
    description = models.TextField()
    achieved = models.BooleanField()
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title