from django.db import models

# Create your models here.
class Todo(models.Model):
    TASK_COMPLETION = [
        ('N', 'Not Started'),
        ('P', 'In Progress'),
        ('F', 'Finished')
    ]
    title = models.CharField(max_length=120)
    description = models.TextField(default = "")
    completed = models.CharField(max_length = 1, choices = TASK_COMPLETION,default='N')

    def _str_(self):
        return self.title