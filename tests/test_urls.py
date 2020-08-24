from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import home
from events.views import events
from gallery.views import gallery
from members.views import team


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, home)

    # def test_sponsers_url_resolves(self):
    #     url = reverse("sponsers")
    #     self.assertEquals(resolve(url).func, sponser)

    def test_events_url_resolves(self):
        url = reverse("events")
        self.assertEquals(resolve(url).func, events)

    def test_gallery_url_resolves(self):
        url = reverse("gallery")
        self.assertEquals(resolve(url).func, gallery)

    # def test_alumni_url_resolves(self):
    #     url = reverse("alumni")
    #     self.assertEquals(resolve(url).func, alumni)

    def test_team_url_resolves(self):
        url = reverse("about")
        self.assertEquals(resolve(url).func, team)
