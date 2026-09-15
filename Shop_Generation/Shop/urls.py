from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.home, name='home'),
<<<<<<< Updated upstream
    path(route='home', view=views.home, name='home'),
    path(route='clothes', view=views.clothes, name='clothes'),
    path('view/<int:id>', view=views.view, name='view')
=======
    path(route='home/', view=views.home, name='home'),
    path(route='shoeses/', view = views.shoeses, name='shoeses'),
    path(route='shoeses_detail/<int:id>', view = views.shoeses_detail, name='shoeses_detail'),
>>>>>>> Stashed changes
]