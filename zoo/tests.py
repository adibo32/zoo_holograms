from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Hologram

class HologramViewTests(TestCase):

    def setUp(self):
        Hologram.objects.create(name="test1", gewicht="100kg", superkraft="Fly", ausgestorben_seit="2020-12-01")
        Hologram.objects.create(name="test2", gewicht="200kg", superkraft="Invisible", ausgestorben_seit="2019-11-01")
        
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, "test1")
        self.assertContains(response, "test2")
        
    def test_index_view_with_filter(self):
        response = self.client.get(reverse('index') + '?filter=test1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test1")
        self.assertNotContains(response, "test2")

    def test_index_view_with_sorting(self):
        response = self.client.get(reverse('index') + '?sort=name&order=desc')
        self.assertEqual(response.status_code, 200)
        holograms = response.context['holograms']
        self.assertEqual(holograms.first().name, "test2")

    def test_add_hologram_view(self):
        response = self.client.post(reverse('add_hologram'), {
            'name': 'test3',
            'gewicht': '150kg',
            'superkraft': 'Super Strength',
            'ausgestorben_seit': '2021-05-05',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Hologram.objects.filter(name="test3").exists())

    def test_edit_hologram_view(self):
        hologram = Hologram.objects.first()
        response = self.client.post(reverse('edit_hologram', args=[hologram.id]), {
            'name': 'test1_edited',
            'gewicht': hologram.gewicht,
            'superkraft': hologram.superkraft,
            'ausgestorben_seit': hologram.ausgestorben_seit,
        })
        self.assertEqual(response.status_code, 302)
        hologram.refresh_from_db()
        self.assertEqual(hologram.name, 'test1_edited')

    def test_delete_hologram_view(self):
        hologram = Hologram.objects.first()
        response = self.client.post(reverse('delete_hologram', args=[hologram.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Hologram.objects.filter(id=hologram.id).exists())

