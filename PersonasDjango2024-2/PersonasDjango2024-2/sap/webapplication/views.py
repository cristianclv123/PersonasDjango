from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from personas.models import Persona
#importo esta referencia cuando cree el form.py persona
from .forms import PesonaForm




# Create your views here.
def bienvenido(request):
    return HttpResponse("Hola mundo desde Django")

def despedirse(request):
    return HttpResponse("Despedida desde Django")

def contacto(request):
    return HttpResponse("Despedida desde Django")

class inicio:
    def __init__(self,variable):
        self.variable = variable


def bienvenidohtml (request):
    context  = inicio(variable=int((12 + 5)))
    personas = Persona.objects.all()
    dicMensajes={'msj1':'Valor mensaje 1','variable': context.variable , 'personas':personas}

    return render(request, 'EstudiantesTdeA.html',dicMensajes)


def despedirsehtml(request):
    return render(request, 'despedirse.html')

def contactohtml(request):
    return render(request, 'contacto.html')


#formulario registrar

def persona_list(request):
    personas=Persona.objects.all()
    return render(request, 'EstudiantesTdeA.html', {'personas': personas})


def registroexitoso(request):
    return render(request, 'registroexitoso.html')

#funcion registro
def persona_register(request):
    # Pregunto Si la solicitud es un POST, se procesa el formulario con los datos enviados.
    if request.method == 'POST':
        # Creo una instancia del formulario PesonaForm con los datos del POST (datos del formulario enviado).
        form=PesonaForm(request.POST)
        # Verifica si los datos cumplen con las reglas de validación
        if form.is_valid():
            # Guarda el formulario en la base de datos si es válido.
            form.save()
            # Redirige al usuario a la URL '/registroexitoso' después de guardar el formulario con éxito.
            return redirect('/registroexitoso')

    # Si la solicitud no es un POST (es decir, es un GET)
    else:
        #crea una instancia vacía del formulario.
        form=PesonaForm()
    # Renderiza la plantilla 'persona_register.html'
    # pasa el formulario como contexto para ser mostrado en la plantilla.
    return render(request ,'persona_register.html',{'form':form})




#funcion actualizar
def persona_update(request, pk):
    persona = get_object_or_404(Persona, pk=pk)

    if request.method == 'POST':
        form = PesonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('/registroexitoso')
    else:
        form = PesonaForm(instance=persona)

    # Agregar el objeto persona al contexto
    return render(request, 'persona_update.html', {'form': form, 'persona': persona})





def buscar_persona(request):
    if request.method == 'POST':
        id_persona = request.POST.get('id_persona')
        if id_persona:
            try:
                persona = Persona.objects.get(pk=id_persona)
                return redirect('persona_update', pk=persona.pk)
            except Persona.DoesNotExist:
                return render(request, 'buscar_persona.html', {'error': 'Persona no encontrada'})

    return render(request, 'buscar_persona.html')


# Vista para eliminar una persona
def persona_delete(request, pk):
    persona = get_object_or_404(Persona, pk=pk)

    # Si el método es POST, significa que el formulario de confirmación fue enviado.
    if request.method == 'POST':
        persona.delete()  # Elimina la persona de la base de datos.
        return redirect('/registroexitoso')  # Redirige a la página de éxito o lista de personas.

    # Si no es POST, se muestra la página de confirmación.
    return render(request, 'persona_delete.html', {'persona': persona})