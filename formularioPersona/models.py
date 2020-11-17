from django.db import models
from multiselectfield import MultiSelectField
import datetime
class Persona(models.Model):
    SELECCIONAR = 'Seleccionar'
    # TAMANO EMPRESA ELECCIONES 
    MICRO_EMPRESA = 'Micro Empresa / Independiente'
    PEQUENA_EMPRESA = 'Pequeña Empresa'
    MEDIANA_EMPRESA = 'Mediana Empresa'
    GRAN_EMPRESA = 'Gran Empresa'
    # PAIS ELECCIONES
    CHILE='Chile'
    ARGENTINA='Argentina'
    PERU='Perú'
    COLOMBIA='Colombia'
    MEXICO='México'
    BRAZIL='Brasil'
    # RANGO DE EDAD ELECCIONES
    MENOR_IGUAL_20='Menor o igual de 20'
    ENTRE_21_25='21-25'
    ENTRE_26_30='26-30'
    ENTRE_31_35='31-35'
    ENTRE_36_40='36-40'
    ENTRE_41_45='41-45'
    ENTRE_46_50='46-50'
    MAS_50='más de 50'
    # ESTUDIOS ELECCIONES
    NINGUNO = 'Ninguno'
    BOOTCAMP = 'Bootcamp'
    TECNICO = 'Técnico'
    LICENCIATURA = 'Licenciatura'
    MASTER = 'Máster'
    DOCTORADO = 'Doctorado'
    #GENERO ELECCIONES
    HOMBRE='Hombre'
    MUJER= 'Mujer'
    #NIVEL INGLES
    INDIFERENTE='Indiferente'
    BASICO= 'Básico'
    INTERMEDIO = 'Intermedio'
    ALTO= 'Alto'
    #ACTIVIDAD O GIRO
    EMPRESA_FABRIL_INDUSTRIAL='Empresa Fabril / Industrial'
    EMPRESA_COMERCIAL = 'Empresa Comercial'
    EMPRESA_SERVICIOS = 'Empresa de Servicios'
    EMPRESA_FINANCIERA = 'Empresa Financiera'
    GOBIERNO = 'Gobierno'
    TIC = 'Tecnologías de la información y la comunicación'
    OTROS= 'Otros(educación, salud, etc)'
    #TIPO_CONTRATO
    CONTRATO_INDEFINIDO='Contrato Indefinido'
    CONTRATO_FIJO= 'Contrato Plazo Fijo'
    SIN_TRABAJO= 'Sin Trabajo'
    BOLETAS= 'Boletas'
    #CARGO
    MANAGEMENT_CIO                          = 'Management / CIO'
    MANAGEMENT_CTO                          = 'Management / CTO'
    MANAGEMENT_HEAD_OF_INFRAESTRUCTURE      = 'Management / Head of Infraestructure'
    MANAGEMENT_IT_MANAGER                   = 'Management / IT Manager'
    MANAGEMENT_PMO                          = 'Management / PMO'
    MANAGEMENT_SUBGERENTE_TI                = 'Management / Subgerente TI'
    MANAGEMENT_JEFE_INFORMATICA             = 'Management / Jefe Informática'
    DESARROLLO_GERENTE_DESARROLLO           = 'Desarrollo / Gerente Desarrollo'
    DESARROLLO_GERENTE_PROYECTOS            = 'Desarrollo / Gerente Proyectos'
    DESARROLLO_LIDER_TECNICO                = 'Desarrollo / Lider Técnico'
    DESARROLLO_ARQUITECTO_SOFTWARE          = 'Desarrollo / Arquitecto Sotware'
    DESARROLLO_ARQUITECTO_EMPRESARIAL       = 'Desarrollo / Arquitecto Empresarial'
    DESARROLLO_DESARROLLADOR_FRONT_END      = 'Desarrollo / Desarrollador Front End'
    DESARROLLO_DESARROLLADOR_BACK_END       = 'Desarrollo / Desarrollador Back End'
    DESARROLLO_FULL_STACK                   = 'Desarrollo / Full Stack'
    DESARROLLO_DESARROLLADOR_MOBILE         = 'Desarrollo / Desarrollador Mobile'
    DESARROLLO_CONSULTOR_QA                 = 'Desarrollo / Consultor QA'
    DESARROLLO_DISENADOR_UX_UI              = 'Desarrollo / Diseñador UX/UI'
    DESARROLLO_JEFE_PROYECTOS               = 'Desarrollo / Jefe de Proyectos'
    DESARROLLO_SCRUM_MASTER                 = 'Desarrollo / Scrum Master'
    DESARROLLO_AGILE_COACH                  = 'Desarrollo / Agile Coach'
    DESARROLLO_PRODUCT_OWNER                = 'Desarrollo / Product Owner'
    DESARROLLO_INGENIERO_DEVOPS             = 'Desarrollo / Ingeniero Devops'
    DESARROLLO_CONSULTOR_RPA                = 'Desarrollo / Consultor RPA'
    DATA_ANALYTICS_ARQUITECTO_DATOS         = 'Data & Analytics / Arquitecto de Datos '
    DATA_ANALYTICS_INGENIERO_DATOS          = 'Data & Analytics / Ingniero de Datos '
    DATA_ANALYTICS_MANAGER_BI               = 'Data & Analytics / Manager BI '
    DATA_ANALYTICS_CONSULTOR_BI             = 'Data & Analytics / Consultor BI'
    DATA_ANALYTICS_CHIEF_DATA_OFFICER       = 'Data & Analytics / Chief Data Officer '
    DATA_ANALYTICS_DIGITAL_ANALITICS_MANAGER= 'Data & Analytics / Digital Analitics Manager '
    DATA_ANALYTICS_DATA_SCIENTIST           = 'Data & Analytics / Data Scientist '
    SAP_ERP_PROJECT_MANAGER_SAP             = 'SAP ERP / Project Manager SAP'
    SAP_ERP_CONSULTOR_ABAP                  = 'SAP ERP / Consultor ABAP '
    SAP_ERP_CONSULTOR_FICO                  = 'SAP ERP / Consultor FICO '
    SAP_ERP_CONSULTOR_MM                    = 'SAP ERP / Consultor MM'
    SAP_ERP_CONSULTOR_SD                    = 'SAP ERP / Consultor SD '
    SAP_ERP_CONSULTOR_PIPO                  = 'SAP ERP / Consultor PIPO'
    SAP_ERP_CONSULTOR_HR                    = 'SAP ERP / Consultor HR '
    SAP_ERP_CONSULTOR_SAP_OTRO              = 'SAP ERP / Consultor SAP otro '
    CIBERSEGURIDAD_CISO                     = 'Ciberseguridad / CISO '
    CIBERSEGURIDAD_MANAGER_CIBERSEGURIDAD   = 'Ciberseguridad / Manager Ciberseguridad  '
    CIBERSEGURIDAD_ETHICAL_HACKER           = 'Ciberseguridad / Ethical Hacker  '
    CIBERSEGURIDAD_PENTESTER                = 'Ciberseguridad / Pentester '
    CIBERSEGURIDAD_ANALISTA_CIBERSEGURIDAD  = 'Ciberseguridad / Analista en Ciberseguridad  '
    CIBERSEGURIDAD_INGENIERO_CIBERSEGURIDAD = 'Ciberseguridad / Ingeniero en Ciberseguridad '
    CIBERSEGURIDAD_JEFE_PROYECTOS_CIBERSEGURIDAD= 'Ciberseguridad / Jefe Proyectos Ciberseguridad  '
    CIBERSEGURIDAD_ARQUITECTO_CIBERSEGURIDAD= 'Ciberseguridad / Arquitecto Ciberseguridad '
    INFRAESTRUCTURA_TECNICO_MONITOREO       = 'Infraestructura / Técnico en Monitoreo '
    INFRAESTRUCTURA_SOPORTE_TECNICO         = 'Infraestructura / Soporte Técnico '
    INFRAESTRUCTURA_JEFE_INFRAESTRUCTURA    = 'Infraestructura / Jefe de Infraestructura  '
    INFRAESTRUCTURA_INGENIERO_REDES         = 'Infraestructura / Ingeniero de Redes '
    INFRAESTRUCTURA_ARQUITECTO_REDES        = 'Infraestructura / Arquitecto de Redes'
    INFRAESTRUCTURA_SYSOPS                  = 'Infraestructura / SysOps '
    INFRAESTRUCTURA_ADMINISTRADOR_SISTEMAS  = 'Infraestructura / Administrador de sistemas '
    #Años de experiencia en el cargo
    MENOS_1='entre uno a once meses'
    UNO= 'un año'
    DOS= 'dos años'
    TRES='tres años'
    CUATRO='cuatro años'
    CINCO='cinco años'
    SEIS='seis años'
    SIETE='siete años'
    OCHO='ocho años'
    NUEVE='nueve años'
    MAS_DE_DIEZ='más de diez años'
    #Rentas Brutas recibidas de bono a fin de anio
    RENTA_BONO_0='0'
    RENTA_BONO_O_5='0,5'
    RENTA_BONO_1= '1'
    RENTA_BONO_1_5='1,5'
    RENTA_BONO_2= '2'
    RENTA_BONO_2_5= '2,5'
    RENTA_BONO_3_MAS= '3 o mas'
    #Duracion Actual Trabajo

    MENOS_6_MESES= 'menos de 6 meses'
    DESDE_6_A_12_MESES= '6 meses a 12 meses'
    DESDE_1_A_2_ANIOS= '1 año a 2 años'
    MAS_2_ANIOS='más de 2 años'

    #Beneficios actual empleador
    ALIMENTACION= 'Alimentación'
    MOVILIZACION= 'Movilización'
    PLAN_SALUD  = 'Plan de Salud'
    PREVISION_AFP= 'Previsión / AFP'
    CELULAR_COMPUTADOR= 'Celular / Computador'
    AUTO= 'Auto'
    PORCENTAJE_TRADING_PROFIT_ANUAL= '% Trading Profit Anual'
    GIMNASIO= 'Gimnasio'
    STOCK_OPTIONS= 'Stock Options'
    EQUITY= 'Equity'
    HORARIO_FLEXIBLE= 'Horario Flexible'
    TRABAJO_REMOTO = 'Trabajo Remoto'
    BENEFICIOS_FLEXIBLES= 'Beneficios Flexibles'
    CAPACITACIONES= 'Capacitaciones'

    #Factores a considerar para cambiar de trabajo
    BENEFICIOS_NO_MONETARIOS='Beneficios no monetarios'
    APRENDIZAJE= 'Aprendizaje'
    DESARROLLO_CARRERA= 'Desarrollo de Carrera'
    AHORRO= 'Ahorro'
    RECONOCIMIENTO= 'Reconocimiento'
    FLEXIBILIDAD_HORARIA= 'Flexibilidad Horaria'
    BONO_DE_GESTION= 'Bono de Gestión'
    TRABAJO_REMOTO= 'Trabajo Remoto'
    CLIMA_LABORAL= 'Clima Laboral'
    LEJANIA_HOGAR= 'Lejania de mi hogar'
    SUELDO= 'Sueldo'
    CAPACITACION= 'Capacitación'


    TAMANO_EMPRESA_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (MICRO_EMPRESA, 'Micro Empresa / Independiente'),
        (PEQUENA_EMPRESA, 'Pequeña Empresa'),
        (MEDIANA_EMPRESA, 'Mediana Empresa'),
        (GRAN_EMPRESA, 'Gran Empresa'),
    ]
    """ RANGO PAIS """
    PAIS_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (CHILE,'Chile'),
    ]
    """ RANGO EDAD """
    RANGO_EDAD_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (MENOR_IGUAL_20,'Menor o igual de 20'),
        (ENTRE_21_25,'21-25'),
        (ENTRE_26_30,'26-30'),
        (ENTRE_31_35,'31-35'),
        (ENTRE_36_40,'36-40'),
        (ENTRE_41_45,'41-45'),
        (ENTRE_46_50,'46-50'),
        (MAS_50,'más de 50'),
    ]
    """ RANGO ESTUDIOS """
    ESTUDIOS_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (NINGUNO ,'Ninguno'),
        (BOOTCAMP ,'Bootcamp'),
        (TECNICO ,'Técnico'),
        (LICENCIATURA ,'Licenciatura'),
        (MASTER ,'Máster'),
        (DOCTORADO ,'Doctorado'),
    ]
    """ GENERO """
    GENERO_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (HOMBRE ,'Hombre'),
        (MUJER ,'Mujer'),
    ]
    """ RANGO INGLES """
    INGLES_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (INDIFERENTE ,'Indiferente'),
        (BASICO ,'Básico'),
        (INTERMEDIO ,'Intermedio'),
        (ALTO ,'Alto'),
    ]
    """ RANGO ACTIVIDADES """
    ACTIVIDAD_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (EMPRESA_FABRIL_INDUSTRIAL,'Empresa Fabril / Industrial'),
        (EMPRESA_COMERCIAL, 'Empresa Comercial'),
        (EMPRESA_SERVICIOS,'Empresa de Servicios'),
        (EMPRESA_FINANCIERA,'Empresa Financiera'),
        (GOBIERNO,'Gobierno'),
        (TIC ,'Tecnologías de la información y la comunicación'),
        (OTROS ,'Otros(educación, salud, etc)'),
    ]
    """ RANGO CONTRATO """
    CONTRATO_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (CONTRATO_INDEFINIDO,'Contrato Indefinido'),
        (CONTRATO_FIJO,'Contrato Plazo Fijo'),
        (SIN_TRABAJO,'Sin Trabajo'),
        (BOLETAS,'Boletas'),
    ]
    """ RANGO CARGO """
    CARGO_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (MANAGEMENT_CTO                          , 'Management / CTO'),
        (MANAGEMENT_HEAD_OF_INFRAESTRUCTURE      , 'Management / Head of Infraestructure'),
        (MANAGEMENT_CIO                          , 'Management / CIO'),
        (MANAGEMENT_IT_MANAGER                   , 'Management / IT Manager'),
        (MANAGEMENT_PMO                          , 'Management / PMO'),
        (MANAGEMENT_SUBGERENTE_TI                , 'Management / Subgerente TI'),
        (MANAGEMENT_JEFE_INFORMATICA             , 'Management / Jefe Informática'),
        (DESARROLLO_GERENTE_DESARROLLO           , 'Desarrollo / Gerente Desarrollo'),
        (DESARROLLO_GERENTE_PROYECTOS            , 'Desarrollo / Gerente Proyectos'),
        (DESARROLLO_LIDER_TECNICO                , 'Desarrollo / Lider Técnico'),
        (DESARROLLO_ARQUITECTO_SOFTWARE          , 'Desarrollo / Arquitecto Sotware'),
        (DESARROLLO_ARQUITECTO_EMPRESARIAL       , 'Desarrollo / Arquitecto Empresarial'),
        (DESARROLLO_DESARROLLADOR_FRONT_END      , 'Desarrollo / Desarrollador Front End'),
        (DESARROLLO_DESARROLLADOR_BACK_END       , 'Desarrollo / Desarrollador Back End'),
        (DESARROLLO_FULL_STACK                   , 'Desarrollo / Full Stack'),
        (DESARROLLO_DESARROLLADOR_MOBILE         , 'Desarrollo / Desarrollador Mobile'),
        (DESARROLLO_CONSULTOR_QA                 , 'Desarrollo / Consultor QA'),
        (DESARROLLO_DISENADOR_UX_UI              , 'Desarrollo / Diseñador UX/UI'),
        (DESARROLLO_JEFE_PROYECTOS               , 'Desarrollo / Jefe de Proyectos'),
        (DESARROLLO_SCRUM_MASTER                 , 'Desarrollo / Scrum Master'),
        (DESARROLLO_AGILE_COACH                  , 'Desarrollo / Agile Coach'),
        (DESARROLLO_PRODUCT_OWNER                , 'Desarrollo / Product Owner'),
        (DESARROLLO_INGENIERO_DEVOPS             , 'Desarrollo / Ingeniero Devops'),
        (DESARROLLO_CONSULTOR_RPA                , 'Desarrollo / Consultor RPA'),
        (DATA_ANALYTICS_ARQUITECTO_DATOS         , 'Data & Analytics / Arquitecto de Datos '),
        (DATA_ANALYTICS_INGENIERO_DATOS          , 'Data & Analytics / Ingniero de Datos '),
        (DATA_ANALYTICS_MANAGER_BI               , 'Data & Analytics / Manager BI '),
        (DATA_ANALYTICS_CONSULTOR_BI             , 'Data & Analytics / Consultor BI'),
        (DATA_ANALYTICS_CHIEF_DATA_OFFICER       , 'Data & Analytics / Chief Data Officer '),
        (DATA_ANALYTICS_DIGITAL_ANALITICS_MANAGER, 'Data & Analytics / Digital Analitics Manager '),
        (DATA_ANALYTICS_DATA_SCIENTIST           , 'Data & Analytics / Data Scientist '),
        (SAP_ERP_PROJECT_MANAGER_SAP             , 'SAP ERP / Project Manager SAP'),
        (SAP_ERP_CONSULTOR_ABAP                  , 'SAP ERP / Consultor ABAP '),
        (SAP_ERP_CONSULTOR_FICO                  , 'SAP ERP / Consultor FICO '),
        (SAP_ERP_CONSULTOR_MM                    , 'SAP ERP / Consultor MM'),
        (SAP_ERP_CONSULTOR_SD                    , 'SAP ERP / Consultor SD '),
        (SAP_ERP_CONSULTOR_PIPO                  , 'SAP ERP / Consultor PIPO'),
        (SAP_ERP_CONSULTOR_HR                    , 'SAP ERP / Consultor HR '),
        (SAP_ERP_CONSULTOR_SAP_OTRO              , 'SAP ERP / Consultor SAP otro '),
        (CIBERSEGURIDAD_CISO                     , 'Ciberseguridad / CISO '),
        (CIBERSEGURIDAD_MANAGER_CIBERSEGURIDAD   , 'Ciberseguridad / Manager Ciberseguridad  '),
        (CIBERSEGURIDAD_ETHICAL_HACKER           , 'Ciberseguridad / Ethical Hacker  '),
        (CIBERSEGURIDAD_PENTESTER                , 'Ciberseguridad / Pentester '),
        (CIBERSEGURIDAD_ANALISTA_CIBERSEGURIDAD  , 'Ciberseguridad / Analista en Ciberseguridad  '),
        (CIBERSEGURIDAD_INGENIERO_CIBERSEGURIDAD , 'Ciberseguridad / Ingeniero en Ciberseguridad '),
        (CIBERSEGURIDAD_JEFE_PROYECTOS_CIBERSEGURIDAD, 'Ciberseguridad / Jefe Proyectos Ciberseguridad  '),
        (CIBERSEGURIDAD_ARQUITECTO_CIBERSEGURIDAD, 'Ciberseguridad / Arquitecto Ciberseguridad '),
        (INFRAESTRUCTURA_TECNICO_MONITOREO       , 'Infraestructura / Técnico en Monitoreo '),
        (INFRAESTRUCTURA_SOPORTE_TECNICO         , 'Infraestructura / Soporte Técnico '),
        (INFRAESTRUCTURA_JEFE_INFRAESTRUCTURA    , 'Infraestructura / Jefe de Infraestructura  '),
        (INFRAESTRUCTURA_INGENIERO_REDES         , 'Infraestructura / Ingeniero de Redes '),
        (INFRAESTRUCTURA_ARQUITECTO_REDES        , 'Infraestructura / Arquitecto de Redes'),
        (INFRAESTRUCTURA_SYSOPS                  , 'Infraestructura / SysOps '),
        (INFRAESTRUCTURA_ADMINISTRADOR_SISTEMAS  , 'Infraestructura / Administrador de sistemas '),
    ]
    """ EXPERIENCIA RANGO """
    EXPERIENCIA_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (0,'entre uno a once meses'),
        (2, 'un año'),
        (2, 'dos años'),
        (3,'tres años'),
        (4,'cuatro años'),
        (5,'cinco años'),
        (6,'seis años'),
        (7,'siete años'),
        (8,'ocho años'),
        (9,'nueve años'),
        (10,'más de diez años'),
    ]
    RENTA_BRUTA_BONO_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (0,'0'),
        (0.5,'0.5'),
        (1, '1'),
        (1.5,'1.5'),
        (2, '2'),
        (2.5, '2.5'),
        (3, '3 o mas'),
    ]
    DURACION_TRABAJO_CHOICES = [
        (SELECCIONAR ,'Seleccionar'),
        (MENOS_6_MESES, 'menos de 6 meses'),
        (DESDE_6_A_12_MESES, '6 meses a 12 meses'),
        (DESDE_1_A_2_ANIOS, '1 año a 2 años'),
        (MAS_2_ANIOS,'más de 2 años'),
        
    ]
    BENEFICIOS_CHOICES=(
        (ALIMENTACION, 'Alimentación'),
        (MOVILIZACION, 'Movilización'),
        (PLAN_SALUD  , 'Plan de Salud'),
        (PREVISION_AFP, 'Previsión / AFP'),
        (CELULAR_COMPUTADOR, 'Celular / Computador'),
        (AUTO, 'Auto'),
        (PORCENTAJE_TRADING_PROFIT_ANUAL, '% Trading Profit Anual'),
        (GIMNASIO, 'Gimnasio'),
        (STOCK_OPTIONS, 'Stock Options'),
        (EQUITY, 'Equity'),
        (HORARIO_FLEXIBLE, 'Horario Flexible'),
        (TRABAJO_REMOTO , 'Trabajo Remoto'),
        (BENEFICIOS_FLEXIBLES, 'Beneficios Flexibles'),
        (CAPACITACIONES, 'Capacitaciones'),
    )

    FACTORES_CAMBIO_CHOICES = [
        (BENEFICIOS_NO_MONETARIOS,'Beneficios no monetarios'),
        (APRENDIZAJE, 'Aprendizaje'),
        (DESARROLLO_CARRERA, 'Desarrollo de Carrera'),
        (AHORRO, 'Ahorro'),
        (RECONOCIMIENTO, 'Reconocimiento'),
        (FLEXIBILIDAD_HORARIA, 'Flexibilidad Horaria'),
        (BONO_DE_GESTION, 'Bono de Gestión'),
        (TRABAJO_REMOTO, 'Trabajo Remoto'),
        (CLIMA_LABORAL, 'Clima Laboral'),
        (LEJANIA_HOGAR, 'Lejania de mi hogar'),
        (SUELDO, 'Sueldo'),
        (CAPACITACION, 'Capacitación'),
        
    ]


    #campos a completar
    nombre=models.CharField(max_length=50,null=False)
    email=models.EmailField(null=False)
    #EMAIL UNIQUE, pero no muestra en pantalla la alerta en caso de que exista en la bbdd , unique=True
    tamano_empresa = models.CharField(
        max_length=30,
        choices=TAMANO_EMPRESA_CHOICES,
        default=SELECCIONAR,
    )
    pais = models.CharField(
        max_length=15,
        choices=PAIS_CHOICES,
        default=SELECCIONAR,
    )
    edad = models.CharField(
        max_length=25,
        choices=RANGO_EDAD_CHOICES,
        default=SELECCIONAR,
    )
    estudios = models.CharField(
        max_length=15,
        choices=ESTUDIOS_CHOICES,
        default=SELECCIONAR,
    )
    genero = models.CharField(
        max_length=11,
        choices=GENERO_CHOICES,
        default=SELECCIONAR,
    )
    ingles_hablado = models.CharField(
        max_length=15,
        choices=INGLES_CHOICES,
        default=SELECCIONAR,
    )
    ingles_escrito = models.CharField(
        max_length=15,
        choices=INGLES_CHOICES,
        default=SELECCIONAR,
    )
    actividad = models.CharField(
        max_length=50,
        choices=ACTIVIDAD_CHOICES,
        default=SELECCIONAR,
    )
    contrato = models.CharField(
        max_length=30,
        choices=CONTRATO_CHOICES,
        default=SELECCIONAR
    )
    cargo = models.CharField(
        max_length=100,
        choices=CARGO_CHOICES,
        default=SELECCIONAR,
    )
    experiencia = models.IntegerField(
        choices=EXPERIENCIA_CHOICES,
        default=SELECCIONAR,
    )
    rentaLiquida=models.IntegerField(default=0)
    rentaBono=models.FloatField(
        choices=RENTA_BRUTA_BONO_CHOICES,
        default=SELECCIONAR,
    )
    duracionTrabajo=models.CharField(
        max_length=50,
        choices=DURACION_TRABAJO_CHOICES,
        default=SELECCIONAR,
    )
    BeneficiosEmpleador=MultiSelectField(choices=BENEFICIOS_CHOICES,
                                 blank=True,max_choices=14,default=0,
                                 )
    FactoresCambioEmpleo=MultiSelectField(choices=FACTORES_CAMBIO_CHOICES,
                                 blank=True,max_choices=12,default=0,
                                 )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
                return self.nombre
    objects = models.Manager()



    

   



