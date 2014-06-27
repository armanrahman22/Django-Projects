from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponseServerError, HttpResponse
from django.views import generic
from django.utils import timezone
from django.template import RequestContext
from polls.models import Choice, Poll, PollingLocation
import json


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def Display(request):
    poll_list = Poll.objects.all().order_by('-pub_date')
    context = {'poll_list': poll_list}
    return render(request, 'polls/phikaps2015areawesome.html', context)


def delete_location(request):
    if request.method == 'GET':
        l_id = request.GET['location_id']
        p_id = request.GET['poll_id']
        p = get_object_or_404(Poll, pk=p_id)
    if l_id:
        del_loc = p.loclist.get(pk=l_id)
        del_loc.delete()
    HttpResponseRedirect(p.get_absolute_url())

def vote(request):
    context = RequestContext(request)
    c_id = None
    if request.method == 'GET':
        c_id = request.GET['choice_id']
        p_id = request.GET['poll_id']
        p = get_object_or_404(Poll, pk=p_id)
    likes = 0
    if c_id:
        selected_choice = p.choice_set.get(pk=c_id)
        likes = selected_choice.votes + 1
        selected_choice.votes = likes
        selected_choice.save()
    return HttpResponse(likes)
