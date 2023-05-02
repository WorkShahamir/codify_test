from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls import static


router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('category/', views.CategoryListCreateApiView.as_view()),
    # path('items/', views.ItemListCreateApiView.as_view()),
    path('function/item/', views.item_list_create_api_view),
    path('function/item/<int:pk>/', views.item_retrieve_update_destroy_api_view),
    path('class/item/', views.ItemListCreateApiView.as_view()),
    path('class/item/<int:pk>/', views.ItemRetrieveUpdateDestroyView.as_view()),
    # path('viewset/category/', views.CategoryViewSet.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('viewset/category/<int:pk>/', views.CategoryViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    # )),
    path('viewset/', include(router.urls)),
]
