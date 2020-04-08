from django.urls import path

from . import views

app_name = 'manga'

urlpatterns = [
    path('', views.homePage, name='home'),
    path('<slug:name>/list/', views.ListView.as_view(), name='index'),
    path('<slug:name>/detail/<int:chap>/', views.DetailView.as_view(), name='detail'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('<slug:name>/detail/<int:chap>/delete/', views.DeleteOneView.as_view(), name='delete1'),
    path('<slug:name>/detail/<int:chap>/update/', views.UpdateOneView.as_view(), name='update1'),
    path('<slug:name>/delete/', views.DeleteAllView.as_view(), name='deleteall'),
    path('<slug:name>/update/', views.UpdateAllView.as_view(), name='updateall'),
    path('video/', views.videoView, name='video')
]
