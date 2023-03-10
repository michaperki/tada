from django.urls import path

from . import views

app_name = 'tada'
urlpatterns = [
    # ex: /tada/
    path('', views.index, name='index'),
    # ex: /tada/5/
    path('<int:tada_id>/', views.detail, name='detail'),
    # ex: /tada/5/results/
    path('<int:tada_id>/results/', views.results, name='results'),
    # ex: /tada/5/modules/
    path('<int:tada_id>/modules/', views.modules, name='modules'),
    # ex: /tada/5/modules/2
    path('<int:tada_id>/module/<int:module_id>', views.module, name='module'),
    # ex: /tada/5/modules/2/setting/3
    path('<int:tada_id>/setting/', views.setting, name='setting'),
    # ex: /tada/5/modules/2/setting/3
    path('<int:tada_id>/setting/<int:setting_id>', views.setting, name='setting'),
    
]