from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import *

# Create your forms here.
class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields.get('name').required = False

    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Category Name'})
        }

    def clean_name(self):
        inp_name = self.cleaned_data.get('name')
        if len(inp_name.strip()) == 0:
            raise ValidationError(_("Please Enter Category Name!"))
        return inp_name

        
class SizeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SizeForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields.get('category_id').required = False
        self.fields.get('size').required = False

    class Meta:
        model = Size
        fields = '__all__'

        widgets = {
            'category_id' : forms.Select(attrs={'class' : 'form-control'}),
            'size' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Size'})
        }

    def clean_category_id(self):
        inp_category_id = self.cleaned_data.get('category_id')
        if inp_category_id == None:
            raise ValidationError(_("Please Select Category!"))
        return inp_category_id

    def clean_size(self):
        inp_size = self.cleaned_data.get('size')
        if inp_size == 0:
            raise ValidationError(_("Please Enter Valid Size!"))
        return inp_size


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields.get('name').required = False
        self.fields.get('price').required = False
        self.fields.get('description').required = False
        self.fields.get('category_id').required = False

    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Name'}),
            'price' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Price'}),
            'description' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Description'}),
            'category_id' : forms.Select(attrs={'class' : 'form-control'}),
        }

    def clean_name(self):
        inp_name = self.cleaned_data.get('name')
        if len(inp_name) == 0:
            raise ValidationError(_("Please Enter Product Name!"))
        return inp_name

    def clean_price(self):
        inp_price = self.cleaned_data.get('price')
        if inp_price == None:
            raise ValidationError(_("Please Enter Valid Price!"))
        return inp_price

    def clean_description(self):
        inp_description = self.cleaned_data.get('description')
        if len(inp_description) == 0:
            raise ValidationError(_("Please Enter Description!"))
        return inp_description

    def clean_category_id(self):
        inp_category_id = self.cleaned_data.get('category_id')
        if inp_category_id == None:
            raise ValidationError(_("Please Select Category!"))
        return inp_category_id


class ProductSizeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductSizeForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields.get('product_id').required = False
        self.fields.get('size_id').required = False

    class Meta:
        model = ProductSize
        fields = '__all__'

        widgets = {
            'product_id' : forms.Select(attrs={'class' : 'form-control'}),
            'size_id' : forms.CheckboxSelectMultiple(),
        }

    def clean_product_id(self):
        inp_product_id = self.cleaned_data.get('product_id')
        if inp_product_id == None:
            raise ValidationError(_("Please Select Product!"))
        return inp_product_id

    def clean_size_id(self):
        inp_size_id = self.cleaned_data.get('size_id')
        if len(inp_size_id) == 0:
            raise ValidationError(_("Please Select Size!"))
        return inp_size_id


class ProductImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductImageForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields.get('product_id').required = False
        self.fields.get('image').required = False

    class Meta:
        model = ProductImage
        fields = '__all__'

        widgets = {
            'product_id' : forms.Select(attrs={'class' : 'form-control'}),
            'image' : forms.FileInput(attrs={'class' : 'form-control'})
        }

    def clean_product_id(self):
        inp_product_id = self.cleaned_data.get('product_id')
        if inp_product_id == None:
            raise ValidationError(_("Please Select Product!"))
        return inp_product_id

    def clean_image(self):
        inp_image = self.cleaned_data.get('image')
        if inp_image == None:
            raise ValidationError(_("Please Upload Image!"))
        return inp_image
