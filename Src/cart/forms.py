from django import forms
from django.utils.translation import gettext_lazy as _



PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)


# def CartAddProductForm_func(max_inventory = 10):
#     PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, max_inventory)]
#     class CartAddProductForm_(forms.Form):
#         quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
#         override = forms.BooleanField(required=False,
#                                     initial=False,
#                                     widget=forms.HiddenInput)

#     return CartAddProductForm_

