from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from core import models

import func.functions as fnc
import func.generators as gen


class AdminSiteTests(TestCase):
    """
    Testowanie strony admina
    """

    def setUp(self):

        self.client = Client()
        self.model = models.User
        self.admin_user = get_user_model().objects.create_superuser(
            **gen.user_payload_gen().__next__()
            )
        self.client.force_login(self.admin_user)
        self.user = fnc.create_user(
            **gen.user_payload_gen().__next__()
            )
        self.instances_fields = fnc.get_model_payload_instances_fields(
            self.model_obj_payload_gen().__next__()
        )

    def model_obj_payload_gen(self):
        """
        Generates various model object payloads (must to be customized)
        """

        while True:

            payload = gen.user_payload_gen().__next__()

            yield payload

    def test_users_listed(self):
        """
        Testuje listowanie userow
        """

        url = reverse(
            'admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """
        Testuje strone edycji
        """

        url = reverse(
            'admin:core_user_change', 
            args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)

    def test_create_user_page(self):
        """
        Testuje strone kreowania usera
        """

        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)