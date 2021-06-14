from django.forms import ModelForm
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import CountryRestriction


class IndexView(generic.ListView):
    template_name = 'travel/index.html'
    context_object_name = 'countryrestriction_list'

    def get_queryset(self):
        """Return the list of restrictions by origin."""
        return CountryRestriction.objects.order_by('restricting_country', 'name_text')


def detail(request, countryrestriction_id):
    instance = get_object_or_404(CountryRestriction, pk=countryrestriction_id)

    class CountryRestrictionForm(ModelForm):
        class Meta:
            model = CountryRestriction
            fields = [f.name for f in CountryRestriction._meta.get_fields()]
    form = CountryRestrictionForm(instance=instance)
    return render(
        request,
        'travel/detail.html',
        {'form': form}
    )
