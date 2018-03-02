from django.db import models

class Variants(models.Model):
    sample_number = models.IntegerField('Sample_Number')
    cdna_variant = models.CharField('cDNA_change', max_length=200)
    protein_variant = models.CharField('Protein_change', max_length=200)
    genome_variant = models.CharField('Genome_change', max_length=200)

class Sequencer(models.Model):
    sample_number = models.IntegerField('Sample_Number')
    sequencer = models.CharField('Sequencer', max_length=100)
