from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

import func.functions as fnc
import func.generators as gen


# USER
class UserTests(TestCase):

    
    def setUp(self):
        self.model = models.User
        self.user = fnc.create_user(**gen.user_payload_gen().__next__())
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


    def test_if_created_success(self):
        """
        Testy tworzenia usera 
        
        """

        p_gen = self.model_obj_payload_gen()
        payload_0 = p_gen.__next__()
        created = get_user_model().objects.create_user(**payload_0)

        payload = payload_0
        password = payload.pop('password', None)

        created_with_instances = fnc.model_to_dict_with_instances(
            instance=created, 
            fields=payload, 
            instance_fields=self.instances_fields
        )

        self.assertTrue(created)
        self.assertEqual(created_with_instances, payload_0)
        self.assertTrue(created.check_password(password))


    def test_new_email_normalized(self):
        """
        Testuje czy login jest konwertowany na male litery w bazie
        """

        p_gen = self.model_obj_payload_gen()
        payload_0 = p_gen.__next__()
        created = get_user_model().objects.create_user(**payload_0)

        self.assertEqual(created.email,payload_0['email'].lower())


    def test_new_user_invaid_email(self):
        """
        Testuje czy wyrzuci wyjatek w momencie wsprowadzenia zlego 
        loginu (nie emailowego)
        """

        with self.assertRaises(ValueError):

            get_user_model().objects.create_user(
                None, gen.login_gen().__next__()
                )


    def test_create_new_superuser(self):
        """
        Test utworzenia superusera
        """

        p_gen = self.model_obj_payload_gen()
        payload_0 = p_gen.__next__()
        created = get_user_model().objects.create_superuser(**payload_0)

        self.assertTrue(created.is_superuser)
        self.assertTrue(created.is_staff)


    def test_create_new_staffuser(self):
        """
        Test tworzenia stuff usera
        """

        p_gen = self.model_obj_payload_gen()
        payload_0 = p_gen.__next__()
        created = get_user_model().objects.create_staff(**payload_0)

        self.assertTrue(created.is_staff)

