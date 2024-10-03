from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Player
from .forms import PlayerForm
from django.core.paginator import Paginator



# View pro zobrazení seznamu hráčů
def players_list(request):
    # Získání vyhledávacího dotazu z GET parametru
    query = request.GET.get('q')

    # Načtení všech hráčů, nebo filtrovaných hráčů na základě vyhledávání
    if query:
        player_list = Player.objects.filter(first_name__icontains=query) | Player.objects.filter(
            last_name__icontains=query)
    else:
        player_list = Player.objects.all()


    paginator = Paginator(player_list, 10)  # 10 hráčů na stránku

    page_number = request.GET.get('page')  # Získání čísla stránky z GET parametru
    players = paginator.get_page(page_number)  # Načtení hráčů pro danou stránku

    return render(request, 'players/players_list.html', {'players': players, 'query': query})

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('players')  # Přesměrování na seznam hráčů
    else:
        form = PlayerForm()
    return render(request, 'players/add_player.html', {'form': form})

# View pro zobrazení detailu hráče
def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)  # Načtení hráče podle primárního klíče (ID)
    return render(request, 'players/player_detail.html', {'player': player})

# View pro smazání hráče
def delete_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('players')  # Přesměrování na seznam hráčů
    return render(request, 'players/delete_player.html', {'player': player})

# players/views.py
def update_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_detail', pk=player.pk)  # Přesměrování na detail hráče
    else:
        form = PlayerForm(instance=player)
    return render(request, 'players/update_player.html', {'form': form, 'player': player})







