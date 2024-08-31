from django.urls import path , include
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<int:post_id>',views.detail,name='detail'),
    path('old_url/',views.old_url_redirect,name='old_url'),
    path('pattu/',views.new_url,name='new_url')
]