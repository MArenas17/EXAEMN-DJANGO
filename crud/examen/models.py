from django.db import models

# Create your models here.
class Empleado(models.Model):
    Nombre= models.CharField(null=False, blank=False, max_length=20 )
    Cargo = models.CharField(null=False, blank=False, max_length=8)
    Diastrabajados = models.IntegerField(null=False, blank=False)
    Mespagado = models.CharField(null=False, blank=False, max_length=12)
    TotalSalario = models.IntegerField(null=True, default=0)
   
    def __str__(self):
        return self.Nombre


    def save(self, *args, **kwargs):
        existe = Empleado.objects.filter(Nombre = self.Nombre, Cargo = self.Cargo, Mespagado = self.Mespagado, Diastrabajados = self.Diastrabajados)
        if not existe:
            if self.Cargo == 'Gerente':
                valorDia = 12000
            elif self.Cargo == 'Asesor':
                valorDia = 9000
            else:
                valorDia = 8000
            self.TotalSalario = self.Diastrabajados * valorDia
            super(Empleado, self).save(*args, **kwargs)
        else:
            return 

