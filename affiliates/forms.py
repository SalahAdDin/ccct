from django import forms
from .models import *

from wagtail.wagtailimages.forms import WagtailImageField

from smart_selects import form_fields, widgets



class AffilliationForm(forms.ModelForm):
    def __init__(self, instance=None, *args, **kwargs):
        _fields = (
        'name', 'logo', 'dni', 'adress', 'country', 'city', 'tel', 'fax', 'e_mail', 'web', 'attorney_name', 'position',
        'staff', 'interest', 'cause', 'economic_sector', 'economic_activity', 'other_interes', )
        _initial = forms.model_to_dict(instance.affiliates) if instance is not None else{}
        super(AffilliationForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
        self.fields.update(forms.fields_for_model(Affiliates, _fields))


    class Meta:
        model = Affilliation
        fields = ['person', 'affiliation', 'date_prein', ]
        exclude = ('affiliates', )
        widgets = {
            'person': form_fields.ChainedModelChoiceField(widget=widgets.ChainedSelect(attrs={'class':'form-control'})),
            'affiliation': form_fields.ChainedModelChoiceField(widget=widgets.ChainedSelect(attrs={'class':'form-control'})),
            'name': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
            'logo': WagtailImageField(widget=forms.FileInput()),
            'dni': forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'})),
            'adress': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
            'country': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
            'city': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
            'tel': forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'})),
            'fax': forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'})),
            'e_mail': forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'})),
            'web': forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'})),
            'attorney_name': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
            'position': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
            'staff': forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'})),
            'interest': forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=INTEREST_AREAS),
            'cause': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
            'economic_sector': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
            'economic_activity': forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=ECONOMIC_ACTIVITY),
            'other_interes': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
        }

    def as_div(self):
        "Returns this form rendered as HTML <div>s."
        return self._html_output(
            normal_row = u'<div class="form-group" %(html_class_attr)s>%(label)s</div> %(field)s%(help_text)s',
            error_row = u'%s',
            row_ender = '</div>',
            help_text_html = u' <span class="help-block">%s</span>',
            errors_on_separate_row = True)

    def save(self, *args, **kwargs):
        a = self.instance.affiliates
        a.name = self.cleaned_data['name']
        a.logo = self.cleaned_data['logo']
        a.dni = self.cleaned_data['dni']
        a.adress = self.cleaned_data['adress']
        a.country = self.cleaned_data['country']
        a.city = self.cleaned_data['city']
        a.tel = self.cleaned_data['tel']
        a.fax = self.cleaned_data['fax']
        a.e_mail = self.cleaned_data['e_mail']
        a.web = self.cleaned_data['web']
        a.attorney_name = self.cleaned_data['attorney_name']
        a.position = self.cleaned_data['position']
        a.staff = self.cleaned_data['staff']
        a.interest = self.cleaned_data['interest']
        a.cause = self.cleaned_data['cause']
        a.economic_sector = self.cleaned_data['economic_sector']
        a.economic_activity = self.cleaned_data['economic_activity']
        a.other_interes = self.cleaned_data['other_interes']
        a.save()
        affiliate = super(AffilliationForm, self).save(*args, **kwargs)
        return affiliate