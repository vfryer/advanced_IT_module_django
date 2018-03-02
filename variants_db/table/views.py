from django.shortcuts import render
# from django.shortcuts import HttpResponse
from django_tables2 import RequestConfig
#from django.template import loader
from .models import Variants
from .tables import VariantTable

def table(request):
#    all_variants = Variants.objects.all().order_by('cdna_variant')
    table = VariantTable(Variants.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'layout.html', {'table': table})

#    template = loader.get_template('table/layout.html')
#    context = {'all_variants' : all_variants,
#    }
#    return  HttpResponse(template.render(context, request))
