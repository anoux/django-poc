from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
	title 		= forms.CharField(label='', 
					widget=forms.TextInput(attrs={"placeholder": "Type your title here"}))
	email = forms.EmailField()
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
								attrs={
									"placeholder": "Describe your product",
									"class": "new-class-name two",
									"id": "my-id-for-textarea",
									"rows": 10,
									"cols": 50
								}
							)
						)
	price = forms.CharField(initial=0)
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		#if statement --> in this way (putting return title at the end) I can specify multiple validatinos
		if not "Osiris" in title:
			raise forms.ValidationError("This is not a valid title")
		return title

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		#if statement --> in this way (putting return title at the end) I can specify multiple validatinos
		if email.endswith("edu"):
			raise forms.ValidationEror("This is not a valid email")
		return email

class RawProductForm(forms.Form):
	title 		= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Type your title here"}))
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