# Generated by Django 4.0.3 on 2022-03-27 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        migrations.swappable_dependency(settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SitePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='users_permitted', to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL, verbose_name='site')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_permissions', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'permissão de acesso',
                'verbose_name_plural': 'permissões de acesso',
            },
        ),
    ]
