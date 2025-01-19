
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_reg_form', '0004_cambios'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrainfo',
            name='curp',
            field=models.CharField(default='', max_length=20, verbose_name='CURP',null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='maximo_nivel',
            field=models.CharField(default='', max_length=5, verbose_name='Máximo nivel de estudios',null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='pais',
            field=models.CharField(default='', max_length=5, verbose_name='País',null=True, blank=True),
        ),


    ]

