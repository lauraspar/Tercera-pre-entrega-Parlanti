from django import forms


class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class Alumno_formulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

class Profesores_formulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    materia = forms.CharField(max_length=30)


