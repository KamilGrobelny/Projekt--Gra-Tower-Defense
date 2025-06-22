# INSTRUKCJA OBSŁUGI:

## Wymagane biblioteki:
- Pygame
- Os
- Math
- Random
- Unittest


## Instrukcja uruchomienia:

Po pobraniu plików należy uruchomić plik main.py, który wyświetli menu wyboru trybu gry.

## Instrukcja użytkowania:

Obecnie gra posiada 2 tryby: "Kampania" oraz  "Nieskończoność".

Kampania posiada dwa pełne poziomy które można ukończyć przez przetrwanie wszystkich fal, fale składają się z kilku przeciwników na każdą. Kolejną falę rozpoczynamy przyciskiem na górze ekranu, gdy 
nie ma żadnych przeciwników na planszy (tzn. przed pierwszą falą, lub gdy przeciwnicy dotarli do końca ścieżki, lub gdy zostali wyeliminowani). 

Tryb Nieskończoność opiera się na ciągłej nawałnicy wrogów z rosnącym poziomem trudności. Ilość życia przeciwników, oraz ich liczba, stopniowo się zwiększają. Celem w tym trybie jest jak najdłuższe przetrwanie. Wynik mierzony jest czasem, przez jaki udało się odeprzeć przeciwników, a uzyskany rezultat można porównać z najlepszym wynikiem.

Gracz przegrywa, gdy straci 10 punktów życia, które są odbierane gdy przeciwnicy docierają na koniec planszy.

W celu przyspieszenia gry można przytrzymać klawisz spacji na klawiaturze.

By powstrzymać przeciwników gracz ma do dyspozycji 4 wieże. Pierwsza jest szybkostrzelna i nie zadaje zbyt wielu obrażeń, druga zadaje więcej obrażeń ale potrzebuje czasu by wystrzelić poraz kolejny,
trzecia to "moździerz" który potrzebuje długiego czasu ładowania ale atakuje przeciwników w niewielkim obszarze, a nie tylko pojedyńczych wrogów, ma on też największy zasięg. Czwarta wieża to mina która aktywuje się, kiedy przeciwnik na nią stanie i wybucha. Stawiana ona może być tylko na środku ścieżki. Pozostałe wieże stawiamy poza ścieżką. Każda z wież ma swój zasięg rażenia widoczny po postawieniu.

Wieże można postawić przez naciśnięcie kafelka planszy, który podświetli się na czerwono, oraz naciśnięciu odpowiedniego przycisku na ekranie. 

Wieże mogą być jeden raz ulepszone, działa to przez kliknięcie na wieżę, którą chcemy ulepszyć i naciśnięciu przycisku "Ulepszenie". Ulepszenie zwiększa niektóre parametry zależnie od wieży.

Wieże są kupowane za pieniądze eliminacji przeciwników na planszy.

Testy jednostkowe znajdują się w pliku test.py.