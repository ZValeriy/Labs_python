from django import forms
from .models import Product, Brand
FORM_ERROR_MESSAGES = {'required': 'Пожалуйста, заполните это поле'}


class ProductForm(forms.Form):
    nameproduct = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'nameproduct',
                                                                'class': 'form-control', }),
                                  max_length=30)

    processor = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'processor',
                                                             'class': 'form-control', }),
                               max_length=30)
    screen_size = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'screen_size',
                                                                'class': 'form-control', }),
                                  max_length=30)

    gpu = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'gpu',
                                                        'class': 'form-control', }),
                          max_length=20)

    memory = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'memory',
                                                           'class': 'form-control', }),
                             max_length=30)

    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'description',
                                                                'class': 'form-control', }),
                                  max_length=1000)

    cost = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'cost',
                                                            'class': 'form-control', }),
                              )

    brand = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'brand',
                                                          'class': 'form-control', }),
                            max_length=20)

    brand = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'brand',
                                                          'class': 'form-control', }),
                            max_length=20)

    image = forms.ImageField(required=False)

    def add_product(self):
        nameproduct = self.cleaned_data['nameproduct']
        processor = self.cleaned_data['processor']
        screen_size = self.cleaned_data['screen_size']
        gpu = self.cleaned_data['gpu']
        memory = self.cleaned_data['memory']
        description = self.cleaned_data['description']
        cost = self.cleaned_data['cost']
        brand = Brand.objects.get(namebrand=self.cleaned_data['brand'])
        image = self.cleaned_data['image']

        try:
            if image:
                new_product = Product(nameproduct=nameproduct, processor=processor, screen_size=screen_size, gpu=gpu,
                                      memory=memory, description=description, cost=cost, brand=brand, img=image)
            else:
                new_product = Product(nameproduct=nameproduct, processor=processor, screen_size=screen_size, gpu=gpu,
                                      memory=memory, description=description, cost=cost, brand=brand)
            new_product.save()
            return new_product.id
        except BaseException as e:  # если вдруг что-то пошло не так
            print(e)
            return False

