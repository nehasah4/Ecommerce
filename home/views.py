from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

from .models import *
# Create your views here.

class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()


class HomeView(BaseView):
    def get(self, request):
        self.views
        self.views['subcategories'] = SubCategory.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['reviews'] = Review.objects.all()
        self.views['new_products'] = Product.objects.filter(labels='new')
        self.views['hot_products'] = Product.objects.filter(labels='hot')
        self.views['sale_products'] = Product.objects.filter(labels='sale')

        return render(request, 'index.html', self.views)

class CategoryView(BaseView):

    def get(self,request,slug):
        ids = Category.objects.get(slug = slug).id
        self.views['cat_products'] = Product.objects.filter(category_id = ids)
        return render(request,'category.html',self.views)


class BrandView(BaseView):

    def get(self,request,slug):
        ids = Brand.objects.get(slug = slug).id
        self.views['brand_products'] = Product.objects.filter(brand_id = ids)
        return render(request,'brand.html', not self.views)



class SearchView(BaseView):

    def get(self,request):
        query = request.GET.get('query')
        if query =="":
            return redirect('/')
        else:
            self.views['search_product'] = Product.objects.filter(description__icontains = query)
        return render(request,'search.html',self.views)


class ProductDetailView(BaseView):

    def get(self,request,slug):
        self.views['product_detail'] = Product.objects.filter(slug = slug)
        subcat_id = Product.objects.get(slug = slug).subcategory.id
        products_id = Product.objects.get(slug = slug).id
        self.views['product_images'] = ProductImage.objects.filter(product_id = products_id)
        self.views['related_product'] = Product.objects.filter(subcategory_id = subcat_id)

        return render(request, 'product-detail.html', self.views)


def product_review(request,slug):
    return redirect(f'/product_detail/{slug}')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        username = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'The username is already taken')
                return redirect('/signup')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'The email is already used')
                return redirect('/signup')
            else:
                date = User.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    password = password,
                )
                data.save()
        else:
            messages.error(request, 'The password does not match!')
            return redirect('/signup')

    return render(request,'signup.html')