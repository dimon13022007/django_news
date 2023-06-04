from django.db import models


class DPR(models.Model):
    Departament = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)















