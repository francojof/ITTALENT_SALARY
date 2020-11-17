from django.contrib import admin
from formularioPersona.models import Persona
class PersonaAdmin (admin.ModelAdmin):
    list_filter=("genero","experiencia","cargo")
    list_display=("nombre","email","tamano_empresa","pais","edad","estudios","genero","ingles_hablado","ingles_escrito","actividad","contrato","cargo","experiencia","rentaLiquida","rentaBono","duracionTrabajo","BeneficiosEmpleador","FactoresCambioEmpleo")
    search_fields=("nombre","email")
    


admin.site.register(Persona,PersonaAdmin)