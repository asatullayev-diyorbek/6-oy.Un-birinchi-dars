from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Brand, Car
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        brand_id = request.GET.get('brand')
        brands = Brand.objects.all()

        if brand_id:
            try:
                cars = Car.objects.filter(brand=brand_id)
                brand = Brand.objects.get(pk=brand_id)
            except:
                messages.error(request, 'Brend mavjud emas!')
                return redirect('home')
        else:
            cars = Car.objects.all()
            brand = None
        context = {
            'title': "Bosh sahifa",
            'brand': brand,
            'brands': brands,
            'cars': cars,
        }
        return render(request, 'home.html', context)


class AboutView(View):
    def get(self, request):
        context = {
            'title': "Biz haqimizda",
        }
        return render(request, 'about.html')


@login_required
def car_detail(request, id):
    try:
        car = Car.objects.get(pk=id)
    except:
        messages.error(request, "Mashina topilmadi")
        return redirect('home')
    return render(request, 'car_detail.html', {'car': car})


def user_login(request):
    if request.user.is_authenticated:
        messages.warning(request, "Siz tizimga allaqachon kirib bo'lgansiz")
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
            return redirect('home')
        else:
            messages.error(request, "Login yoki parol noto'g'ri!")
            return redirect('login')
    else:
        return render(request, 'login.html', {'title': "Login sahifasi"})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')



def user_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Parollar mos kelmaydi!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bunday foydalanuvchi mavjud!")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name)
        user.email = username  # Username sifatida emailni saqlaymiz
        user.save()
        login(request, user)
        messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
        return redirect('home')
    else:
        return render(request, 'register.html', {'title': "Ro'yxatdan o'tish"})

