import django
import csv, sys, os
from datetime import *

django_project  = "/home/verity/Desktop/Work/MSc/advanced_IT_module"
sys.path.append(django_project)
os.environ['DJANGO_SETTINGS_MODULE'] ='variants_db.settings'

import django
django.setup()
from table.models import Variants

input_file = "/home/verity/Desktop/Work/MSc/advanced_IT_module/BRCA1_variants_for_Django_db.csv"

with open(input_file) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        table_data = Variants(sample_number = row[0],cdna_variant = row[7],protein_variant = row[8],genome_variant = row[9])
        table_data.save()

