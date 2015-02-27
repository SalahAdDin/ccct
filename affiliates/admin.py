from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from .models import *
from import_export.admin import ImportExportModelAdmin
from datetime import datetime, timedelta

import wagtail.wagtailimages.admin

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_editable = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Person, PersonAdmin)

class MemberShipAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_person', 'descript', 'value', )
    list_editable = ('title', 'descript', 'value', )
    list_filter = ('title', 'descript', 'value', )
    search_fields = ('title', 'value',)

admin.site.register(MemberShip, MemberShipAdmin)

class AffilliationInline(admin.StackedInline):
    fieldsets = [
        (None, {
            'fields': ['person', 'affiliation', 'is_active'],
        }),
        (None, {
            'fields': ['date_in', ],
        }),
    ]
    model = Affilliation
    suit_classes = 'suit-tab suit-tab-affilliation'

class AffiliatesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Afiliado', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['name', 'logo', 'dni', 'attorney_name', 'position'],
        }),
        ('Ubicación', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['adress', 'country', 'city', 'tel', 'fax', 'e_mail', 'web'],
        }),
        ('Información Económica', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['staff', 'interest', 'cause', 'economic_sector', 'economic_activity', 'other_interes'],
        })
    ]

    inlines = [AffilliationInline,]
    list_display = ('name', 'logo', 'dni', 'adress', 'tel', 'attorney_name', 'economic_sector', 'economic_activity',)
    list_filter = ('name', 'dni', 'country', 'city', 'staff', 'interest', 'economic_sector', 'economic_activity',)
    list_editable = ('name', 'dni', 'tel', 'attorney_name', 'economic_sector', 'economic_activity',)
    search_fields = ('name', 'dni', 'country', 'city', 'staff', 'cause', 'interest', 'economic_sector', 'economic_activity',)
    suit_form_tabs = (('general', 'General'), ('affilliation', 'Afiliación'))

admin.site.register(Affiliates, AffiliatesAdmin)

class AuditHistoryInline(admin.TabularInline):
    model = AuditHistory
    suit_classes = 'suit-tab suit-tab-audit'

class AffilliationAdmin(admin.ModelAdmin):
    actions = ['make_active', 'make_deactive',]
    fieldsets = [
        ('Afiliación', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['person', 'affiliation', 'affiliates', 'is_active'],
        }),
        ('Fechas', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['date_in', ],
        }),
    ]
    inlines = [AuditHistoryInline, ]
    list_display = ('affiliation', 'affiliates', 'is_active', 'date_prein', 'date_in', 'date_end', )
    list_filter = ('affiliation', 'affiliates', 'is_active')
    list_editable = ('affiliation',)
    search_fields = ('affiliation', 'affiliates', 'is_active', 'date_in',)

    suit_form_tabs = (('general', 'General'), ('audit', 'Historial'))

    def date_end(self, obj):
        if obj.date_in:
            return obj.date_in + timedelta(days=365)

    date_end.short_description = "Fecha de Expiración"
    date_end.allow_tags = True

    #Actions
    def make_active(self, request, queryset):
        rows_activated = queryset.update(is_active=True)
        queryset.update(date_in=datetime.now())
        for obj in queryset:
            #a = ContentType.objects.get_for_model(queryset.model)
            ah = AuditHistory.objects.create(affiliates=obj.affiliates, affiliation=obj, date_in=datetime.now(), date_out=obj.date_in + timedelta(days=365), )
            ah.save()
        if rows_activated == 1:
            message_bit = "1 afiliación fue"
        else:
            message_bit = "%s afiliaciones fueron" % rows_activated
        self.message_user(request, "%s exitosamente activada(s)." % message_bit)

    make_active.short_description = "Activar afiliación"

    def make_deactive(self, request, queryset):
        rows_deactivated = queryset.update(is_active=True)
        queryset.update(date_in=datetime.now())
        if rows_deactivated == 1:
            message_bit = "1 afiliación fue"
        else:
            message_bit = "%s afiliaciones fueron" % rows_deactivated
        self.message_user(request, "%s exitosamente canceladas(s)." % message_bit)

    make_deactive.short_description = "Cancelar afiliación"

admin.site.register(Affilliation, AffilliationAdmin)

class AuditHistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Afiliación', {
            'fields': ['affiliates', 'affiliation', ],
        }),
        ('Fechas', {
            'fields': ['date_out', ],
        }),
        ('Notas', {
            'fields': ['notes', ],
        }),
    ]
    list_display = ('affiliates', 'affiliation', 'date_in', 'date_out', 'notes',)
    list_editable = ('notes',)
    list_filter = ('affiliates', 'affiliation', 'date_in', 'date_out',)
    search_fields = ('affiliates', 'affiliation', 'date_in', 'date_out',)

admin.site.register(AuditHistory, AuditHistoryAdmin)