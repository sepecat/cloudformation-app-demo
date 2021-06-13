from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Country, CountryRestriction


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


class ResultsView(generic.DetailView):
    model = Country
    template_name = 'travel/results.html'


def vote(request, question_id):
    question = get_object_or_404(Country, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, CountryRestriction.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'travel/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('travel:results', args=(question.id,)))
