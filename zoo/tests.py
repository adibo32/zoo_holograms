from django.test import TestCase
from django.urls import reverse
from .models import Hologram

class HologramTests(TestCase):

    def setUp(self):
        self.hologram = Hologram.objects.create(
            name="Test",
            gewicht="100kg",
            superkraft="Fly",
            ausgestorben_seit="2024-01-01"
        )

    def test_add_hologram(self):
        response = self.client.post(reverse('add_hologram'), {
            'name': 'Neues Test',
            'gewicht': '200kg',
            'superkraft': 'Fliegen',
            'ausgestorben_seit': '2023-01-01'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Hologram.objects.filter(name='Neues Test').exists())

    def test_edit_hologram(self):
        response = self.client.post(reverse('edit_hologram', args=[self.hologram.id]), {
            'name': 'Bearbeitetes Hologramm',
            'gewicht': '150kg',
            'superkraft': 'schwimmen',
            'ausgestorben_seit': '2022-01-01'
        })
        self.assertEqual(response.status_code, 302)
        self.hologram.refresh_from_db()
        self.assertEqual(self.hologram.name, 'Bearbeitetes Hologramm')
        self.assertEqual(self.hologram.gewicht, '150kg')
        self.assertEqual(self.hologram.superkraft, 'schwimmen')

    def test_delete_hologram(self):
        response = self.client.post(reverse('delete_hologram', args=[self.hologram.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Hologram.objects.filter(id=self.hologram.id).exists())
    
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.hologram.name)

