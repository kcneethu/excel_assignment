from django.db import models

# Create your models here.
class Exceldata(models.Model):
    data_id     = models.AutoField(primary_key=True)
    color       = models.CharField(max_length=50, null=True)
    group       = models.CharField(max_length=50, null=True)
    size        = models.IntegerField( null=True)
    article     = models.CharField(max_length=100, null=True)
    pairs       = models.IntegerField(null=True) 
    rate        = models.IntegerField(null=True) 
    amount      = models.IntegerField(null=True) 
    created_at  = models.DateTimeField(null=True)
    updated_at  = models.DateTimeField(default = None , null=True)

    class Meta:
        db_table = 'excel_data'