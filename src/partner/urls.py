from django.urls import include, path
from .views import index, signup

urlpatterns = [
    path('', index, name ="index" ),
    path('signup/', signup, name ="signup" ),
]
