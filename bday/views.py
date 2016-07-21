from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def happy_bday(request):
    return render(request, 'bday.html')


@require_GET
def wishes(request):
    return render(request, 'wishes.html', {'wish': '.... да бъдеш много щастлива, здрава, прекрасна, обичана, все така упорита, постоянна, борбена и мотивирана!', 'link': 'more'})


@require_GET
def more(request):
    return render(request, 'wishes.html', {'wish': 'Много успехи в личен и професионален план - да станеш шеф на някоя гоооляма IT компания (10000 пъти по-голяма от SAP :D), да обиколиш света, да покориш много върхове (и в буквалния смисъл), да имаш много имения, вили, хеликоптери, самолети... и куп други материални придобивки, но и най-важното - да си заобиколена от близки хора, с които да прекарваш прекрасни моменти! ', 'link': 'we'})


@require_GET
def we(request):
    return render(request, 'we.html', {'wish': "Бъди щастлива!"})
