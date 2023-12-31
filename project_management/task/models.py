from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.name
    
class team_member(models.Model):
    first_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    def __str__(self):
        return self.first_name
    
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank = True,null = True)
    start_date = models.DateField(null = True,blank = True)
    deadline = models.DateField(null = True,blank = True)
    status_choices = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices)
    assignee = models.ForeignKey(team_member, on_delete=models.CASCADE) 
    def __str__(self):
            return self.assignee.first_name
    
