from django.shortcuts import render, redirect
from django import forms
from .models import Result, Establishment
from .forms import NewResultForm

# Create your views here.

def homepage(request):
    # establishments = Establishment.objects.all()
    # return render(request, 'restroom_rater/homepage.html', {'establishments': establishments})

    if request.method == 'POST':
        form = NewResultForm(request.POST)
        try:
            result = form.save(commit=False)
            if form.is_valid():
                # result.save()
                # results = Result.objects.all()
                new_result_form = NewResultForm()
                return render(request, 'restroom_rater/homepage.html', {'results': results, 'new_result_form': new_result_form})
            else:
                return redirect('restroom_rater/homepage.html')
        except (ValueError):
            print('whoops.')
            return homeFormReroute(request)

def homeFormReroute(request):
    results = Result.object.all()
    newresult_form = NewResultForm()
    return render(request, 'restroom_rater/homepage.html', {'results': results, 'new_result_form': new_result_form})