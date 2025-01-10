from django.shortcuts import render, get_object_or_404
from .models import TimeTraveler
from .forms import  TimeTravelerForm
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def time_traveler_insert(request):
    if request.method == 'POST':
        form = TimeTravelerForm(request.POST, request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TimeTravelerForm
    context = {'form': form}
    return render(request, 'time_traveler/traveler_insertion.html', context)

def time_traveler_list(request):
    time_traveler = TimeTraveler.objects.all()
    context = {'time_traveler': time_traveler}
    return render(request, 'time_traveler/traveler_list.html', context)


def edit_time_traveler(request, id):
    obj = get_object_or_404(TimeTraveler, id=id)
    if request.method == 'GET':
        form = TimeTravelerForm(instance=obj)

    else:
        form = TimeTravelerForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/time_traveler_list/')
    context = {'form': form}
    return render(request, 'time_traveler/edit_time_traveler.html', context)

def delete_time_traveler(request, id):
    obj = get_object_or_404(TimeTraveler, id=id)
    obj.delete()
    return HttpResponseRedirect('/time_traveler_list/')

def detail_time_traveler(request, id):
    traveler = get_object_or_404(TimeTraveler, id=id)
    context = {'traveler': traveler}
    return render(request, 'time_traveler/traveler_detail.html', context)
