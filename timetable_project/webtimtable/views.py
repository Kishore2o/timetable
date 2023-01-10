from django.shortcuts import render

# Create your views here.
def timetable(request):
    return render(request,'webtimtable/timetable.html')


def secmap(request):
    return render(request,'webtimtable/secmap.html')

def firstyearblock(request):
    return render(request,'wibetimtable/firstyearblock')