from .views import (home_page, logout_user, painel_page, Create, UpdateView, DeleteView, login_page, authenticate_login, Find)
from django.urls import path


urlpatterns = [
    path('home/', home_page, name="home"),
    path('post/ajax/create/', Create.as_view(), name="post_create"),
    path('ajax/crud/update/', UpdateView.as_view(), name='post_update'),
    path('ajax/crud/delete/', DeleteView.as_view(), name='post_delete'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('auth/', authenticate_login, name='authenticate'),
    path('ajax/model/find/', Find.as_view(), name='post_find'),
    path('', painel_page, name='painel')
]