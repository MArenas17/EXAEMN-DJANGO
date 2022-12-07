from django.shortcuts import render,redirect
from .forms import EmpleadoForm
from.models import Empleado


# def crearEmpleado(request):
#     if request.method == 'POST':
#         form = EmpleadoForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('crearEmpleado')
#         else:
#             return redirect('crearEmpleado')
#     else:
#         form = EmpleadoForm()
#     return render (request,'crearEmpleado.html',{'form':form})
def crearEmpleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid:
            form.save()
    form = EmpleadoForm
    context = {'form': form }
    return render(request,'crearEmpleado.html',context)


def verEmpleado(request):
    empleado = Empleado.objects.all()
    return render(request,'verEmpleado.html',{'empleado':empleado})

def actualizarEmpleado(request, id):
    empleado = Empleado .objects.get(id = id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance = empleado)
        if form.is_valid:
            form.save()
        return redirect('verEmpleado')
    else:
        form = EmpleadoForm(instance = empleado)
    context = {
        'form':form,
        'id': id}
    return render(request,'crearEmpleado.html',context)

def eliminarEmpleado(request,id):
    empleado = Empleado.objects.get(id = id)
    empleado.delete()
    return redirect('verEmpleado')