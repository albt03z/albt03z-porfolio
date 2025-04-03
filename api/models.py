from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.
class Countries(models.Model):
    """
    Modelo para almacenar la informacion de los países siguiendo la norma ISO 3166
    """
    iso_code = models.CharField(
        max_length=2,
        unique=True,
        validators=[
            MaxLengthValidator(2),
            RegexValidator(
                regex=r'^[A-Z]{2}$',
                message='El código ISO debe ser de 2 letras mayúsculas'
            ),
        ],
        help_text='Código ISO 3166-1 alpha-2 del país (dos letras mayúsculas)'
    )

    iso_code3 = models.CharField(
        max_length=3,
        unique=True,
        validators=[
            MaxLengthValidator(3),
            RegexValidator(
                regex=r'^[A-Z]{3}$',
                message='El código ISO-3 debe ser de 3 letras mayúsculas'
            ),
        ],
        help_text='Código ISO 3166-1 alpha-3 del país (tres letras mayúsculas)'
    )

    numeric_code = models.CharField(
        max_length=3,
        unique=True,
        validators=[
            MaxLengthValidator(3),
            RegexValidator(
                regex=r'^\d{3}$',
                message='El código numérico debe ser de 3 dígitos'
            ),
        ],
        help_text='Código numérico ISO 3166-1 del país (tres dígitos)'
    )

    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text='Nombre oficial del país en español'
    )
    
    name_en = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text='Nombre oficial del país en inglés'
    )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países' 
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name} ({self.iso_code})"
    
class CountryInfo(models.Model):
    """
    Información adicional de un país, relacionada con el modelo Country.
    """
    country = models.OneToOneField(
        Countries,
        on_delete=models.CASCADE,
        related_name='info'
    )
    capital = models.CharField(
        max_length=100,
        blank=True,
        help_text='Capital del país'
    )
    flag_png = models.URLField(
        max_length=200,
        blank=True,
        help_text='URL de la bandera en formato PNG'
    )
    flag_svg = models.URLField(
        max_length=200,
        blank=True,
        help_text='URL de la bandera en formato SVG'
    )
    calling_code = models.CharField(
        max_length=5,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+\d{1,4}$',
                message='El código de llamada debe comenzar con + seguido de dígitos'
            ),
        ],
        help_text='Código telefónico internacional del país (ej: +34)'
    )
    
    def __str__(self):
        return f"Info de {self.country.name}"


class Region(models.Model):
    """
    Modelo para regiones o estados siguiendo la norma ISO 3166-2
    """
    country = models.ForeignKey(
        Countries,
        on_delete=models.CASCADE,
        related_name='regions',
        help_text='País al que pertenece esta región'
    )
    
    iso_code = models.CharField(
        max_length=6,
        validators=[
            MaxLengthValidator(6),
            RegexValidator(
                regex=r'^[A-Z]{2}-[A-Z0-9]{1,3}$',
                message='El código ISO debe seguir el formato XX-YYY (país-región)'
            ),
        ],
        help_text='Código ISO 3166-2 de la región (ej: ES-MD)'
    )
    
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text='Nombre oficial de la región o estado'
    )
    
    type = models.CharField(
        max_length=50,
        blank=True,
        help_text='Tipo de división administrativa (ej: Estado, Provincia, Región, etc.)'
    )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'
        ordering = ['country', 'name']
        unique_together = [['country', 'iso_code']]
        
    def __str__(self):
        return f"{self.name} ({self.iso_code})"
    
    def save(self, *args, **kwargs):
        if not self.iso_code.startswith(f"{self.country.iso_code}-"):
            self.iso_code = f"{self.country.iso_code}-{self.iso_code.split('-')[-1]}"
        super().save(*args, **kwargs)


class City(models.Model):
    """
    Modelo para ciudades
    """
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='cities',
        help_text='Región a la que pertenece esta ciudad'
    )
    
    country = models.ForeignKey(
        Countries,
        on_delete=models.CASCADE,
        related_name='cities',
        help_text='País al que pertenece esta ciudad'
    )
    
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text='Nombre oficial de la ciudad'
    )
    
    locode = models.CharField(
        max_length=5,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z0-9]{5}$',
                message='El código UN/LOCODE debe ser de 5 caracteres alfanuméricos'
            ),
        ],
        help_text='Código UN/LOCODE de la ciudad (si aplica)'
    )
    
    postal_code_format = models.CharField(
        max_length=100,
        blank=True,
        help_text='Formato del código postal (ej: NNNNN para España)'
    )
    
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        help_text='Latitud geográfica de la ciudad'
    )
    
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        help_text='Longitud geográfica de la ciudad'
    )
    
    is_capital = models.BooleanField(
        default=False,
        help_text='Indica si es la capital del país o región'
    )
    
    population = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Población estimada de la ciudad'
    )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['region', 'name']
        unique_together = [['region', 'name']]
        
    def __str__(self):
        return f"{self.name}, {self.region.name}"
    
    def save(self, *args, **kwargs):
        if self.region and self.region.country != self.country:
            self.country = self.region.country
        super().save(*args, **kwargs)