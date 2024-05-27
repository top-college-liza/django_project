from django import forms
from .bulma_mixin import BulmaMixin
from store.models import *


class OrderForm(BulmaMixin, forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Напишите адрес доставки'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Напишите номер телефона'
    }))
    status = forms.ChoiceField(choices=STATUS)

    class Meta:
        model = Order
        fields = ['address', 'phone', 'status']



class ProductForm(BulmaMixin, forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Напишите наименование товара'
    }), required=False)
    slug = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Придумайте уникальный идентификатор'
    }), required=False)
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Описание продукта'
    }), required=False)
    price = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите цену товара'
    }), required=False)
    is_new = forms.CharField(widget=forms.CheckboxInput(), label='Новинка', required=False)
    is_discounted = forms.CharField(widget=forms.CheckboxInput(), label='Скидка', required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'description',
            'price',
            'is_new',
            'is_discounted',
            'category',
            'brand',
            'image'
        ]
