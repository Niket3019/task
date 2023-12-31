from django.urls import path
from .views import add_task, project_list_get, add_projects, task_list, edit_task, add_team_member

urlpatterns = [
    path('tasks/add/', add_task, name='add_task'),
    path('tasks/project_list_get/', project_list_get, name='project_list_get'),
    path('tasks/api/add_projects/', add_projects, name='add_projects'),
    path('tasks/api/task_list/', task_list, name='task_list'),
    path('tasks/api/edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('tasks/add_team_member/',add_team_member,name = "add_team_member")
]
