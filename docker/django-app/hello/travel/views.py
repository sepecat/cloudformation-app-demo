from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Country, CountryRestriction


class IndexView(generic.ListView):
    template_name = 'travel/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Country.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Country
    template_name = 'travel/detail.html'


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
