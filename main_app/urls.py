from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='index'),
    path('birds/<int:bird_id>/', views.birds_detail, name='detail'),
    path('birds/create/', views.BirdCreate.as_view(), name='birds_create'),
    path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='birds_update'),
    path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='birds_delete'),
    path('birds/<int:bird_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('birds/<int:bird_id>/assoc_tree/<int:tree_id>', views.assoc_tree, name='assoc_tree'),
    path('birds/<int:bird_id>/unassoc_tree/<int:tree_id>', views.unassoc_tree, name='unassoc_tree'),
    path('trees/', views.TreeList.as_view(), name='trees_index'),
    path('trees/<int:pk>/', views.TreeDetail.as_view(), name='trees_detail'),
    path('trees/create/', views.TreeCreate.as_view(), name='trees_create'),
    path('trees/<int:pk>/update/', views.TreeUpdate.as_view(), name='trees_update'),
    path('trees/<int:pk>/delete/', views.TreeDelete.as_view(), name='trees_delete'),
]