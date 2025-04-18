# Generated by Django 5.1.7 on 2025-04-07 20:56

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('AS', 'Asia'), ('AF', 'África'), ('NA', 'América del Norte'), ('SA', 'América del Sur'), ('EU', 'Europa'), ('OC', 'Oceanía'), ('AN', 'Antártida')], help_text='Código de dos letras para el continente', max_length=2, unique=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre del continente')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Continente',
                'verbose_name_plural': 'Continentes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_name', models.CharField(help_text='Nombre oficial completo del país', max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('common_name', models.CharField(help_text='Nombre común del país', max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('english_name', models.CharField(help_text='Nombre en inglés', max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('alpha_2_code', models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z]{2}$')], verbose_name='Código Alpha-2')),
                ('alpha_3_code', models.CharField(max_length=3, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z]{3}$')], verbose_name='Código Alpha-3')),
                ('numeric_code', models.CharField(max_length=3, unique=True, validators=[django.core.validators.RegexValidator('^\\d{3}$')], verbose_name='Código numérico')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('continent', models.ForeignKey(help_text='Continente al que pertenece el país', on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='api.continents')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
                'ordering': ['common_name'],
            },
        ),
        migrations.CreateModel(
            name='Types_Document',
            fields=[
                ('id_type', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='Código del tipo de documento')),
                ('name', models.CharField(help_text='Nombre del tipo de documento', max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tipo de Documento',
                'verbose_name_plural': 'Tipos de Documentos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Countries_Info',
            fields=[
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='additional_info', serialize=False, to='api.countries')),
                ('capital', models.CharField(blank=True, help_text='Capital oficial del país', max_length=100)),
                ('flag_png', models.URLField(blank=True, help_text='URL de la bandera en formato PNG', max_length=300)),
                ('flag_svg', models.URLField(blank=True, help_text='URL de la bandera en formato SVG', max_length=300)),
                ('calling_code', models.CharField(blank=True, help_text='Código telefónico internacional', max_length=10, validators=[django.core.validators.RegexValidator('^\\+\\d{1,4}$')])),
                ('timezones', models.JSONField(default=list, help_text='Zonas horarias en formato JSON')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Información del País',
                'verbose_name_plural': 'Información de los Países',
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Código ISO 3166-2', max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z]{2}-[A-Z0-9]{1,4}$')])),
                ('name', models.CharField(help_text='Nombre oficial', max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('admin_type', models.CharField(choices=[('STATE', 'Estado'), ('PROVINCE', 'Provincia'), ('REGION', 'Región'), ('DISTRICT', 'Distrito')], help_text='Tipo de división administrativa', max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='api.countries')),
            ],
            options={
                'verbose_name': 'División Administrativa',
                'verbose_name_plural': 'Divisiones Administrativas',
                'ordering': ['country', 'name'],
            },
        ),
        migrations.AddIndex(
            model_name='countries',
            index=models.Index(fields=['alpha_2_code'], name='api_countri_alpha_2_c342ac_idx'),
        ),
        migrations.AddIndex(
            model_name='countries',
            index=models.Index(fields=['common_name'], name='api_countri_common__6e9b07_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='states',
            unique_together={('country', 'code')},
        ),
    ]
