from django.db import models
from django.utils.translation import gettext as _


class AdType(models.Model):
    name = models.CharField(_("Ad type"), max_length=50)

    def __str__(self):
        return self.name



class Condition(models.Model):
    name = models.CharField(_("Condition"), max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.PROTECT)
    ISBN = models.CharField(_("ISBN"), max_length=13)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_("Category"), max_length=50)

    def __str__(self):
        return self.name


class PriceType(models.Model):
    name = models.CharField(_("Price type"), max_length=50)

    def __str__(self):
        return self.name


class Price(models.Model):
    price_type = models.ForeignKey(PriceType, on_delete=models.PROTECT)
    current_price = models.FloatField(_("Current Price"))
    original_price = models.FloatField(_("Original Price"))

    def __str__(self):
        return f'current:{self.current_price},original:{self.original_price}'


class Ad(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), max_length=1000)
    ad_type = models.ForeignKey(AdType, on_delete=models.PROTECT)
    book = models.OneToOneField(Book, on_delete=models.PROTECT)
    price = models.OneToOneField(Price, on_delete=models.PROTECT)
    pictures = models.ImageField(upload_to="ad_images", blank=True)

    def __str__(self):
        return self.name
