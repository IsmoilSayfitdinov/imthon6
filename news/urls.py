from django.urls import path
from .views import get_models_list_news_fucntion, register, user_login, user_logout, search_data, create_data_function

app_name = "news"

urlpatterns = [
    path('', get_models_list_news_fucntion, name="list_news"),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('search/', search_data, name='search_data'),
    path('add/', create_data_function, name='create_data'),
   
]