from django.shortcuts import render
from webapp.models import Project
from random import shuffle

def index(request):
    context_dict = {}
    context_dict['projects'] = Project.objects.all()
    return render(request, 'webapp/index.html', context_dict);

def project(request, project_name_slug):

    context_dict = {}

    try:
        project = Project.objects.get(slug=project_name_slug)
        other = Project.objects.exclude(name=project.name)
        context_dict['project'] = project
        context_dict['other'] = other

    except Project.DoesNotExist:
        print "Project doesn't exist"
        return index(request)

    return render(request, 'webapp/projectpage.html', context_dict)
        
        
