from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404

from .forms import ProductoForm
from .models import Producto

# Create your views here.

def index(request):
    productos = Producto.objects.all().values()

    return render(
        request, 
        'productos/index.html', 
        context={'productos': productos}
    )


def producto(request, id):
    producto = Producto.objects.get(id=id)

    return render(
        request, 
        'producto.html', 
        context={'producto': producto}
    )


def detalle(request, producto_id):
    # try: 
    #     producto = Producto.objects.get(id=producto_id)
    #     return render(
    #         request, 
    #         'detalle.html', 
    #         context={'producto': producto}
    #     )
    
    # except Producto.DoesNotExist:
    #     raise Http404("El producto no existe")

# Otra forma de hacerlo
    producto = get_object_or_404(Producto, id=producto_id)
    return render(
        request, 
        'detalle.html', 
        context={'producto': producto}
    )

def nuevo(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productos')
    else:
        form = ProductoForm()

    return render(
        request, 
        'nuevo.html', 
        {'form': form}
    )
