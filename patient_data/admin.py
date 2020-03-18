from django.contrib import admin
from . import models



class BiospecimenChildAdmin(admin.TabularInline):    # can also use TabularInline
    model = models.Biospecimen
    extra = 3

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'gender', 'comment', 'biospecimen_count')
    inlines = [BiospecimenChildAdmin]
    
admin.site.register(models.Patient, PatientAdmin)


class BiospecimenAdmin(admin.ModelAdmin):
    list_display = ('type', 'aliquot_count', 'sample_date', 'patient')
    
admin.site.register(models.Biospecimen, BiospecimenAdmin)