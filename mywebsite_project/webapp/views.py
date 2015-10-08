from django.shortcuts import render

def index(request):
    return render(request, 'webapp/index.html', {});

def pkmnrevo(request):
	return render(request, 'webapp/pkmnrevo.html', {});

def arkanoid(request):
	return render(request, 'webapp/arkanoid.html', {});

def scrabble(request):
	return render(request, 'webapp/scrabble.html', {});

def tichu(request):
	return render(request, 'webapp/tichu.html', {});

def pokyellow(request):
	return render(request, 'webapp/pokyellow.html', {});