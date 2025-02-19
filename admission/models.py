from django.db import models

class Admission(models.Model):
    ClassName = models.CharField(max_length=255, verbose_name="জামাতের নাম")
    class_level = models.CharField(max_length=100, verbose_name="শ্রেণীর স্তর", null=True, blank=True)
    form_fee = models.IntegerField(default=100, verbose_name="ফরম ফি")
    new_admission_fee = models.IntegerField(verbose_name="নতুন ভর্তি ফি")
    old_admission_fee = models.IntegerField(verbose_name="পুরাতন ভর্তি ফি")
    new_total_fee = models.IntegerField(verbose_name="নতুন সর্বমোট ফি")
    old_total_fee = models.IntegerField(verbose_name="পুরাতন সর্বমোট ফি")
    additional_fee = models.IntegerField(null=True, blank=True, verbose_name="অতিরিক্ত ফি")
    monthly_fee = models.IntegerField(null=True, blank=True, verbose_name="মাসিক বেতন")
    
    admission_start_date = models.CharField(verbose_name="ভর্তি শুরুর তারিখ")
    admission_end_date = models.CharField(verbose_name="ভর্তি শেষের তারিখ")
    required_documents = models.TextField(verbose_name="ভর্তির জন্য প্রয়োজনীয় কাগজপত্র")
    admission_notes = models.TextField(null=True, blank=True, verbose_name="ভর্তি সংক্রান্ত নির্দেশনা")
    seat_availability = models.BooleanField(default=True, verbose_name="আসন ফাঁকা আছে কিনা")
    
    admission_created = models.DateTimeField(auto_now_add=True)
    admission_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ClassName
    
    class Meta:
        verbose_name_plural = 'ভর্তি'
