from django.urls import include, path
from .views import index, signup, login, logout

urlpatterns = [
    path('', index, name ="index" ),
    path('signup/', signup, name ="signup" ),
    path('login/', login, name ="login" ),
    path('logout/', login, name ="logout" ),
]
