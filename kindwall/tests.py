import os
from pathlib import Path
from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command
from django.contrib.staticfiles import storage, finders
from django.conf import settings
from .models import Message


class WallViewTests(TestCase):
    def test_wall_renders_and_shows_static_links(self):
        response = self.client.get(reverse('wall'))
        self.assertEqual(response.status_code, 200)
        # Base template deve referenciar os CSS estáticos
        content = response.content.decode()
        self.assertIn('kindwall/css/base', content)
        self.assertIn('kindwall/css/header', content)
        self.assertIn('kindwall/css/footer', content)
        self.assertIn('kindwall/css/wall', content)

    def test_create_message_and_like_flow(self):
        payload = {'author_name': 'Tester', 'text': 'Olá, mundo gentil!'}
        post_resp = self.client.post(reverse('wall'), payload, follow=True)
        self.assertEqual(post_resp.status_code, 200)
        self.assertEqual(Message.objects.count(), 1)

        message = Message.objects.first()
        self.assertEqual(message.likes, 0)

        like_resp = self.client.get(reverse('like_message', args=[message.id]), follow=True)
        self.assertEqual(like_resp.status_code, 200)

        message.refresh_from_db()
        self.assertEqual(message.likes, 1)


class StaticAssetsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Gera manifest e arquivos comprimidos para o storage de produção.
        call_command('collectstatic', verbosity=0, interactive=False)

    def test_css_file_is_discoverable(self):
        css_path = 'kindwall/css/base.css'

        # Finder precisa localizar o arquivo fonte.
        source_path = finders.find(css_path)
        self.assertIsNotNone(source_path)
        self.assertTrue(os.path.exists(source_path))

        # Storage de estáticos em produção deve gerar URL hashada e existir no disco.
        url = storage.staticfiles_storage.url(css_path)
        self.assertIn('/static/kindwall/css/base', url)
        self.assertTrue(storage.staticfiles_storage.exists(css_path))

        relative = url[len(settings.STATIC_URL):] if url.startswith(settings.STATIC_URL) else url.lstrip('/')
        hashed_file = Path(settings.STATIC_ROOT) / relative.replace('/', os.sep)
        self.assertTrue(hashed_file.exists())

# Create your tests here.
