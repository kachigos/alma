from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, CategoryViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CategoryViewSet, CommentViewSet, add_rating, favorites, FavouriteViewSet

router = DefaultRouter()
router.register("product", ProductViewSet)
router.register("category", CategoryViewSet)
router.register("comments", CommentViewSet)
router.register("favorites", FavouriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add_rating/<int:p_id>/', add_rating),
    path('add_to_favorite/<int:s_id>/', favorites),

]
