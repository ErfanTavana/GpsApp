from django.contrib.auth.models import User
from django.db import models
from khayyam import JalaliDatetime  # یا استفاده از jdatetime
class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    latitude = models.FloatField(verbose_name='عرض جغرافیایی', blank=True, null=True)
    longitude = models.FloatField(verbose_name='طول جغرافیایی', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ و ساعت ثبت')
    timestamp_shamsi = models.CharField(max_length=20, blank=True, verbose_name='تاریخ و ساعت شمسی')
    speed = models.FloatField(verbose_name='سرعت', blank=True, null=True)  # جدید
    battery_level = models.FloatField(verbose_name='مقدار شارژ باتری', blank=True, null=True)  # جدید

    def save(self, *args, **kwargs):
        # تبدیل تاریخ میلادی به شمسی
        if self.timestamp:
            self.timestamp_shamsi = JalaliDatetime(self.timestamp).strftime('%Y/%m/%d %H:%M:%S')
        super(Location, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'مکان'
        verbose_name_plural = 'مکان‌ها'

    def __str__(self):
        return f"{self.user.username} - {self.latitude}, {self.longitude} at {self.timestamp_shamsi}, Speed: {self.speed}, Battery: {self.battery_level}"
