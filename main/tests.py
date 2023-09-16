from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Item
from users.models import User
from django.urls import reverse


class ItemTestCase(APITestCase):

    def setUp(self):
        # Создание тестового пользователя
        self.user = User.objects.create_user(
            email='testuser',
            password='testpass',
            is_staff=True
        )
        self.client.force_authenticate(user=self.user)

        # Создание тестовой привычки
        self.item = Item.objects.create(
            price=20.30,
            final_price=25.50
        )

    def test_create_item(self):
        """ Тест для создания продукта с ценой """
        url = reverse('main:item-create')
        data = {
            'name': 'test',
            'price': 11.25
        }

        response = self.client.post(url, data, format='json')  # Отправка POST-запроса для создания записи

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)  # Проверка, что код статуса ответа равен 201 (Создан)
        self.assertEqual(Item.objects.count(), 2)  # Проверка, что был создан объект

    def test_list_items(self):
        """ Тест для получения списка продуктов """
        url = reverse('main:item-list')  # Получение URL для получения списка продуктов с ценой
        self.client.force_authenticate(user=self.user)  # Аутентификация пользователя
        response = self.client.get(url)  # Отправка GET-запроса на получение списка продуктов с ценой
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа (должен быть 200 OK)
        self.assertEqual(len(response.data), 4)  # Проверка количества объектов в ответе (должно быть 4)

    def test_retrieve_item(self):
        """ Тест для получения информации о конкретной цене """
        url = reverse('main:item-detail', args=[self.item.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['final_price'], '25.50')  # Проверка финальной цены

    def test_destroy_habit(self):
        """ Тест для удаления записи """
        url = reverse('main:item-delete', args=[self.item.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(),
                         0)  # Проверяем, что количество объектов модели Item равно 0,
        # что означает успешное удаление записи.


