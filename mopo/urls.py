from django.urls import path

from . import views

app_name = 'mopo'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /mopo/5/
    path('<int:quote_id>/', views.detail, name='detail'),
    # ex: /mopo/5/summary/
    path('<int:quote_id>/summary/', views.summary, name='summary'),
    # ex: /mopo/5/comment/
    path('<int:quote_id>/comment/', views.comment, name='comment'),
    # ex: /mopo/5/vote/1
    path('<int:quote_id>/vote', views.vote, name='vote'),
]
