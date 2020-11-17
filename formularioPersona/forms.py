from django import forms
from .models import Persona

class FormularioP(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'email',
            'tamano_empresa',
            'pais',
            'edad',
            'estudios',
            'genero',
            'ingles_hablado',
            'ingles_escrito',
            'actividad',
            'contrato',
            'cargo',
            'experiencia',
            'rentaLiquida',
            'rentaBono',
            'duracionTrabajo',
            'BeneficiosEmpleador',
            'FactoresCambioEmpleo'
        ]
    def clean_email(self):
        email_passed=self.cleaned_data.get("email")
        email_req="@"
        if not email_req in email_passed:
            raise forms.ValidationError("correo invalido, ingrese nuevamente")
        return email_passed

 
        

        nombre              = forms.CharField(max_length=50,)
        email               = forms.EmailField(max_length=50,)
        tamano_empresa      = forms.CharField()
        pais                = forms.CharField()
        edad = forms.CharField()
        estudios = forms.CharField()
        genero = forms.CharField()
        ingles_hablado = forms.CharField()
        ingles_escrito = forms.CharField()
        actividad = forms.CharField()
        contrato = forms.CharField()
        cargo = forms.CharField()
        experiencia = forms.IntegerField()
        rentaLiquida=forms.IntegerField()
        rentaBono=forms.FloatField()
        duracionTrabajo=forms.CharField()
        BeneficiosEmpleador=forms.MultipleChoiceField(default=0,blank=True)
        FactoresCambioEmpleo=forms.MultipleChoiceField(default=0,min_choices=0)





        