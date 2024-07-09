from django import forms
from django.template.defaultfilters import slugify
from DjangoBlogApp.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from tinymce import models as tinymce_models
from .models import Post


from tinymce.widgets import TinyMCE 
class TinyMCEWidget(TinyMCE): 
    def use_required_attribute(self, *args): 
        return False
    
    
class EigeneUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['username'].label = 'Benutzername'
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].label = 'Passwort'
        self.fields['password2'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].label = 'Passwort wiederholen'
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].label = 'Email'
       


class PostFormular(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
    
    CATEGORIE = (
        ("microsoft", "Microsoft"),
        ("office", "Office"),
        ("python", "Python"),
        ("django", "Django"),
        ("html", "HTML"),
        ("css", "CSS"),
        ("boostrap", "Bootstrap"),
        ("linux", "Linux"),
        ("github", "github")
    )
        
    categorie = forms.ChoiceField(choices=CATEGORIE, label='Kategorie' )

    title = forms.CharField(label='Beitrag - Titel',widget=forms.TextInput(attrs={'placeholder': 'Titel des Beitrages'}))
    # content = tinymce_models.HTMLField(name='Beitrag')
    created_date = forms.DateTimeField(label='Erstellt am:')
    published_date = forms.DateTimeField(label='veröffentlich am:')
      
        
   