from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from dashboard.views import index

from visitantes.views import (
    registrar_visitante, informacoes_visitante, finalizar_visita
)

urlpatterns = [
    path("",  auth_views.LoginView.as_view(
            template_name="login.html"
        ),),
    path("admin/", admin.site.urls),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="logout.html"
        ),
        name="logout"
    ),

     path("securevista",
         index,
         name="index",
         ),

    path(
        "registrar_visitante/",
        registrar_visitante,
        name="registrar_visitante",
    ),

    path(
        "visitantes/<int:id>/",
        informacoes_visitante,
        name="informacoes_visitante"
    ),

    path(
        "visitantes/<int:id>/finalizar-visita",
        finalizar_visita,
        name="finalizar_visita"
    )
]
