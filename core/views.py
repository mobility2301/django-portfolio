from django.shortcuts import render, get_object_or_404
from .models import ContactMessage, Project, Profile

# Create your views here.


def home(request):
    projects = Project.objects.all().order_by('-created_at')
    profile = Profile.objects.first() 
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
    return render(request, 'core/home.html', {'projects': projects, 'profile': profile})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'core/project_detail.html', {'project': project})
