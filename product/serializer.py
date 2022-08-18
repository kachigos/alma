from rest_framework import serializers

from .models import Product, Category, Rating, Like, Favorite
from comments.models import Comment

from comments.serializers import CommentSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance: Product):
        rep = super().to_representation(instance)
        rep["comments"] = CommentSerializer(instance.comments.all(), many=True).data
        rep["likes"] = instance.likes.all().count()
        rep["rating"] = instance.get_average_rating()
        rep["liked_by_user"] = False
        rep["user_rating"] = 0
        rep["favorites"] = instance.favorites.all().count()
        rep["favorite_by_user"] = False
        # rep['images'] = ProductImageSerializer(instance.image.all(),
        #                                        many=True, context=self.context).data

        request = self.context.get("request")

        if request.user.is_authenticated:
            rep["liked_by_user"] = Like.objects.filter(user=request.user, product=instance).exists()
            if Rating.objects.filter(user=request.user, product=instance).exists():
                rating = Rating.objects.get(user=request.user, product=instance)
                rep["user_rating"] = rating.value

        return rep


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        exclude = ['user', ]
