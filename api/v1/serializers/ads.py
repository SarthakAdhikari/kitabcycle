from ads.models import Ad, Book, Category, Condition, Price, PriceType, AdType
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class AdTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdType
        fields = '__all__'

class ConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    original = serializers.FloatField(source='original_price')
    final = serializers.FloatField(source='current_price')

    class Meta:
        model = Price
        fields = ('original', 'final', 'price_type')

class PriceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PriceType
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AdSerializer(serializers.ModelSerializer):

    book = BookSerializer()
    price = PriceSerializer()

    class Meta:
        model = Ad
        fields = '__all__'

    def create(self, validated_data):
        book_data = validated_data.pop('book')
        book = Book.objects.create(**book_data)

        price_data = validated_data.pop('price')
        price = Price.objects.create(**price_data)

        ad = Ad.objects.create(book=book, price=price,**validated_data)
        return ad
