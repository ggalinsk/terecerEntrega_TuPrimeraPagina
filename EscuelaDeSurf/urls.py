from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear-clase/', views.create_surf_class, name='crear_clase'),
    path('add-membershipplan/', views.create_membership_plan, name='create_membership_plan'),
    path('add-merchandising/', views.create_Products, name='add_merchandising'),
    path('clases/', views.list_surf_clases, name='list_surf_clases'),
    path('planes/', views.list_membership_plans, name='list_membership_plans'),
    path('merchandising/', views.list_products, name='list_products'),
    path('buscar-clase/', views.buscar_clase, name='buscar_clase'),
]
