from django.urls import include, path
from .views import index, signup, login

urlpatterns = [
    path('', index, name ="index" ),
    path('signup/', signup, name ="signup" ),
    path('login/', login, name ="login" ),
]
