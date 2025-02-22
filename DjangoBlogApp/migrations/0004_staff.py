# Generated by Django 5.0.2 on 2024-03-02 10:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoBlogApp', '0003_rename_posts_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, choices=[('agent', 'Agent'), ('manager', 'Manager'), ('support', 'Support'), ('admin', 'Administrator')], max_length=100, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('benutzer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
