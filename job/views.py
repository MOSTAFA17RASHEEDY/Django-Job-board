import email
from re import I
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .form import ApplyForm, AddForm
# Create your views here.
from .models import job, apply


def job_list(request):

    job_list = job.objects.all()
    paginator = Paginator(job_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs': page_obj}
    return render(request, 'job/job_list.html', context)


def job_details(request, slug):
    job_details = job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_details
            myform.save()
    else:
        form = ApplyForm()

    context = {
        'job': job_details,
        'form': form
    }
    return render(request, 'job/job_details.html', context)


'''
def applyform(request):
    nameOfView = request.POST['name']
    emailOfView = request.POST['e_mail']
    websiteOfView = request.POST['website']
    #cvOfView = request.POST['upload_cv']
    coverlOfView = request.POST['cover_latter']
    if request.method == 'POST':
        applyer = apply(name=nameOfView, email=emailOfView,
                        website=websiteOfView, coverLeter=coverlOfView)
        applyer.save()
    return render(request, 'job/job_list.html')
'''


def add_job(request):

    if request.method == 'POST':
        form1 = AddForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save(commit=False)
            #form1.owner = request.user
            form1.save()
            return redirect(reverse("jobs:job_list"))
    else:
        form1 = AddForm()

    context = {
        "form1": form1
    }
    return render(request, "job/add_job.html", context)
