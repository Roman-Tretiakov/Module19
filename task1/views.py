from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.defaultfilters import title

from task1.forms import UserRegister
from task1.models import Buyer, Game

DEFAULT_BALANCE = 100.00
MIN_AGE = 18


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page'] = 'Главная страница'
        context['main'] = 'Главная'
        context['shop'] = 'Магазин'
        context['basket'] = 'Корзина'
        context['games'] = 'Игры'
        context['game_list'] = Game.objects.all()
        context['buy_button'] = 'Купить'
        context['back_button'] = 'Вернуться обратно'
        context['basket_message'] = 'Извините, ваша корзина пуста!'
        return context


class Main(BaseView):
    template_name = 'task1/main_page_template.html'


class Shop(BaseView):
    template_name = 'task1/shop_template.html'


class Basket(BaseView):
    template_name = 'task1/basket_template.html'


def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            info['username'] = username = form.cleaned_data['username']
            info['password'] = password = form.cleaned_data['password']
            info['repeat_password'] = repeat_password = form.cleaned_data['repeat_password']
            info['age'] = age = form.cleaned_data['age']

            user_names = Buyer.objects.all().values_list('name', flat=True)

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают!'
            elif int(age) < MIN_AGE:
                info['error'] = f'Вам должно быть {18} или больше!'
            elif title(username) in user_names:
                info['error'] = 'Пользователь уже существует!'
            else:
                Buyer.objects.create(name=title(username), balance=DEFAULT_BALANCE, age=int(age))
                info['success_message'] = f'Приветствуем,  {username}!'

            return render(request, 'task1/registration_page.html', context=info)
    else:
        form = UserRegister(request.POST)
        return render(request, 'task1/registration_page.html', {'form': form})
