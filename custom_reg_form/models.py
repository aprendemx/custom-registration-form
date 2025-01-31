from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


NIVELES=(
('0',"EDUCACIÓN PREESCOLAR"),
('1',"EDUCACIÓN PRIMARIA"),
('2',"EDUCACIÓN SECUNDARIA"),
('3',"EDUCACIÓN MEDIA SUPERIOR"),
('4',"EDUCACIÓN SUPERIOR"),
('5',"FORMACIÓN DOCENTE (ESCUELA NORMAL)"),
('6',"EDUCACIÓN ESPECIAL"),
('7',"EDUCACIÓN INDÍGENA"),
('8',"EDUCACIÓN PARA ADULTOS"),
('9',"CAPACITACIÓN PARA TRABAJO")
)

FUNCIONES = (
            ('0',"DOCENTE FRENTE A GRUPO"),
            ('1',"ADMINSTRATIVAS"),
            ('5', "SUPERVICIÓN"),
            ('6', "ASESOR TÉCNICO PEDAGÓGICO"),
            ('2',"DIRECTIVAS"),
            ('3',"TÉCNICAS"),
            ('4',"OTRAS"),

        )


ESTADOS_MX = (
    ('0', 'Seleccionar'),
    ('1', 'Aguascalientes'),
    ('2', 'Baja California'),
    ('3', 'Baja California Sur'),
    ('4', 'Campeche'),
    ('5', 'Chiapas'),
    ('6', 'Chihuahua'),
    ('7', 'Coahuila de Zaragoza'),
    ('8', 'Colima'),
    ('9', 'Ciudad de México'), 
    ('10', 'Durango'),
    ('11', 'Estado de México'),
    ('12', 'Guanajuato'),
    ('13', 'Guerrero'),
    ('14', 'Hidalgo'),
    ('15', 'Jalisco'),
    ('16', 'Michoacán de Ocampo'),
    ('17', 'Morelos'),
    ('18', 'Nayarit'),
    ('19', 'Nuevo León'),
    ('20', 'Oaxaca'),
    ('21', 'Puebla'),
    ('22', 'Querétaro'),
    ('23', 'Quintana Roo'),
    ('24', 'San Luis Potosí'),
    ('25', 'Sinaloa'),
    ('26', 'Sonora'),
    ('27', 'Tabasco'),
    ('28', 'Tamaulipas'),
    ('29', 'Tlaxcala'),
    ('30', 'Veracruz de Ignacio de la Llave'),
    ('31', 'Yucatán'),
    ('32', 'Zacatecas'),
    ('33', 'Fuera de México'),
)
OCUPACION = (
    ('1', "ESTUDIANTE"),
    ('2', "EDUCATIVO"),
    ('3', "CULTURAL"),
    ('4', "COMERCIAL"),
    ('5', "GOBIERNO"),
    ('6', "SALUD"),
    ('8', "PRODUCCIÓN AUDIOVISUAL"),
    ('7', "OTRO")

)
MAX_NIVEL_ESTUDIOS = (
    ('0', "Preescolar"),
    ('1', "Primaria"),
    ('2', "Secundaria"),
    ('3', "Preparatoria o Bachillerato"),
    ('4', "Técnica-Profesional"),
    ('5', "Licenciatura"),
    ('6', "Especialidad"),
    ('7', "Maestría"),
    ('8', "Doctorado"),
    ('9', "Ninguna educación formal")

)

class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """

    
    nombres = models.CharField(default="", max_length=220, verbose_name="Nombre(s) (*) ")
    primer_apellido = models.CharField(default="", max_length=120, verbose_name="Primer Apellido (*)")
    segundo_apellido = models.CharField(default="", max_length=120, verbose_name="Segundo Apellido")

    estado =  models.CharField(max_length=128,default='0', choices=ESTADOS_MX, verbose_name="Estado de residencia (*)")
    
        
    municipio = models.CharField( null=True, 
                                  verbose_name="Municipio o alcaldía de residencia (*)",default="",max_length=128)

    ocupacion = models.CharField(max_length=128, default='0', choices=OCUPACION,
                              verbose_name="Ocupación/Sector(*) ")


   # nivel_estudios = models.ForeignKey(NivelMaximoEducativo, null=True, on_delete=models.DO_NOTHING, blank=True,
    #                                   verbose_name="Máximo nivel de estudios")
    eres_docente = models.BooleanField(default=False, blank=True, verbose_name="¿Eres docente?")

    cct = models.CharField(default="", blank=True, max_length=11, verbose_name="Clave de tu Centro de Trabajo C.C.T.")

    funcion = models.CharField(max_length=128, default='0', choices=FUNCIONES, blank=True,
                                 verbose_name="Función")

    nivel_Educativo = models.CharField(max_length=128, default='0', choices=NIVELES, blank=True,
                               verbose_name="Nivel educativo que imparte")

    
    asignatura = models.CharField(default="", blank=True, max_length=120, verbose_name="Asignatura que imparte")
    cuentanos = models.TextField(default="", blank=True , verbose_name="Cuéntenos por que está interesado en MéxicoX")
    curp = models.CharField(max_length=20,default="", blank=True , verbose_name="Clave Única de Registro de población: CURP")
    dni = models.CharField(max_length=20,default="", blank=True , verbose_name="ID/DNI")
    maximo_nivel = models.CharField(max_length=5, default='0', choices=MAX_NIVEL_ESTUDIOS, blank=True,
                               verbose_name="Nivel educativo que imparte")
    pais = models.CharField(max_length=5, default='MX', blank=True,
                               verbose_name="País de residencia")


    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return u"ExtraInfo for user {}".format(self.user.username)







