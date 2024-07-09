from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from tinymce import models as tinymce_models


# models.CharField – so definierst du ein Textfeld mit einer limitierten Anzahl von Zeichen.
# models.TextField – so definierst du ein langes Textfeld ohne Grössenbeschränkung. 
# models.DateTimeField – ein Feld für einen Zeitpunkt (ein Datum und eine Uhrzeit).
# models.ForeignKey – definiert eine Verknüpfung/Beziehung zu einem anderen Model.

class Post(models.Model):
    
    class Typ(models.TextChoices):
        PAGE = "page", "Seite"
        BLOG = "blog", "Blog"
        HOME = "home", "Home"
        IMPRESSUM = "impressum", "Impressum"
        TEMPLATE = "template", "Template"

    typ = models.CharField(
        max_length=20, choices=Typ.choices, null=True, blank=True
    )
    
    class Categorie(models.TextChoices):
        MiCROSOFT = "microsoft", "Microsoft"
        OFFICE = "office", "Office"
        PYTHON = "python", "Python"
        DJANGO = "django", "Django"
        HTML = "html", "HTML"
        CSS = "css", "CSS"
        BOOTSTRAP = "boostrap", "Bootstrap"
        LINUX = "linux", "Linux"
        GITHUB = "github", "github"
        
    categorie = models.CharField( max_length=50, choices=Categorie.choices, null=True, blank=True )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = tinymce_models.HTMLField(default="", null=True, blank=True )
    banner_bild = models.ImageField(upload_to ='uploads/', default='uploads/default.jpg', null=True, blank=True) 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    # ### AH
# Author:   Armin Hünniger
# Erstellt: 11.02.2024
# ###
# Spaltendefinitionen unter:
# Feld Typen: https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field
#
# ## CharField
# hausnummer = models.CharField(max_length=25, default="", null=True, blank=True)
#
# ## DateField - DateTimeField
# erstellt_am = models.DateTimeField(auto_now_add=True)
# aktualisiert_am = models.DateTimeField(auto_now=True)
# enddatum = models.DateField()

## DecimalField
# monatlicher_betrag = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
#
#
###

# ### AH
# Login 
# Staff = Mitarbeiter, Kunde usw.
# ###
class Staff(models.Model):
    class Position(models.TextChoices):
        AGENT = "agent", "Agent"
        MANAGER = "manager", "Manager"
        SUPPORT = "support", "Support"
        ADMIN = "admin", "Administrator"
    position = models.CharField(
        max_length=100, choices=Position.choices, null=True, blank=True
    )
    benutzer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.name} --> {self.position}"
    
 
    
    