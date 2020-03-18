from django.db import models

class Patient(models.Model):
    patient_id = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.patient_id)
    
    def biospecimen_count(self):
        return self.biospecimen_set.all().count()
    
class Biospecimen(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    type = models.CharField(max_length=120)
    aliquot_count = models.IntegerField(default=1)
    sample_date = models.DateField()
    
    def __str__(self):
        return '{} - {}'.format(self.type, self.sample_date)