from django.db import models

class Raw_data(models.Model):
    sample_number = models.IntegerField('Sample_Number')
    first_name = models.CharField('First_Name', max_length=100)
    last_name = models.CharField('Last_Name', max_length=100)
    age = models.IntegerField('Age')
    stage = models.IntegerField('Stage')
    type = models.CharField('Type', max_length=100)
    sequencer = models.CharField('Sequencer', max_length=100)
    cDNA_variant = models.CharField('cDNA_change', max_length=200)
    protein_variant = models.CharField('Protein_change', max_length=200)
    genomic_variant = models.CharField('Genome_change', max_length=200)