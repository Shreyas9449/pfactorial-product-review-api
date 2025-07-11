from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class ProductSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    review_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'created_by', 'created_at', 'updated_at', 'average_rating', 'review_count']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'feedback', 'created_at']
    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError('Rating must be between 1 and 5.')
        return value
    def validate(self, data):
        request = self.context.get('request')
        user = request.user if request else None
        product = data.get('product')
        if self.instance is None and user and product:
            if Review.objects.filter(user=user, product=product).exists():
                raise serializers.ValidationError('You have already reviewed this product.')
        return data
