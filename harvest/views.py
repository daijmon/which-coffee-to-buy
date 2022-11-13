from datetime import datetime

from django.db.models import F
from django.views.generic import TemplateView

from .models import CoffeeOriginCountry


class CoffeeFromCountryView(TemplateView):
    template_name = "harvest/coffee-from-country.html"
    COFFEE_TRANSPORT_DELAY = 3  # months

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.harvest_month = self._current_month() - self.COFFEE_TRANSPORT_DELAY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["valid_countries"] = self.which_coffee_to_buy()
        return context

    @staticmethod
    def _current_month() -> int:
        return datetime.today().month

    def which_coffee_to_buy(self) -> list[CoffeeOriginCountry]:
        all_countries_annotated = CoffeeOriginCountry.objects.all().annotate(
            middle_of_harvest=((F("start_date__month") + F("end_date__month")) / 2)
        )
        valid_countries = all_countries_annotated.filter(
            middle_of_harvest__lte=self.harvest_month,
            end_date__month__gte=self.harvest_month,
        )
        return self._sort_countries_based_on_harvest(valid_countries)

    def _sort_countries_based_on_harvest(
        self, countries: list[CoffeeOriginCountry]
    ) -> list[CoffeeOriginCountry]:
        return sorted(countries, key=self._middle_harvest_closeness)

    def _middle_harvest_closeness(self, country: CoffeeOriginCountry) -> int:
        middle_of_harvest = (country.start_date.month + country.end_date.month) // 2
        return abs(self.harvest_month - middle_of_harvest)
