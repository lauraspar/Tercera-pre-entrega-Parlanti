
from django.shortcuts import render
from Appcoder.models import Curso
from Appcoder.models import Alumnos
from Appcoder.models import Profesores
from django.http import HttpResponse
from django.template import loader
from Appcoder.forms import Curso_formulario
from Appcoder.forms import Alumno_formulario
from Appcoder.forms import Profesores_formulario



# Create your views here.

def inicio (request):
    return render (request, 'padre.html')

def alta_curso (request, nombre):
    curso= Curso (nombre=nombre, camada= 1212)
    curso.save() #GUARDA TODOS EN LA BASE DE DATOS
    texto= f"Se guardo en la BD {curso.nombre} {curso.camada}"
    return HttpResponse (texto)

def ver_cursos (request):
    curso=Curso.objects.all()
    dicc={"curso":curso}
    plantilla=loader.get_template("cursos.html")
    documento= plantilla.render(dicc)
    return HttpResponse(documento)

def alumnos (request):
    return render ( request, "alumnos.html")

def profesores (request):
    return render (request, "profesores.html")


def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")


def buscar_curso (request):
    return render (request, "buscar_curso.html")


def buscar (request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        curso = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"curso":curso})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    


def eliminar_curso (request, id):
    curso=Curso.objects.get (id=id)
    curso.delete()
    curso=Curso.objects.all()
    return render (request, "cursos.html", {"curso": curso})
 
def editar_curso (request, id):
    curso=Curso.objects.get(id=id)
    if request.method =="POST":
        mi_formulario=Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            curso.nombre=datos["nombre"]
            curso.camada=datos["camada"]
            curso.save()
            curso=Curso.objects.all()
            return render (request,"cursos.html",{"curso":curso})
        
    else:
        mi_formulario=Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    return render (request, "editar_curso.html", {"mi_formulario":mi_formulario,"curso":curso})


def alta_alumno (request, nombre, apellido):
    alumno= Alumnos (nombre=nombre, apellido= apellido)
    alumno.save() #GUARDA TODOS EN LA BASE DE DATOS
    texto= f"Se guardo en la BD {alumno.nombre} {alumno.apellido}"
    return HttpResponse (texto)

def ver_alumno (request):
    alumno=Alumnos.objects.all()
    dicc={"alumno":alumno}
    plantilla=loader.get_template("alumnos.html")
    documento= plantilla.render(dicc)
    return HttpResponse(documento)

def alumno_formulario(request):

    if request.method == "POST":

        mi_formulario = Alumno_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumnos = Alumnos( nombre=datos["nombre"] , apellido=datos["apellido"])
            alumnos.save()
            return render(request , "alumno_formulario.html")
        
    return render(request , "alumno_formulario.html")

def buscar_alumno (request):
    return render (request, "buscar_alumno.html")

def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumno = Alumnos.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda_alumno.html" , {"alumno":alumno})
    else:
        return HttpResponse("Ingrese el nombre del alumno")
    
def eliminar_alumno (request, id):
    alumno=Alumnos.objects.get (id=id)
    alumno.delete()

    alumno=Alumnos.objects.all()

    return render (request, "alumnos.html", {"alumno": alumno})

def editar_alumno (request, id):
    alumno=Alumnos.objects.get(id=id)
    if request.method =="POST":
        mi_formulario=Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            alumno.nombre=datos["nombre"]
            alumno.apellido=datos["apellido"]
            alumno.save()
            alumno=Alumnos.objects.all()
            return render (request,"alumnos.html",{"alumno":alumno})
        
    else:
        mi_formulario=Alumno_formulario(initial={"nombre":alumno.nombre , "apellido":alumno.apellido})
    return render (request, "editar_alumno.html", {"mi_formulario":mi_formulario,"alumno":alumno})



def alta_profesor (request, nombre,materia):
    profesor= Profesores (nombre=nombre, materia= materia)
    profesor.save() #GUARDA TODOS EN LA BASE DE DATOS
    texto= f"Se guardo en la BD {profesor.nombre} {profesor.materia}"
    return HttpResponse (texto)

def ver_profesor (request):
    profesor=Profesores.objects.all()
    dicc={"profesor":profesor}
    plantilla=loader.get_template("profesores.html")
    documento= plantilla.render(dicc)
    return HttpResponse(documento)


def profesores_formulario(request):

    if request.method == "POST":

        mi_formulario_profesores = Profesores_formulario( request.POST )

        if mi_formulario_profesores.is_valid():
            datos = mi_formulario_profesores.cleaned_data
            profesor = Profesores(nombre=datos["nombre"], materia=datos["materia"])
            profesor.save()
            return render(request , "profesores_formulario.html")
        
    return render(request , "profesores_formulario.html")

def buscar_profesores (request):
    return render (request, "buscar_profesores.html")

def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesor = Profesores.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda_profesores.html" , {"profesor":profesor})
    else:
        return HttpResponse("Ingrese el nombre del profesor")
    
def eliminar_profesor (request, id):
    profesor=Profesores.objects.get (id=id)
    profesor.delete()

    profesor=Profesores.objects.all()

    return render (request, "profesores.html", {"profesor": profesor})

def editar_profesor (request, id):
    profesor=Profesores.objects.get(id=id)
    if request.method =="POST":
        mi_formulario=Profesores_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            profesor.nombre=datos["nombre"]
            profesor.materia=datos["materia"]
            profesor.save()
            profesor=Profesores.objects.all()
            return render (request,"profesores.html",{"profesor":profesor})
        
    else:
        mi_formulario=Profesores_formulario(initial={"nombre":profesor.nombre , "materia":profesor.materia})
    return render (request, "editar_profesor.html", {"mi_formulario":mi_formulario,"profesor":profesor})