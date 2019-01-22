from django.urls import include, path
from .views import (
    index,
    signup, login, logout,
    edit_info,
    menu, menu_add,
)

urlpatterns = [
    path('', index, name ="index" ),
    path('signup/', signup, name ="signup" ),
    path('login/', login, name ="login" ),
    path('logout/', login, name ="logout" ),
    path('edit_info/', edit_info, name ="edit_info" ),
    path('menu/', menu, name ="menu" ),
    path('menu/add/', menu_add, name ="menu_add" ),
]
