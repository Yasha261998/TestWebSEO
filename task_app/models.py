from django.db import models


class Items(models.Model):
    """Товары"""

    id = models.BigAutoField(primary_key=True)
    name = models.CharField("Название товара", max_length=60)
    price = models.FloatField("Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Employees(models.Model):
    """Продавцы"""

    id = models.BigAutoField(primary_key=True)
    name = models.CharField("Имя продавца", max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Sales(models.Model):
    """Продажи"""

    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)   # товар
    price_sale = models.FloatField("Цена")
    number = models.PositiveIntegerField("Количество")
    dt_sale = models.DateTimeField("Дата и время покупки", auto_now_add=True, blank=True)
    seller = models.ForeignKey(Employees, on_delete=models.CASCADE)     # продавец
