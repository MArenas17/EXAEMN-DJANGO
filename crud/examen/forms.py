from django.forms import ModelForm, TextInput,Select,NumberInput
from .models import Empleado

class EmpleadoForm(ModelForm):
    class Meta:
        model =  Empleado
        exclude = ['TotalSalario']
        Opciones = (('Gerente', 'Gerente'),('Asesor', 'Asesor'),('Vendedor', 'Vendedor'),)
        Mes = (('Enero','Enero'),('Febrero','Febrero'),('Marzo','Marzo'),('Abril','Abril'),('Mayo','Mayo'),('Junio','Junio'),('Julio','Julio'),('Agosto','Agosto'),('Septiembre','Septiembre'),('Octubre','Octubre'),('Noviembre','Noviembre'),('Diciembre','Diciembre'),)
        widgets = {
            'Nombre':TextInput(attrs={'class':'form-control'}),
            'Cargo':Select(attrs={'class':'form-control'}, choices= Opciones),
            'Diastrabajados':NumberInput(attrs={'class':'form-control'}),
            'Mespagado':Select(attrs={'class':'form-control'}, choices=Mes),
        }

        labels = {  
            'Nombre': 'Nombre del Empleado:',
            'Cargo': 'Cargo del Empleado',
            'Diastrabajados': 'Dias laborados:',
            'Mespagado': 'Mes de pago:',
        }