# Generated by Django 5.0.2 on 2024-03-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoBlogApp', '0009_rename_categrorie_post_categorie_alter_post_typ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorie',
            field=models.CharField(blank=True, choices=[('microsoft', 'Microsoft'), ('office', 'Office'), ('python', 'Python'), ('django', 'Django'), ('html', 'HTML'), ('css', 'CSS'), ('boostrap', 'Bootstrap'), ('linux', 'Linux')], max_length=50, null=True),
        ),
    ]
