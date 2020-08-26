from django.test import TestCase, Client
from django.urls import reverse


class TestView(TestCase):
    def setup(self):
        self.client = Client()

    def test_home_GET(self):
        response = self.client.get(reverse("home"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "main/home.html")

    # def test_sponser_GET(self):
    #     response = self.client.get(reverse("sponsers"))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "main/sponsers.html")

    def test_events_GET(self):
        response = self.client.get(reverse("events"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "events/events.html")

    def test_gallery_GET(self):
        response = self.client.get(reverse("gallery"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "gallery/gallery.html")

    # def test_alumni_GET(self):
    #     response = self.client.get(reverse("alumni"))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "members/alumni.html")

    def test_team_GET(self):
        response = self.client.get(reverse("about"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "members/about.html")
