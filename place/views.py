from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from place.models import Place
from django.core.urlresolvers import reverse_lazy


# Create your views here.

class PlaceList(ListView):
    model = Place


class PlaceCreate(CreateView):
    model = Place
    success_url = reverse_lazy('place_list')
    fields = ['room_number', 'white_board', 'black_board', 'projector', 'start_date', 'duration', 'num_of_persons']

class PlaceUpdate(UpdateView):
    model = Place
    success_url = reverse_lazy('place_list')
    fields = ['room_number', 'white_board', 'black_board', 'projector', 'start_date', 'duration', 'num_of_persons']

class PlaceDelete(DeleteView):
    model = Place
    success_url = reverse_lazy('place_list')

# Create your views here.
