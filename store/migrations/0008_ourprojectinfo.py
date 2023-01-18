# Generated by Django 4.0.5 on 2023-01-12 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0007_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurProjectInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, verbose_name='Company Name')),
                ('company_address', models.CharField(max_length=250, verbose_name='Company address')),
                ('about_company', models.CharField(max_length=250, verbose_name='About Company')),
                ('email_adddress', models.CharField(max_length=50, verbose_name='Email adddress')),
                ('contract_number', models.CharField(max_length=15, verbose_name='Contract Number')),
                ('facebook', models.CharField(max_length=250, verbose_name='Facebook')),
                ('twitter', models.CharField(max_length=250, verbose_name='Twitter')),
                ('youtube', models.CharField(max_length=250, verbose_name='Youtube')),
                ('linkedin', models.CharField(max_length=250, verbose_name='Linkedin')),
                ('company_logo', models.ImageField(upload_to='logo')),
                ('fabi_icon', models.ImageField(upload_to='fabi_icon')),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]