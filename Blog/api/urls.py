from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, PostListCreateView, PostRetrieveUpdateDestroyView,
 ComentarioListCreateView, ComentarioRetrieveUpdateDestroyView , LoginView

urlpatterns = [
    path('usuario/', UserListCreateView.as_view(), name='users_list'),
    path('usuario/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='manipulate-user'),  
    
    path('post/', PostListCreateView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='manipulate-post'),  
    
    path('comentario/', ComentarioListCreateView.as_view(), name='comentarios_list'),
    path('comentario/<int:pk>/', ComentarioRetrieveUpdateDestroyView.as_view(), name='manipulate-comentario'),

    path('login/', views.LoginView.as_view(), name='login'),
    
]