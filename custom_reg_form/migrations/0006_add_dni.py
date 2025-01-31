
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_reg_form', '0005_mas_cambios'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrainfo',
            name='dni',
            field=models.CharField(default='', max_length=20, verbose_name='DNI',null=True, blank=True),
        ),


    ]

