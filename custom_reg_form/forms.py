from .models import ExtraInfo
from django.conf import settings
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """

    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)



    class Meta(object):
        model = ExtraInfo
        fields = ("nombres","primer_apellido","segundo_apellido","estado","municipio", "ocupacion","eres_docente","cct","funcion","nivel_Educativo","asignatura")
