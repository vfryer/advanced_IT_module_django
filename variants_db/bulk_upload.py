import django
import csv, sys, os
from datetime import *

django_project  = "/home/verity/Desktop/Work/MSc/advanced_IT_module"
sys.path.append(django_project)
os.environ['DJANGO_SETTINGS_MODULE'] ='variants_db.settings'

import django
django.setup()
from data.models import Sample

input_file = "/home/verity/Desktop/Work/MSc/advanced_IT_module/BRCA1_variants_for_Django_db.csv"

with open(input_file) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        sample = Sample(sample_number = row[0],first_name = row[1],last_name = row[2],age = row[3],stage = row[4],type = row[5],sequencer = row[6],cdna_variant = row[7],protein_variant = row[8],genome_variant = row[9])
        sample.save()

#        Sample.sample_number = row[0]
#        Sample.first_name = row[1]
#        Sample.last_name = row[2]
#        Sample.age = row[3]
#        Sample.stage = row[4]
 ##       Sample.type = row[5]
 #       Sample.sequencer = row[6]
 #       Sample.cdna_variant = row[7]
 #       Sample.protein_variant = row[8]
 #       Sample.genome_variant = row[9]
 #       Sample.save()
