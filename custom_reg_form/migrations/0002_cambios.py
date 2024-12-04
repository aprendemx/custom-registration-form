
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_reg_form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=128)),
                ('entidad', models.IntegerField(default=0)),
                ('codigo', models.CharField(default='MX', max_length=3)),
                ('clave', models.CharField(default='00', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('codigo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NivelEducativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('codigo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NivelMaximoEducativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('codigo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('codigo', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='asignatura',
            field=models.CharField(blank=True, default='', max_length=120, verbose_name='Asignatura que imparte'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='cuentanos',
            field=models.TextField(blank=True, default='', verbose_name='Cuéntenos por que está interesado en MéxicoX'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='primer_apellido',
            field=models.CharField(default='', max_length=120, verbose_name='Primer Apellido'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='segundo_apellido',
            field=models.CharField(default='', max_length=120, verbose_name='Primer Apellido'),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('codigo', models.CharField(max_length=30)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_reg_form.estado')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='custom_reg_form.estado', verbose_name='Estado de residencia'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='funcion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='custom_reg_form.funcion', verbose_name='¿Qué función desempeñas en tu institución?'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='custom_reg_form.municipio', verbose_name='Municipio de residencia'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='nivel_Educativo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='custom_reg_form.niveleducativo', verbose_name='¿A qué nivel educativo pertenece tu institución'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='nivel_estudios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='custom_reg_form.nivelmaximoeducativo', verbose_name='Máximo nivel de estudios'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='ocupacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='custom_reg_form.ocupacion', verbose_name='Ocupación'),
        ),
    ]




