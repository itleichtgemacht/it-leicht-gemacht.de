from django.urls import path
from . import views

urlpatterns = [
    # Wird http://127.0.0.1 aufgerufen, so soll eine HTML Seite
    # namens home.html geladen werden
    # hierzu muss eine View erstellt werden und eine HTML Datei
    # namens home.html
    path('', views.home, name='home'),
    path('impressum', views.impressum, name='impressum'),

    path('post', views.post_list, name='post_list'),
    path('post/categorie/<str:filter>',views.post_list_categorie, name='post_list_categorie'),
    path("post/neu/", views.post_create, name="post_create"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/<int:pk>/bearbeiten/", views.post_update, name="post_update"),
    path("post/<int:pk>/loeschen/", views.post_delete, name="post_delete"),

    path('login/', views.loginSeite, name ="login"),
    path('logout/', views.logoutBenutzer, name ="logout"),
    path('reg/', views.regBenutzer, name ="reg"),

    
]

