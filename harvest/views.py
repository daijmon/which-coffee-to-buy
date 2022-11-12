from django.views.generic import TemplateView

from .models import CoffeeOriginCountry


class CoffeeFromCountryView(TemplateView):
    template_name = "harvest/coffee-from-country.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_countries = CoffeeOriginCountry.objects.all()
        context['all_countries'] = all_countries
        return context
