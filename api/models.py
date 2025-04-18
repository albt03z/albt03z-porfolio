from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

class Continents(models.Model):
    CONTINENT_CHOICES = [
        ('AS', 'Asia'),
        ('AF', 'África'),
        ('NA', 'América del Norte'),
        ('SA', 'América del Sur'),
        ('EU', 'Europa'),
        ('OC', 'Oceanía'),
        ('AN', 'Antártida')
    ]
    
    code = models.CharField(
        max_length=2,
        choices=CONTINENT_CHOICES,
        unique=True,
        help_text='Código de dos letras para el continente'
    )
    name = models.CharField(
        max_length=100, 
        unique=True,
        verbose_name='Nombre del continente'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Continente'
        verbose_name_plural = 'Continentes' 
        ordering = ['name']
        
    def __str__(self):
        return self.name

class Countries(models.Model):
    continent = models.ForeignKey(
        Continents,
        on_delete=models.CASCADE,
        related_name='countries',
        help_text='Continente al que pertenece el país'
    )
    official_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text='Nombre oficial completo del país'
    )
    common_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text='Nombre común del país'
    )
    english_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text='Nombre en inglés'
    )
    alpha_2_code = models.CharField(
        max_length=2, 
        unique=True, 
        validators=[RegexValidator(r'^[A-Z]{2}$')],
        verbose_name='Código Alpha-2'
    )
    alpha_3_code = models.CharField(
        max_length=3, 
        unique=True, 
        validators=[RegexValidator(r'^[A-Z]{3}$')],
        verbose_name='Código Alpha-3'
    )
    numeric_code = models.CharField(
        max_length=3, 
        unique=True, 
        validators=[RegexValidator(r'^\d{3}$')],
        verbose_name='Código numérico'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países' 
        ordering = ['common_name']
        indexes = [
            models.Index(fields=['alpha_2_code']),
            models.Index(fields=['common_name']),
        ]
        
    def __str__(self):
        return f"{self.common_name} ({self.alpha_2_code})"
    
class Countries_Info(models.Model):
    country = models.OneToOneField(
        Countries,
        on_delete=models.CASCADE,
        related_name='additional_info',
        primary_key=True
    )
    capital = models.CharField(
        max_length=100,
        blank=True,
        help_text='Capital oficial del país'
    )
    flag_png = models.URLField(
        max_length=300,
        blank=True,
        help_text='URL de la bandera en formato PNG'
    )
    flag_svg = models.URLField(
        max_length=300,
        blank=True,
        help_text='URL de la bandera en formato SVG'
    )
    calling_code = models.CharField(
        max_length=10,
        blank=True,
        validators=[RegexValidator(r'^\+\d{1,4}$')],
        help_text='Código telefónico internacional'
    )
    timezones = models.JSONField(
        default=list,
        help_text='Zonas horarias en formato JSON'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Información del País'
        verbose_name_plural = 'Información de los Países'
        
    def __str__(self):
        return f"Info de {self.country.common_name}"

class States(models.Model):
    ADMIN_TYPES = [
        ('STATE', 'Estado'),
        ('PROVINCE', 'Provincia'),
        ('REGION', 'Región'),
        ('DISTRICT', 'Distrito')
    ]
    
    country = models.ForeignKey(
        Countries,
        on_delete=models.CASCADE,
        related_name='states'
    )
    code = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^[A-Z]{2}-[A-Z0-9]{1,4}$')],
        help_text='Código ISO 3166-2'
    )
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text='Nombre oficial'
    )
    admin_type = models.CharField(
        max_length=50,
        choices=ADMIN_TYPES,
        help_text='Tipo de división administrativa'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'División Administrativa'
        verbose_name_plural = 'Divisiones Administrativas'
        unique_together = [['country', 'code']]
        ordering = ['country', 'name']

    def __str__(self):
        return f"{self.name}, {self.country.alpha_2_code}"

    def save(self, *args, **kwargs):
        if not self.code.startswith(f"{self.country.alpha_2_code}-"):
            self.code = f"{self.country.alpha_2_code}-{self.code.split('-')[-1]}"
        super().save(*args, **kwargs)


class Types_Document(models.Model):
    id_type = models.CharField(verbose_name = 'Código del tipo de documento', max_length=2, primary_key=True)
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text='Nombre del tipo de documento'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'
        ordering = ['name']

    def __str__(self):
        return self.name