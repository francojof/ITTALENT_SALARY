from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpRequest
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string   
from formularioPersona.models import Persona
from .forms import FormularioP
from django.conf import settings
import threading
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.views.generic import  View
import os
from django.template import context
import smtplib
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from io import BytesIO
from django.http import JsonResponse
from django import forms
from django.contrib import messages
from datetime import datetime
from django.utils import formats
import re

def index(request):
    form = FormularioP()
    if request.method == 'POST':
        try:
            form=FormularioP(request.POST)
            date_joined = datetime.now()
            formatted_datetime = formats.date_format(date_joined, "SHORT_DATETIME_FORMAT")
            nombre= request.POST.get('nombre')
            email = request.POST.get('email')
            tamano_empresa = request.POST.get('tamano_empresa')
            pais = request.POST.get('pais')
            edad = request.POST.get('edad')
            estudios = request.POST.get('estudios')
            genero = request.POST.get('genero')
            ingles_hablado = request.POST.get('ingles_hablado')
            ingles_escrito = request.POST.get('ingles_escrito')
            actividad = request.POST.get('actividad') 
            contrato = request.POST.get('contrato') 
            cargo = request.POST.get('cargo')
            experiencia = request.POST.get('experiencia')
            rentaLiquida = request.POST.get('rentaLiquida')
            rentaBono = request.POST.get('rentaBono')
            duracionTrabajo = request.POST.get('duracionTrabajo')
            BeneficiosEmpleador = request.POST.get('BeneficiosEmpleador')
            FactoresCambioEmpleo = request.POST.get('FactoresCambioEmpleo')
            template= get_template('correo.html')
            
            if(nombre==""):
                messages.error(request, 'Debe ingresar un nombre')
                context= {'form':form}
                return render(request,'formulario.html',context)
            if(email==""):
                messages.error(request, 'Debe ingresar un email')
                context= {'form':form}
                return render(request,'formulario.html',context)
            if(es_correo_valido(email)==False):
                messages.error(request, 'Correo invalido')
                context= {'form':form}
                return render(request,'formulario.html',context)
            if(validar_nombre(nombre)==False):
                messages.error(request, 'Nombre invalido')
                context= {'form':form}
                return render(request,'formulario.html',context)
            if(len(nombre)>60):
                messages.error(request, 'El nombre ingresado es muy largo ')
                context= {'form':form}
                return render(request,'formulario.html',context)
            if(len(email)>100):
                messages.error(request, 'El email ingresado es muy largo ')
                context= {'form':form}
                return render(request,'formulario.html',context)
            if(tamano_empresa=='Seleccionar'or pais=='Seleccionar'or edad=='Seleccionar' or estudios=='Seleccionar' or 
                    genero=='Seleccionar' or ingles_hablado=='Seleccionar' or ingles_escrito=='Seleccionar' or actividad=='Seleccionar' or
                    contrato=='Seleccionar' or cargo=='Seleccionar' or experiencia=='Seleccionar' or rentaBono=='Seleccionar' or 
                    duracionTrabajo=='Seleccionar'):
                        messages.error(request, 'Completa todos los campos antes de enviar')
                        
                        context= {'form':form}
                        return render(request,'formulario.html',context)
            if Persona.objects.filter(email=request.POST['email']).exists():
                messages.error(request, 'El correo que ingresaste ya está registrado')
                context= {'form':form}
                return render(request,'formulario.html',context)
            if (rentaLiquida<0):
                messages.error(request, 'Renta ingresada invalida')
                context= {'form':form}
                return render(request,'formulario.html',context)

        except :
            messages.error(request, 'Error inesperado, intente mas tarde')
            context= {'form':form}
            return render(request,'formulario.html',context)

        if form.is_valid():
            try:
                context1 = {
                    'nombre': nombre,
                    'email' : email,
                    'tamano_empresa' : tamano_empresa,
                    'pais' : pais,
                    'edad' : edad,
                    'estudios' : estudios,
                    'genero' : genero,
                    'ingles_hablado' : ingles_hablado,
                    'ingles_escrito': ingles_escrito,
                    'actividad' : actividad,
                    'contrato' : contrato,
                    'cargo' : cargo,
                    'experiencia' : experiencia,
                    'rentaLiquida' : rentaLiquida,
                    'rentaBono' : rentaBono,
                    'duracionTrabajo' : duracionTrabajo,
                    'BeneficiosEmpleador' : BeneficiosEmpleador,
                    'FactoresCambioEmpleo' : FactoresCambioEmpleo,   
                    'fecha': formatted_datetime,
                }
                
                content = template.render(context1)
                objEmail = EmailMultiAlternatives(
                'Informe Estudio de Renta',
                '',
                settings.EMAIL_HOST_USER,
                [email]
                )      
                
                objEmail.attach_alternative(content , 'text/html')
                objEmail.send()
                form.save()
                
                messages.success(request, 'Gracias por participar en nuestro Estudio de renta, revisa tu correo.')
                form=FormularioP()
                return render(request,'formulario.html',context)  
            except:  
                context= {'form':form}   
                return render(request,'formulario.html',context)
            return render(request,'formulario.html')
    context= {'form':form}
    return render(request,'formulario.html',context)
def es_correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None
def validar_nombre(nombre):
    expresion =r"^([a-zA-Z ñÑ])+$"
    return re.match(expresion, nombre) is not None