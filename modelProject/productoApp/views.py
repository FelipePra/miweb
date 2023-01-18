from django.shortcuts import  redirect, render
from django.http import HttpResponse

from productoApp.forms import FormMarca,FormCategoria, FormProducto, FormFiltroProduto
from personaApp.models import Producto
import xlwt

# Metodos Marca

def createmarca(request):
    form = FormMarca()
    data= {'form':form,'titulo':'Crear Marca'}
    return render(request,'create.html',data)

#Fin Metodos Marca

def createcategoria(request):
    form = FormCategoria()
    data= {'form':form,'titulo':'Crear Categoria'}
    return render(request,'create.html',data)


#Metodos Productos
def createproducto(request):
    form = FormProducto()
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listaproducto)
    data = {'form': form,'titulo':'Crear Producto'}
    return render(request,'producto/create.html',data)


def listaproducto (request):
   productos = Producto.objects.all()
   data = {'productos': productos}
   return render(request,'producto/index.html',data)


def eliminarproducto(request,id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('/listaproducto')
    
def editarproducto(request,id):
    per = Producto.objects.get(id=id)
    form = FormProducto(instance=per)
    if request.method == 'POST':
        form = FormProducto(request.POST,instance=per)
        if form.is_valid():
            form.save()
            return redirect('/listaproducto')
    data = {'form':form,'titulo':'Modificar Producto'}
    return render (request,'create.html',data)


def filtroproducto(request):
    form = FormFiltroProduto(request.POST)
    if request.method == 'POST':
        lista_productos = Producto.objects.all()
        marca = request.POST.get('marcas','')
        if marca != '':
            lista_productos = Producto.objects.filter(marca_id=marca)
        data = {'form':form,'productos':lista_productos}
        categoria = request.POST.get('categorias','')
        if categoria != '':
            lista_productos = Producto.objects.filter(categoria_id=categoria)
        data = {'form':form,'productos':lista_productos}
        return render(request,'producto/filtroproducto.html',data)
    data = {'form':form}
    return render(request,'producto/filtroproducto.html',data)
def export_excel(request,marca,cat):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=productos.xls'
    archivo = xlwt.Workbook(encoding='utf-8')
    hoja = archivo.add_sheet('Productos')
    row_num = 0
    font_style= xlwt.XFStyle()
    font_style.font.bold = True
    columnas = ['Nombre', 'Marca','Categoria','Precio','Stock','Descripcion']
    for col_num in range(len(columnas)):
        hoja.write(row_num,col_num,columnas[col_num],font_style)

    filas = Producto.objects.all().values_list('nombre','marca__nombre','categoria__nombre','precio','stock','descripcion')
    if marca != 0:
        filas = filas.filter(marca__id==marca)
    if cat != 0:
        filas = filas.filter(cat__id==cat)    
    font_style = xlwt.XFStyle()

    for fila in filas:
        row_num +=1
        for col_num in range(len(fila)):
            hoja.write(row_num,col_num,fila[col_num],font_style)
    archivo.save(response)
    return response





def eliminarvent(request,id):
    vent = Ventilacion.objects.all()
    vent.delete()
    return redirect('/todo/')

def eliminarplaca(request,id):
    plac =Motherboard.objects.all()
    plac.delete()
    return redirect('/todo/')

def eliminargraf(request,id):
    graf=Grafica.objects.all()
    graf.delete()
    return redirect('/todo/')

def eliminarfuente(request,id):
    fuente=Fuente.objects.all()
    fuente.delete()
    return redirect('/todo/')

def eliminarram(request,id):
    ram=Ram.objects.all()
    ram.delete()
    return redirect('/todo/')

def eliminaralma(request,id):
    alma=Almacenimiento.objects.all()
    alma.delete()

def eliminargab(request,id):
    gab = Gabinete.objects.all()
    gab.delete()
    return redirect('/todo/')


    path('eliminarvent/<int:id>', views.eliminarvent),
    path('eliminarplaca/<int:id>', views.eliminarplaca),
    path('eliminargraf/<int:id>', views.eliminargraf),
    path('eliminafuenter/<int:id>', views.eliminarfuente),
    path('eliminarram/<int:id>', views.eliminarram),
    path('eliminaralma/<int:id>', views.eliminaralma),
    path('eliminargab/<int:id>', views.eliminargab),