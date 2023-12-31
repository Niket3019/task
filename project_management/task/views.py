from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Project, Task, team_member


def project_list_get(request):
    return render(request, 'task/project_list.html')
@csrf_exempt
def add_task(request,task_id = 0):
    projects = Project.objects.all()
    project_data = [{'id': project.id, 'name': project.name, 'description': project.description,
                         'start_date': project.start_date.strftime('%Y-%m-%d'),
                         'end_date': project.end_date.strftime('%Y-%m-%d')} for project in projects]
    user_obj = team_member.objects.all()
    if request.method == 'POST':
        data = json.loads(request.body)
        project_id = data.get('project_id')
        title = data.get('title')
        description = data.get('description')
        deadline = data.get('end_date')
        status = data.get('status')
        assign = data.get('assigned_to')
        start = data.get('start_date')

        project_obj = get_object_or_404(Project, pk=int(project_id))
        user_obj = get_object_or_404(team_member,pk=int(assign))
        try:
            task_obj = Task.objects.get(project = project_obj)
            return JsonResponse({'status': f'This Project Already Assign To {task_obj.assignee.first_name}', 'task_id': task_obj.id},status = 400)
        except:
            task_obj = Task()
            task_obj.project=project_obj
            task_obj.title=title
            task_obj.description=description
            task_obj.deadline=deadline
            task_obj.status=status
            task_obj.assignee=user_obj
            task_obj.start_date = start
            task_obj.save()
            return JsonResponse({'status': 'successfully added', 'task_id': task_obj.id})
    elif request.method == 'DELETE':
        print("============ayaaa")
        data = json.loads(request.body)
        if data.get("task_id"):
            try:
                print("===============okokok")
                task_obj = Task.objects.get(pk=int(data.get("task_id"))).delete()
                
            except Exception as  e:
                return JsonResponse({'status': str(e)},status = 400)
            return JsonResponse({'status': 'successfully deleted'})
    return render(request, 'task/add_task.html',context={"projects":project_data,"user_obj":user_obj})

@csrf_exempt
def add_projects(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        add_projects = Project()
        add_projects.name = data.get("name")
        add_projects.description = data.get("description")
        add_projects.start_date = data.get("start_date")
        add_projects.end_date = data.get("end_date")
        add_projects.save()

        return JsonResponse({'status': 'success'})
    return render(request, 'task/add_projects.html')

@csrf_exempt
def task_list(request):
    tasks_obj = Task.objects.order_by('-id')
    return render(request, 'task/task_list.html',context={"tasks":tasks_obj})

@csrf_exempt
def edit_task(request,task_id=0):
    is_edit = True
    projects = Project.objects.all()
    try:
        task_details = Task.objects.get(pk=task_id)
    except:
        task_details = None
    print("==========>task_id",task_id)
    if request.method == "POST":
        data = json.loads(request.body)
        project_id = data.get('project_id')
        title = data.get('title')
        description = data.get('description')
        deadline = data.get('end_date')
        status = data.get('status')
        start = data.get('start_date')
        print("==========>task_id",task_id)
        if task_id:
            print("=========task_idcdfd",task_id)
            try:
                task_obj = Task.objects.get(pk=task_id)
                task_obj.project_id=project_id
                task_obj.title=title
                task_obj.description=description
                task_obj.deadline=deadline
                task_obj.status=status

                task_obj.start_date = start
                task_obj.save()
            except  Exception as e:
                return JsonResponse({'status': str(e)},status=400)
            
            return JsonResponse({'status': 'successfully  edited', 'task_id': task_obj.id})
    return render(request, 'task/add_task.html',context={"projects":projects,"task_details":task_details,"is_edit":is_edit})

@csrf_exempt
def add_team_member(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("=======data",data)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email =data.get('email')
        try:
            team_member.objects.get(email = email)
            return JsonResponse({'error':'User already exists'},status=409)
        except:
            team_member.objects.create(first_name=first_name, last_name=last_name, email=email)
            return JsonResponse({'status': 'successfully  added team member'})
    return render(request, 'task/add_team_member.html')