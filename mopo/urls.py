from django.urls import path

from . import views

app_name = 'mopo'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # # ex: /mopo/5/
    # path('<int:quote_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # # ex: /mopo/5/summary/
    # path('<int:quote_id>/summary/', views.summary, name='summary'),
    path('<int:pk>/results/', views.SummaryView.as_view(), name='summary'),
    # TODO: add comment with commentform:
    # # ex: /mopo/5/comment/
    # path('<int:quote_id>/comment/', views.comment, name='comment'),
    # ex: /mopo/5/vote
    path('<int:quote_id>/vote', views.vote, name='vote'),
]
