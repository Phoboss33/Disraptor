from django.shortcuts import render
from .forms import RespondentForm
# Create your views here.
def testform(request):
    form = RespondentForm()
    return render(request, 'lending/testform.html', {'form': form})