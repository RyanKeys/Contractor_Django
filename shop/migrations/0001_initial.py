# Generated by Django 2.2.6 on 2020-03-06 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of your listing:', max_length=50)),
                ('slug', models.CharField(blank=True, editable=False, help_text='Unique URL path to access this page. Generated by the system.', max_length=50)),
                ('created', models.TextField(help_text='Date and time model was created')),
                ('publisher', models.ForeignKey(help_text='Publisher of the listing', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
