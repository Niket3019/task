from django.contrib import admin
from .models import Project, Task, team_member

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(team_member)
