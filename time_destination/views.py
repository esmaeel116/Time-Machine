from django.http import HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from .forms import TimeDestinationForm
from .models import TimeDestination
# Create your views here.
def time_destination_insert(request):
    if request.method == 'POST':
        form = TimeDestinationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TimeDestinationForm

    context = {'form': form}
    return render(request, 'time_destination/destination_insertion.html', context)

def time_destination_list(request):
    time_destination = TimeDestination.objects.all()
    context = {'time_destination': time_destination}
    return render(request, 'time_destination/destination_list.html', context)

def edit_time_destination(request, id):
    obj = get_object_or_404(TimeDestination, id=id)
    if request.method == 'GET':
        form = TimeDestinationForm(instance=obj)

    else:
        form = TimeDestinationForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/time_destination_list/')
    context = {'form': form}
    return render(request, 'time_destination/edit_time_destination.html', context)

def delete_time_destination(request, id):
    obj =get_object_or_404(TimeDestination, id=id)
    obj.delete()
    return HttpResponseRedirect('/time_destination_list/')
