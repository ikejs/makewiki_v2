import unittest

from django.test import TestCase, Client
from django.contrib.auth.models import User
from wiki.models import Page


class WikiTestCase(TestCase):
    def test_true_is_true(self):
        """" Tests that True equals True """
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """ Test the slug generated when saving a Page """
        # Create a user for this test.
        user = User()
        user.save()

        # Create and save Page to DB.
        page = Page(title="My Test Page", content="test", author=user)
        page.save()

        self.assertEqual(page.slug, 'my-test-page')


class PageListViewTests(TestCase):
    """ Tests that the homepage works. """
    def test_multiple_pages(self):
        # Create a user & pages for this test.
        user = User.objects.create()

        Page.objects.create(title="My Test Page", content="test", author=user)
        Page.objects.create(title="Another Test Page", content="testing again", author=user)

        # Make a GET request
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

class WikiDetailsPageTest(TestCase):
    def test_wiki_details_page_load(self):
            user = User.objects.create()
            page = Page.objects.create(title="My Test Page", content="test", author=user)

            response = self.client.get('/my-test-page/')
            response_page = response.context['page']

            self.assertEqual(response.status_code, 200)
            self.assertEqual(page.title, response_page.title)
