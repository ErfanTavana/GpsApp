from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'longitude', 'timestamp_shamsi', 'timestamp', 'speed', 'battery_level')  # نمایش فیلدهای جدید
    search_fields = ('user__username', 'latitude', 'longitude', 'speed', 'battery_level')  # قابلیت جستجو براساس فیلدهای جدید
    list_filter = ('user', 'timestamp', 'speed', 'battery_level')  # فیلتر براساس فیلدهای جدید
    ordering = ('-timestamp',)  # مرتب‌سازی پیش‌فرض براساس جدیدترین زمان ثبت
    readonly_fields = ('timestamp_shamsi',)  # فیلد فقط خواندنی برای تاریخ شمسی
