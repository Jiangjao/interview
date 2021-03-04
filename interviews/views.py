from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from jobs.models import Job
from jobs.models import Cities, JobTypes

def joblist(request):
    job_list = Job.request.order_by('job_type')
    template = loader.get_template('joblist.html')
    context = {'job_list':job_list}
    
    for job in job_list:
        job.city_name = Cities(job.job_city)
        job.job_type = JobTypes(job.job_type)

    return HttpResponse(template.render(context))