from django.urls import include, path
from .views import (
    index,
    signup, login, logout,
    edit_info,
    menu, menu_add, menu_detail, menu_edit, menu_delete,
    order,
)

urlpatterns = [
    path('', index, name ="index" ),
    path('signup/', signup, name ="signup" ),
    path('login/', login, name ="login" ),
    path('logout/', logout, name ="logout" ),
    path('edit_info/', edit_info, name ="edit_info" ),
    path('menu/', menu, name ="menu" ),
    path('menu/add/', menu_add, name ="menu_add" ),
    path('menu/<int:menu_id>/', menu_detail, name ="menu_detail" ),
    path('menu/<int:menu_id>/edit/', menu_edit, name ="menu_edit" ),
    path('menu/<int:menu_id>/delete/', menu_delete, name ="menu_delete" ),
    path('order/', order, name ="order" ),
]
