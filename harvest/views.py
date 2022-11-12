from datetime import datetime

from django.views.generic import TemplateView

from .models import CoffeeOriginCountry


class CoffeeFromCountryView(TemplateView):
    template_name = "harvest/coffee-from-country.html"
    COFFEE_TRANSPORT_DELAY = 2  # months

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valid_countries'] = self.which_coffee_to_buy()
        return context

    def _current_month(self):
        return datetime.today().month

    def which_coffee_to_buy(self):
        harvest_month = self._current_month() - self.COFFEE_TRANSPORT_DELAY
        valid_countries = CoffeeOriginCountry.objects.filter(start_date__month__gte=harvest_month,
                                                             end_date__month__lte=harvest_month)
        return valid_countries
