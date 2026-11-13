from django.db import migrations, models


class Migration(migrations.Migration):
    """
    El segundo apellido deja de ser obligatorio en el formulario de registro.

    Solo cambia `blank` (validación de Django); no altera la tabla.
    """

    dependencies = [
        ('custom_reg_form', '0006_add_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='segundo_apellido',
            field=models.CharField(blank=True, default='', max_length=120, verbose_name='Segundo Apellido'),
        ),
    ]
