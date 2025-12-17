from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['restaurant_name', 'items', 'total_price']
        widgets = {
            'items': forms.Textarea(attrs={'rows': 4, 'placeholder': '例: 野菜プレート x1, パフェ x1'}),
            'restaurant_name': forms.TextInput(attrs={'placeholder': 'レストラン名'}),
        }

