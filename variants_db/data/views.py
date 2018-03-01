from django.shortcuts import HttpResponse

from data.models import Sample

def index(request):
    list_of_patient_names = Sample.objects.values()
    return HttpResponse(list_of_patient_names)
#    return HttpResponse("This is going to be a variant database. Work in Progress")
