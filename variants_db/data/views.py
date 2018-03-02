from django.shortcuts import HttpResponse
from django.template import loader
from data.models import Sample

def index(request):
    all_samples = Sample.objects.all().order_by('last_name')
    template = loader.get_template('data/index.html')
    context = {'all_samples' : all_samples,
    }
    return  HttpResponse(template.render(context, request))

def detail(request, sample_id):
    sample_info = Sample.objects.all().filter(id=sample_id)
    template = template = loader.get_template('data/details.html')
    context = {'sample_info':sample_info,
    }
    return  HttpResponse(template.render(context, request))
#    return HttpResponse("<h2>Details for Sample id: " + sample_id + "</h2>")
