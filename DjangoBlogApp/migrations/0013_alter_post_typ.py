# Generated by Django 5.0.2 on 2024-03-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoBlogApp', '0012_alter_post_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='typ',
            field=models.CharField(blank=True, choices=[('page', 'Seite'), ('blog', 'Blog'), ('home', 'Home'), ('impressum', 'Impressum'), ('template', 'Template')], max_length=20, null=True),
        ),
    ]
