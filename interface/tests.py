from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import LeadGeneratorForm, SignupForm


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("interface:login")
        self.logout_url = reverse("interface:logout")
        self.signup_url = reverse("interface:signup")
        self.lead_generator_url = reverse("interface:lead_generator")

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

    def test_logout_view(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/logged_out.html")

    def test_signup_view(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_lead_generator_view(self):
        User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

        response = self.client.get(self.lead_generator_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interface/lead_generator.html")

        form_data = {
            "keywords": "Hotel, Gym",
            "location": "Lviv, Rivne",
            "leads_num": "1",
        }
        response = self.client.post(self.lead_generator_url, form_data)
        self.assertEqual(response.status_code, 302)

    def test_deploying_page(self):
        response = self.client.get(reverse("interface:deploying"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interface/deploying_page.html")

    def test_lead_generator_form(self):
        form = LeadGeneratorForm(
            data={
                "keywords": "Hotel, Gym",
                "location": "Lviv, Rivne",
                "leads_num": "1",
            }
        )
        self.assertTrue(form.is_valid())

    def test_signup_form(self):
        form = SignupForm(
            data={
                "email": "test@example.com",
                "username": "testuser",
                "password1": "testpassword",
                "password2": "testpassword",
            }
        )
        self.assertTrue(form.is_valid())
