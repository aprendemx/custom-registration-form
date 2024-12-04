
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_reg_form', '0003_cambios_dos'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrainfo',
            name='nombres',
            field=models.CharField(default='', max_length=120, verbose_name='Nombre(s)'),
        )
    ]




