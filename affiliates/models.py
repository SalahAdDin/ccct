from django.db import models

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.models import Image

from smart_selects.db_fields import ChainedForeignKey

from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel, MultiFieldPanel)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

# Create your models here.

#Values for Choice Fields
AFFILIATION_PERSON_TYPE = (
    ('natural', "Persona Natural"),
    ('legal', "Persona Jurídica"),
)

ECONOMIC_ACTIVITY = (
    ('maker', "Fabricante"),
    ('trading', "Comercializadora"),
    ('exporter', "Exportador"),
    ('consulting', "Consultoría"),
    ('importer', "Importador"),
    ('services', "Servicios"),
)

INTEREST_AREAS = (
    ('opportunities', "Oportunidades comerciales y de inversión"),
    ('databases', "Acceso a Base de Datos"),
    ('misions', "Misiones Empresariales"),
    ('seminars', "Asistencia a seminarios y/o capacitaciones"),
    ('consulting', "Asesorías comerciales"),
    ('directories', "Directorios Empresariales"),
    ('other', "Otros"),
)

#Model
class Person(models.Model):
    name = models.CharField(max_length=20, help_text="Tipo de Persona que se inscribe", verbose_name="Nombre del Tipo")

    class Meta:
        verbose_name = "Tipo de Persona"

    def __str__(self):
        return self.name

class MemberShip(models.Model):
    title = models.CharField(max_length=255, help_text="Nombre del tipo de afiliación.",verbose_name="Título")
    #type_person = models.CharField(max_length=255, choices=AFFILIATION_PERSON_TYPE, verbose_name='Tipo de Persona',)
    type_person = models.ForeignKey(Person, verbose_name="Tipo de Persona", related_name="membership")
    descript = models.CharField(max_length=500, help_text="Descripción del tipo de afiliación.", verbose_name="Descripción")
    value = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cuota', help_text="Cuota de afiliación.")

    class Meta:
        #description = 'Modelo Membresía'
        verbose_name = "Membresía"

    def __str__(self):
        return self.title

#Afiliados
class Affiliates(models.Model):
    #type_person = models.CharField(max_length=255, choices=AFFILIATION_PERSON_TYPE)
    name = models.CharField("Nombre Solicitante", max_length=255, )
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='logo',
    )
    dni = models.IntegerField("Documento de Identificación", max_length=12, help_text="Para NIT omitir la '-'. ")
    adress = models.CharField("Dirección", max_length=255, )
    country = models.CharField("País", max_length=255, )
    city = models.CharField("Ciudad", max_length=255, )
    tel = models.IntegerField("Teléfono", max_length=10,)
    e_mail = models.EmailField("Correo Electrónico")
    web = models.URLField("Sitio Web", max_length=255, null=True, blank=True, )
    fax = models.IntegerField(max_length=7, null=True, blank=True,)
    attorney_name = models.CharField("Representante Legal", max_length=255, )
    position = models.CharField("Cargo", max_length=255, )
    staff = models.IntegerField("Número de Empleados", max_length=4, null=True, blank=True,)
    interest = models.CharField("Interéses de Afiliación", choices=INTEREST_AREAS, max_length=255, )
    cause = models.CharField("Razón Social", max_length=255, )
    economic_sector = models.CharField("Sector Económico", max_length=255, )
    economic_activity = models.CharField("Actividad Económica", choices=ECONOMIC_ACTIVITY, max_length=255, null=True, blank=True, )
    other_interes = models.CharField("Otro", max_length=255,blank=True, null=True, )

    class Meta:
        #description = 'Modelo Afiliado.'
        verbose_name = "Afiliado"

    def __str__(self):
        return self.name

#Afiliacion
class Affilliation(models.Model):
    person = models.ForeignKey(Person, verbose_name="Tipo de Persona", related_name="person")
    affiliation = ChainedForeignKey(
        MemberShip,
        chained_field="person",
        chained_model_field="type_person",
        show_all=False,
        auto_choose=True,
        verbose_name='Membresía',
        #related_name='affiliation'
    )
    affiliates = models.ForeignKey(Affiliates,  verbose_name="Afiliado", related_name="affiliate")
    date_prein = models.DateField("Fecha de Inscripción", auto_now_add=True,)
    date_in = models.DateField("Fecha de Aceptación",blank=True, null=True,)
    is_active = models.BooleanField(verbose_name='Activo', help_text="Está activo?", default=False, )

    class Meta:
         #description = "Modelo Afiliacion."
        verbose_name = "Afiliación"
        verbose_name_plural = 'Afiliaciones'

    def __str__(self):
        return '%s, %s' % (self.affiliation, self.affiliates)

#Auditorias
class AuditHistory(models.Model):
    affiliates = models.ForeignKey(Affiliates,  verbose_name="Afiliado", related_name="member")
    affiliation = models.ForeignKey(Affilliation, verbose_name="Afiliación", related_name="membership")
    date_in = models.DateField("Fecha de Aceptación", auto_now_add=True,)
    date_out = models.DateField(verbose_name='Fecha de Expiración', null=True, blank=True, )
    notes = models.TextField(verbose_name='Anotaciones', )

    class Meta:
         #description = "Modelo Afiliacion."
        verbose_name = "Historial de Afiliación"
        verbose_name_plural = 'Historiales de Afiliaciones'

    def __str__(self):
        return '%s, %s, %s' % (self.affiliation, self.affiliates, self.date_in)
