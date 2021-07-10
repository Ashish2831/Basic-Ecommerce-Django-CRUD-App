from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.views.generic.base import View
from django.core.paginator import Paginator
from .models import *
from .forms import *

# Create your views here.
class CategoryView(View):
    def get(self, request, id = None, *args, **kwargs):
        category_form = CategoryForm()
        if id is not None:
            categories = [Category.objects.get(pk=id)]
        else:
            categories = Category.objects.all()
        paginator = Paginator(categories, 10, orphans=4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "Core/categories.html", {'page_obj' : page_obj, 'form' : category_form})

    def post(self, request, *args, **kwargs) :
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Category Added Successfully!")
        else:
            messages.error(request, "Not Able To Add Category!")
            categories = Category.objects.all()
            return render(request, "Core/categories.html", {'categories' : categories, 'form' : category_form})
        return HttpResponseRedirect('/categories/')


class UpdateCategory(View):
    def get(self, request, id, *args, **kwargs):
        category = Category.objects.get(pk=id)
        category_form = CategoryForm(instance=category)
        return render(request, "Core/updatecategory.html", {'form' : category_form})

    def post(self, request, id, *args, **kwargs) :
        category = Category.objects.get(pk=id)
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Category Updated Successfully!")
        else:
            messages.error(request, "Not Able To Update Category!")
            categories = Category.objects.all()
            return render(request, "Core/categories.html", {'categories' : categories, 'form' : category_form})
        return HttpResponseRedirect('/categories/')


class DeleteCategory(View):
    def get(self, request, id, *args, **kwargs):
        category = Category.objects.get(pk=id)
        category.delete()
        messages.success(request, "Category Deleted Successfully!")
        return HttpResponseRedirect("/categories/")


class ProductView(View):
    def get(self, request, id = None, *args, **kwargs):
        product_form = ProductForm()
        if id is not None:
            products = [Product.objects.get(pk=id)]
        else:
            products = Product.objects.all()
        paginator = Paginator(products, 10, orphans=4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "Core/products.html", {'page_obj' : page_obj, 'form' : product_form})

    def post(self, request, *args, **kwargs) :
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Product Added Successfully!")
        else:
            messages.error(request, "Not Able To Add Product!")
            products = Product.objects.all()
            return render(request, "Core/products.html", {'products' : products, 'form' : product_form})
        return HttpResponseRedirect('/products/')


class UpdateProduct(View):
    def get(self, request, id, *args, **kwargs):
        product = Product.objects.get(pk=id)
        product_form = ProductForm(instance=product)
        return render(request, "Core/updateproduct.html", {'form' : product_form})

    def post(self, request, id, *args, **kwargs) :
        product = Product.objects.get(pk=id)
        product_form = ProductForm(request.POST, instance=product)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Product Updated Successfully!")
        else:
            messages.error(request, "Not Able To Update Product!")
            products = Product.objects.all()
            return render(request, "Core/products.html", {'products' : products, 'form' : product_form})
        return HttpResponseRedirect('/products/')


class DeleteProduct(View):
    def get(self, request, id, *args, **kwargs):
        product = Product.objects.get(pk=id)
        product.delete()
        messages.success(request, "Product Deleted Successfully!")
        return HttpResponseRedirect("products")


class SizeView(View):
    def get(self, request, id = None, *args, **kwargs):
        size_form = SizeForm()
        if id is not None:
            sizes = [Size.objects.get(pk=id)]
        else:
            sizes = Size.objects.all()
        paginator = Paginator(sizes, 10, orphans=4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "Core/sizes.html", {'page_obj' : page_obj, 'form' : size_form})

    def post(self, request, *args, **kwargs) :
        size_form = SizeForm(request.POST)
        if size_form.is_valid():
            size_form.save()
            messages.success(request, "Size Added Successfully!")
        else:
            messages.error(request, "Not Able To Add Size!")
            sizes = Size.objects.all()
            return render(request, "Core/sizes.html", {'sizes' : sizes, 'form' : size_form})
        return HttpResponseRedirect('/sizes/')


class UpdateSize(View):
    def get(self, request, id, *args, **kwargs):
        size = Size.objects.get(pk=id)
        size_form = SizeForm(instance=size)
        return render(request, "Core/updatesize.html", {'form' : size_form})

    def post(self, request, id, *args, **kwargs) :
        size = Size.objects.get(pk=id)
        size_form = SizeForm(request.POST, instance=size)
        if size_form.is_valid():
            size_form.save()
            messages.success(request, "Size Updated Successfully!")
        else:
            messages.error(request, "Not Able To Update Size!")
            sizes = Size.objects.all()
            return render(request, "Core/sizes.html", {'sizes' : sizes, 'form' : size_form})
        return HttpResponseRedirect('/sizes/')


class DeleteSize(View):
    def get(self, request, id, *args, **kwargs):
        size = Size.objects.get(pk=id)
        size.delete()
        return HttpResponseRedirect('/sizes/')


class ProductSizeView(View):
    def get(self, request, id = None, *args, **kwargs):
        product_size_form = ProductSizeForm()
        if id is not None:
            productSizes = [ProductSize.objects.get(pk=id)]
        else:
            productSizes = ProductSize.objects.all()
        paginator = Paginator(productSizes, 10, orphans=4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "Core/productsizes.html", {'page_obj' : page_obj, 'form' : product_size_form})

    def post(self, request, *args, **kwargs) :
        product_size_form = ProductSizeForm(request.POST)
        if product_size_form.is_valid():
            product_size_form.save()
            messages.success(request, "Product Size Added Successfully!")
        else:
            messages.error(request, "Not Able To Add Product Size!")
            productSizes = ProductSize.objects.all()
            return render(request, "Core/productsizes.html", {'productSizes' : productSizes, 'form' : product_size_form})
        return HttpResponseRedirect('/productsizes/')


class UpdateProductSize(View):
    def get(self, request, id, *args, **kwargs):
        productSize = ProductSize.objects.get(pk=id)
        product_size_form = ProductSizeForm(instance=productSize)
        return render(request, "Core/updateproductsize.html", {'form' : product_size_form})

    def post(self, request, id, *args, **kwargs):
        productSize = ProductSize.objects.get(pk=id)
        product_size_form = ProductSizeForm(request.POST, instance=productSize)
        if product_size_form.is_valid():
            product_size_form.save()
            messages.success(request, "Product Size Updated Successfully!")
        else:
            messages.error(request, "Not Able To Update Product Size!")
            productSizes = ProductSize.objects.all()
            return render(request, "Core/productsizes.html", {'productSizes' : productSizes, 'form' : product_size_form})
        return HttpResponseRedirect('/productsizes/')


class DeleteProductSize(View):
    def get(self, request, id, *args, **kwargs):
        productSize = ProductSize.objects.get(pk=id)
        productSize.delete()
        return HttpResponseRedirect('/productsizes/')


class ProductImagesView(View):
    def get(self, request, id = None, *args, **kwargs):
        product_image_form = ProductImageForm()
        if id is not None:
            productImages = [ProductImage.objects.get(pk=id)]
        else:
            productImages = ProductImage.objects.all()
        paginator = Paginator(productImages, 10, orphans=4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "Core/productimages.html", {'page_obj' : page_obj, 'form' : product_image_form})

    def post(self, request, *args, **kwargs) :
        product_image_form = ProductImageForm(request.POST, request.FILES)
        if product_image_form.is_valid():
            product_image_form.save()
            messages.success(request, "Product Image Added Successfully!")
        else:
            messages.error(request, "Not Able To Add Product Image!")
            productImages = ProductImage.objects.all()
            return render(request, "Core/productimages.html", {'productImages' : productImages, 'form' : product_image_form})
        return HttpResponseRedirect('/productimages/')


class UpdateProductImage(View):
    def get(self, request, id, *args, **kwargs):
        productImage = ProductImage.objects.get(pk=id)
        product_image_form = ProductImageForm(instance=productImage)
        return render(request, "Core/updateproductimage.html", {'form' : product_image_form})

    def post(self, request, id, *args, **kwargs):
        productImage = ProductImage.objects.get(pk=id)
        product_image_form = ProductImageForm(request.POST, request.FILES, instance=productImage)
        if product_image_form.is_valid():
            product_image_form.save()
            messages.success(request, "Product Image Updated Successfully!")
        else:
            messages.error(request, "Not Able To Update Product Image!")
            productImages = ProductImage.objects.all()
            return render(request, "Core/productimages.html", {'productImages' : productImages, 'form' : product_image_form})
        return HttpResponseRedirect('/productimages/')


class DeleteProductImage(View):
    def get(self, request, id, *args, **kwargs):
        productImage = ProductImage.objects.get(pk=id)
        productImage.delete()
        return HttpResponseRedirect('/productimages/')