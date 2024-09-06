from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Location

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Location


@api_view(["POST"])
def SaveUserLocationView(request):
    data = request.data
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    speed = data.get('speed')
    battery_level = data.get('battery_level')
    user = request.user

    # اعتبارسنجی ورودی‌ها
    if latitude is None or longitude is None:
        return Response(
            {"message": "مختصات مکانی الزامی هستند.", "data": None},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        latitude = float(latitude)
        longitude = float(longitude)
        if speed is not None:
            speed = float(speed)
        if battery_level is not None:
            battery_level = float(battery_level)
    except ValueError:
        return Response(
            {"message": "مقادیر ورودی معتبر نیستند.", "data": None},
            status=status.HTTP_400_BAD_REQUEST
        )

    # ایجاد یک رکورد مکان جدید برای کاربر
    location = Location.objects.create(
        user=user,
        latitude=latitude,
        longitude=longitude,
        speed=speed,
        battery_level=battery_level
    )

    if location:
        return Response(
            {"message": "مکان با موفقیت ذخیره شد.",
             "data": {
                 "latitude": location.latitude,
                 "longitude": location.longitude,
                 "speed": location.speed,
                 "battery_level": location.battery_level
             }},
            status=status.HTTP_201_CREATED
        )
    else:
        return Response(
            {"message": "مشکلی در ذخیره مکان کاربر وجود دارد.", "data": None},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):
    """
    احراز هویت کاربر و نمایش فرم یا پیام مناسب در صورت اعتبارسنجی صحیح.
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # اعتبارسنجی ورودی‌ها
        if not username or not password:
            return render(request, 'location/login.html', {
                'error': "نام کاربری و رمز عبور الزامی هستند."
            })

        # احراز هویت کاربر
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                # ورود کاربر (لاگین)
                login(request, user)

                # هدایت به صفحه‌ی مورد نظر بعد از ورود موفق
                return redirect('home')  # 'home' نام URL مقصد است
            else:
                return render(request, 'location/login.html', {
                    'error': "Account is disabled."
                })
        else:
            return render(request, 'location/login.html', {
                'error': "The username or password is incorrect."
            })

    # اگر درخواست GET بود، فرم لاگین را نمایش می‌دهد
    return render(request, 'location/login.html')


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login_view_name')
    locations = Location.objects.all()
    return render(request, 'location/home.html', {'locations': locations})
