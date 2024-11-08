from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from .models import Monografia, Estudiante, Profesor, Rol, ProfesorMonografia
import sweetify

# Create your views here.
def index(request):
    if request.htmx:
        if request.method == "GET":
            index_url = reverse('index') 
            monos = Monografia.objects.all()
            return render(request, "partials/table-mono.html", {'monos': monos,  'index_url': index_url})

    monos = Monografia.objects.all()
    index_url = reverse('index') 
    addEstuUrl = reverse('addEstu') 
    return render(request, 'Register/layout.html', {'monos': monos, 'index_url': index_url})

def registerMono(request):
    if request.method == "POST":
        try:
            titulo = request.POST.get('titulo')
            fecha_defensa = request.POST.get('fecha_defensa')
            nota_defensa = request.POST.get('nota_defensa')
            tiempo_otorgado = request.POST.get('tiempo_otorgado')
            tiempo_defensa = request.POST.get('tiempo_defensa')
            tiempo_pregunta = request.POST.get('tiempo_pregunta')
                    
            Monografia.objects.create(
                titulo = titulo,
                fecha_defensa = fecha_defensa,
                nota_defensa = nota_defensa,
                tiempo_otorgado = tiempo_otorgado,
                tiempo_defensa = tiempo_defensa,
                tiempo_pregunta = tiempo_pregunta
            )
        
            return JsonResponse({'status': 'success', 'message': 'Monografía registrada exitosamente'}, status=200)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Error al registrar la Monografía'}, status=500)
        
    elif request.method == 'GET' and request.htmx:
        return render(request, "partials/register-mono.html")
    return render(request,'Register/layout.html')

def registerEstu(request):
    if request.method == "POST":
        try:
            estuData = request.POST
            nombres = estuData.get('nombres')
            apellidos = estuData.get('apellidos')
            direccion = estuData.get('direccion')
            telefono = estuData.get('telefono')
            fecha_nacimiento = estuData.get('fecha_nacimiento')
            
            Estudiante.objects.create(
                nombres=nombres,
                apellidos=apellidos,
                direccion=direccion,
                telefono=telefono,
                fecha_nacimiento=fecha_nacimiento
            )
            
            return JsonResponse({'status': 'success', 'message': 'Estudiante registrado exitosamente'}, status=200)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Error al registrar el estudiante'}, status=500)

    elif request.method == "GET" and request.htmx:
        return render(request, "partials/register-estu.html")
    
    return render(request, 'Register/layout.html')


def registerProf(request):
    if request.method == "POST":
        try:
            estuData = request.POST
            nombres = estuData.get('nombres')
            apellidos = estuData.get('apellidos')
            direccion = estuData.get('direccion')
            telefono = estuData.get('telefono')
            fecha_nacimiento = estuData.get('fecha_nacimiento')
            
            Profesor.objects.create(
                nombres=nombres,
                apellidos=apellidos,
                direccion=direccion,
                telefono=telefono,
                fecha_nacimiento=fecha_nacimiento
            )
            
            return JsonResponse({'status': 'success', 'message': 'Profesor registrado exitosamente'}, status=200)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Error al registrar el Profesor'}, status=500)

    elif request.method == "GET" and request.htmx:
        print('get')
        return render(request, "partials/register-profe.html")
    return render(request,'Register/layout.html')
    
def addEstu(request):
        addEstuUrl = reverse('addEstu') 
        if request.htmx:
            if request.method == "POST":
                print('post')
                return render(request, "partials/add-estu.html", {'addEstuUrl': addEstuUrl})
            elif request.method == "GET":
                monos = Monografia.objects.all()
                students = Estudiante.objects.all()
                return render(request, "partials/add-estu.html",{'students': students, 'monos': monos, 'addEstuUrl': addEstuUrl})
        return render(request,'Register/layout.html', {'addEstuUrl': addEstuUrl})
    
def addTutor(request):
        addProfUrl = reverse('addTutor')
        if request.htmx:
            if request.method == "POST":
                return render(request, "partials/add-tutor.html", {'addProfUrl': addProfUrl})
            elif request.method == "GET":
                profesores = Profesor.objects.all()
                return render(request, "partials/add-tutor.html",{'profesores': profesores, 'addProfUrl': addProfUrl})
        return render(request,'Register/layout.html')
    
def addJudges(request):
        addProfUrl = reverse('addJudges')
        if request.htmx:
            if request.method == "POST":
                return render(request, "partials/add-judges.html", {'addProfUrl': addProfUrl})
            elif request.method == "GET":
                profesores = Profesor.objects.all()
                return render(request, "partials/add-judges.html",{'profesores': profesores, 'addProfUrl': addProfUrl})
        return render(request,'Register/layout.html')
    
    
def deleteMono(request, id):
    if request.method == "POST":
        print('POST request received')
        try:
            monografia = Monografia.objects.get(id=id) 
            monografia.delete() 
            return JsonResponse({'status': 'success', 'message': 'Monografía borrada exitosamente'}, status=200)
            
        except Monografia.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Monografía no encontrada'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error al eliminar Monografía: {str(e)}'}, status=500) 

def deleteProf(request, id):
    if request.method == "POST":
        try:
            profesor = Profesor.objects.get(id=id)
            profesor.delete()
            return JsonResponse({'status': 'success', 'message': 'Profesor borrado exitosamente'}, status=200)   
        except Profesor.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Profesor no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error al eliminar profesor: {str(e)}'}, status=500)

def deleteEstu(request, id):
    if request.method == "POST":
        try:
            estudiante = Estudiante.objects.get(id=id)
            estudiante.delete()
            return JsonResponse({'status': 'success', 'message': 'Estudiante borrado exitosamente'}, status=200)   
        except Estudiante.DoesNotExist: 
            return JsonResponse({'status': 'error', 'message': 'Estudiante no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error al eliminar estudiante: {str(e)}'}, status=500)
 