# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import modelcluster.tags
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtaildocs', '0002_initial_data'),
        ('taggit', '0001_initial'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.URLField(blank=True, null=True)),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Alerta',
                'verbose_name_plural': 'Alertas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdvertPlacement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('advert', models.ForeignKey(to='core.Advert', related_name='+')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Indice de Blogs',
                'verbose_name_plural': 'Indices de Blogs',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace.', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('date', models.DateField(verbose_name='Publicación')),
                ('feed_image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace.', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content_object', modelcluster.fields.ParentalKey(to='core.BlogPage', related_name='tagged_items')),
                ('tag', models.ForeignKey(to='taggit.Tag', related_name='core_blogpagetag_items')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=100, blank=True)),
                ('telephone', models.CharField(verbose_name='Teléfono', max_length=20, blank=True)),
                ('email', models.EmailField(verbose_name='Correo Electrónico', max_length=75, blank=True)),
                ('address_1', models.CharField(verbose_name='Dirección 1', max_length=255, blank=True)),
                ('address_2', models.CharField(verbose_name='Dirección 2', max_length=255, blank=True)),
                ('district', models.CharField(verbose_name='Barrio', max_length=255, blank=True)),
                ('city', models.CharField(verbose_name='Ciudad', max_length=255, blank=True)),
                ('country', models.CharField(verbose_name='País', max_length=255, blank=True)),
                ('post_code', models.CharField(verbose_name='Código Postal', max_length=10, blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Página de Contacto',
                'verbose_name_plural': 'Página de Contactos',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='EventIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Indice de Eventos',
                'verbose_name_plural': 'Indices de Eventos',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace.', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
                ('date_from', models.DateField(verbose_name='Start date')),
                ('date_to', models.DateField(help_text='Not required if event is on a single day', verbose_name='End date', blank=True, null=True)),
                ('time_from', models.TimeField(verbose_name='Start time', blank=True, null=True)),
                ('time_to', models.TimeField(verbose_name='End time', blank=True, null=True)),
                ('audience', models.CharField(choices=[('public', 'Público'), ('private', 'Privado')], max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('cost', models.CharField(max_length=255)),
                ('signup_link', models.URLField(blank=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventPageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace.', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventPageSpeaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('first_name', models.CharField(verbose_name='Nombres', max_length=255, blank=True)),
                ('last_name', models.CharField(verbose_name='Apellidos', max_length=255, blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('label', models.CharField(help_text='The label of the form field', max_length=255)),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], max_length=16)),
                ('required', models.BooleanField(default=True)),
                ('choices', models.CharField(help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', max_length=512, blank=True)),
                ('default_value', models.CharField(help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, blank=True)),
                ('help_text', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
                ('to_address', models.CharField(help_text='Optional - form submissions will be emailed to this address', max_length=255, blank=True)),
                ('from_address', models.CharField(max_length=255, blank=True)),
                ('subject', models.CharField(max_length=255, blank=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('thank_you_text', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Página de Formulario',
                'verbose_name_plural': 'Página de Formularios',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomePageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace.', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Indice de Noticia',
                'verbose_name_plural': 'Indice de Noticias',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NewIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace.', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('date', models.DateField(verbose_name='Publicación')),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NewPageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace.', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=100, blank=True)),
                ('telephone', models.CharField(verbose_name='Teléfono', max_length=20, blank=True)),
                ('email', models.EmailField(verbose_name='Correo Electrónico', max_length=75, blank=True)),
                ('address_1', models.CharField(verbose_name='Dirección 1', max_length=255, blank=True)),
                ('address_2', models.CharField(verbose_name='Dirección 2', max_length=255, blank=True)),
                ('district', models.CharField(verbose_name='Barrio', max_length=255, blank=True)),
                ('city', models.CharField(verbose_name='Ciudad', max_length=255, blank=True)),
                ('country', models.CharField(verbose_name='País', max_length=255, blank=True)),
                ('post_code', models.CharField(verbose_name='Código Postal', max_length=10, blank=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('biography', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
                ('image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Página Personal',
                'verbose_name_plural': 'Páginas Personales',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='PersonPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace.', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StandardIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Indice de páginas estandar',
                'verbose_name_plural': 'Indices de páginas estandar',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StandardIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace.', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Página Estandar',
                'verbose_name_plural': 'Páginas Estandar',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StandardPageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(to='core.StandardPage', related_name='carousel_items')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StandardPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace.', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(to='core.StandardPage', related_name='related_links')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='standardindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='standardindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.StandardIndexPage', related_name='related_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.PersonPage', related_name='related_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.NewPage', related_name='related_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newpagecarouselitem',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newpagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.NewPage', related_name='carousel_items'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.NewIndexPage', related_name='related_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagerelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.HomePage', related_name='related_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagecarouselitem',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.HomePage', related_name='carousel_items'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.FormPage', related_name='form_fields'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagespeaker',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagespeaker',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.EventPage', related_name='speakers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.EventPage', related_name='related_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagecarouselitem',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.EventPage', related_name='carousel_items'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.EventIndexPage', related_name='related_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.BlogPage', related_name='related_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagecarouselitem',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.BlogPage', related_name='carousel_items'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.tags.ClusterTaggableManager(help_text='A comma-separated list of tags.', blank=True, verbose_name='Tags', through='core.BlogPageTag', to='taggit.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(to='core.BlogIndexPage', related_name='related_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advertplacement',
            name='page',
            field=modelcluster.fields.ParentalKey(to='wagtailcore.Page', related_name='advert_placements'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advert',
            name='page',
            field=models.ForeignKey(blank=True, null=True, related_name='adverts', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Página de Inicio'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
    ]
