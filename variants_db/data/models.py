from django.db import models

class Variant(models.Model):
    cDNA_change = models.CharField('cDNA_change', max_length=200)
    protein_change = models.CharField('Protein_change', max_length=200)
    genomic_change = models.CharField('Genome_change', max_length=200)

class Patient(models.Model):
    name = models.CharFiled('Name', max_length=100)
    stage = models.IntegerField('Stage', default=0)
