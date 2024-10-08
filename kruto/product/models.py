from django.db import models
from django.conf import settings
from twilio.rest import Client
from django.core.mail import send_mail

class Category(models.Model):
    title = models.CharField(max_length=256)
    
    def __str__(self):
        return self.title


class Material(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, max_length=256, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='materials/', blank=True, null=True)
    desc1 = models.TextField(null=True)
    desc2 = models.TextField(null=True)
    desc3 = models.TextField(null=True)

    def __str__(self):
        return f"{self.name} - {self.description} - {self.category} - {self.image}"

class Callback(models.Model):
    name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=13)
    text = models.TextField()
    material = models.ForeignKey(Material, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} - {self.material}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        subject = 'Новая заявка'
        message = f"""
        Name: {self.name}
        Phone Number: {self.phone_number}
        Message: {self.text}
        Material: {self.material}
        """
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        whatsapp_message = f"Новая заявка\n\nName: {self.name}\nPhone: {self.phone_number}\nMessage: {self.text}\nMaterial: {self.material}"

        client.messages.create(
            body=whatsapp_message,
            from_=settings.TWILIO_WHATSAPP_FROM,
            to=settings.TWILIO_WHATSAPP_TO
        )


class PriceList(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название прайс-листа')
    file = models.FileField(upload_to='price_lists/', verbose_name='Файл прайс-листа')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    def __str__(self):
        return self.name
    

class Companies(models.Model):
    photo = models.ImageField(upload_to="companies/")
    link = models.CharField(max_length=10000, null=True)
    
    def __str__(self):
        return str(self.pk)
