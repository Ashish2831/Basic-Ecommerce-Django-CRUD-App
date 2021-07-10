from django.urls import path, include
from . import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name="Categories"),
    path('categories/<int:id>/', views.CategoryView.as_view(), name="Category"),
    path('updatecategory/<int:id>/', views.UpdateCategory.as_view(), name="UpdateCategory"),
    path('deletecategory/<int:id>/', views.DeleteCategory.as_view(), name="DeleteCategory"),
    path('products/', views.ProductView.as_view(), name="Products"),
    path('products/<int:id>/', views.ProductView.as_view(), name="Product"),
    path('updateproduct/<int:id>/', views.UpdateProduct.as_view(), name="UpdateProduct"),
    path('deleteproduct/<int:id>/', views.DeleteProduct.as_view(), name="DeleteProduct"),
    path('sizes/', views.SizeView.as_view(), name="Sizes"),
    path('sizes/<int:id>/', views.SizeView.as_view(), name="Size"),
    path('updatesize/<int:id>/', views.UpdateSize.as_view(), name="UpdateSize"),
    path('deletesize/<int:id>/', views.DeleteSize.as_view(), name="DeleteSize"),
    path('productsizes/', views.ProductSizeView.as_view(), name="ProductSizes"),
    path('productsizes/<int:id>/', views.ProductSizeView.as_view(), name="ProductSize"),
    path('updateproductsize/<int:id>/', views.UpdateProductSize.as_view(), name="UpdateProductSize"),
    path('deleteproductsize/<int:id>/', views.DeleteProductSize.as_view(), name="DeleteProductSize"),
    path('productimages/', views.ProductImagesView.as_view(), name="ProductImages"),
    path('productimages/<int:id>/', views.ProductImagesView.as_view(), name="ProductImage"),
    path('updateproductimage/<int:id>/', views.UpdateProductImage.as_view(), name="UpdateProductImage"),
    path('deleteproductimage/<int:id>/', views.DeleteProductImage.as_view(), name="DeleteProductImage"),
]
