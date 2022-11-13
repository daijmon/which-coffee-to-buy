from django.views.generic import TemplateView

from .coffee_harvest import CoffeeHarvest


class CoffeeFromCountryView(TemplateView):
    template_name = "harvest/coffee-from-country.html"
    COFFEE_TRANSPORT_DELAY = 3  # months

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coffe_harvest = CoffeeHarvest()
        context["valid_countries"] = coffe_harvest.which_coffee_to_buy()
        return context
