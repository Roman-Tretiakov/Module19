from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Product, Review
from .forms import ReviewForm
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from django.shortcuts import render, get_object_or_404, redirect


@api_view(['GET'])
def category_list_api(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def product_list_api(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product  # Связываем отзыв с продуктом
            review.save()
            return redirect('product_reviews', product_id=product.id)  # Перенаправляем на ту же страницу
    else:
        form = ReviewForm()
    return render(request, 'catalog/product_reviews.html', {
        'product': product, 'reviews': reviews, 'form': form
    })


@api_view(['GET', 'POST'])
def review_list(request, product_id):
    if request.method == 'GET':
        reviews = Review.objects.filter(product_id=product_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewForm(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
