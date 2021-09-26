from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import UserInfo, User, Ingestion
from datetime import datetime
from .computer import norm_man, norm_woman


# Регистрация
def signup(request):
    error = ''
    if request.method == 'POST':
        # Получение данных
        username = request.POST['username']
        password = request.POST['password']
        weight = int(request.POST['weight'])
        height = int(request.POST['height'])
        birthdate = request.POST['birthdate']
        gender = request.POST['gender']
        datetime_birth = datetime.fromisoformat(birthdate)
        norm = norm_man(weight, height, datetime_birth) if gender == 'М' else norm_woman(weight, height, datetime_birth)
        try:
            if len(password) >= 8:
                # Создание пользователя
                user = User.objects.create_user(username=username, password=password)
                UserInfo.objects.create(user=user, weight=weight, height=height, birthdate=birthdate, gender=gender,
                                        norm=norm)
                login(request, user)
                return redirect('/')
            else:
                error = 'Пароль слишком маленький'
        except Exception:
            error = 'Такой пользователь уже существует'
    return render(request, "main/signup.html", {'error': error})


# Авторизация
def login_user(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = 'Ошибка в имени или пароле'
    return render(request, "main/login.html", {'error': error})


# Выход
def logout_user(request):
    logout(request)
    return redirect('/login')


# Главная страница
@login_required(login_url='/login')
def index(request):
    if request.method == 'POST':
        food = request.POST['food']
        calories = request.POST['calories']
        Ingestion.objects.create(user=request.user, food=food, calories=calories)

    # Сумма всех калорий за сегодня
    calories = 0
    ingestions = list(request.user.ingestion_set.filter(date=datetime.now()))
    for ingestion in ingestions:
        calories += ingestion.calories
    return render(request, "main/index.html", {'user': request.user, 'calories': calories, 'ingestions': ingestions,
                                               'difference': request.user.userinfo.norm - calories})


# Профиль
@login_required(login_url='/login')
def profile(request):
    saved = False
    if request.method == 'POST':
        weight = int(request.POST['weight'])
        height = int(request.POST['height'])
        userinfo = User.objects.get(pk=request.user.pk).userinfo
        userinfo.weight = weight
        userinfo.height = height
        userinfo.norm = norm_man(weight, height, userinfo.birthdate) if userinfo.gender == 'М' else norm_woman(weight, height, userinfo.birthdate)
        userinfo.save()
        saved = True
    # Получение информации о пользователе
    info = request.user.userinfo
    return render(request, "main/profile.html", {'info': info, 'saved': saved, 'username': request.user.username})


# История
@login_required(login_url='/login')
def history(request):
    # Объединение данных в группы по дате
    groups = {}
    for ingestion in request.user.ingestion_set.order_by('-date'):
        date = ingestion.date.strftime('%d-%m-%Y')
        if date in groups.keys():
            groups[date][1].append(ingestion)
            groups[date][0] += ingestion.calories
        else:
            groups[date] = [ingestion.calories, [ingestion]]
    return render(request, "main/history.html", {'groups': groups})
