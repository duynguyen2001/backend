from django.db import models

# Create your models here.
class Todo(models.Model):
    TASK_COMPLETION = [
        ('N', 'Not Started'),
        ('P', 'In Progress'),
        ('F', 'Finished')
    ]
    PRIORITY_NUMS = [
        (0, "Not Urgent and Not Important"),
        (1, "Not Urgent and Important"),
        (2, "Urgent and Not Important"),
        (3, "Urgent and Important")
    ]
    title = models.CharField(max_length=120)
    description = models.TextField(default = "")
    completed = models.CharField(max_length = 1, choices = TASK_COMPLETION,default='N')
    priority = models.IntegerField(max_length = 1, choices = PRIORITY_NUMS,default=0)
    date = models.DateTimeField(null=True)

    def _str_(self):
        return self.title
    
    class Meta: 
        ordering = ['-priority', '-date']