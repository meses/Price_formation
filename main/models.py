from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара'),
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена исходная')
    final_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name='Цена с учётом надбавок',
                                      **NULLABLE)

    def __str__(self):
        return f"{self.name} - {self.final_price}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
