from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

class RawProductForm(forms.Form):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Type your title here"}))
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
								attrs={
									"placeholder": "Type your title here",
									"class": "new-class-name two",
									"id": "my-id-for-textarea",
									"rows": 10,
									"cols": 50
								}
							)
						)
	price = forms.CharField(initial=199.99)