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

Kampania posiada dwa pełne poziomy które można przejść przez przetrwanie wszystkich fal, fale składają się z kilku przeciwników na każdą. Kolejną falę odpalamy przyciskiem na górze ekranu, gdy 
nie ma żadnych przeciwników na planszy (tzn. przed pierwszą falą, lub gdy przeciwnicy dotarli do końca ścieżki, lub gdy zostali wyeliminowani). 

Tryb Nieskończoność opiera się na ciągłej nawałnicy wrogów ze zwiększającym się poziomem trudności, przez stopniowy wzrost życia przeciwników i coraz częstsze pojawianie się przeciwników. Celem w tym trybie jest jak najdłuższe przetrwanie licznik czasu, jaki wytrzymaliśmy odpierając przeciwników i możliwość porównywania go z najlepszym wynikiem. 

Gracz przegrywa jak straci 10 punktów życia, które są odbierane gdy przeciwnicy docierają na koniec planszy.

W celu przyspieszenia gry można przytrzymać klawisz spacji na klawiaturze.

By powstrzymać przeciwników gracz ma do dyspozycji 4 wieże. Pierwsza jest szybkostrzelna i nie zadaje zbyt wielu obrażeń, druga zadaje więcej obrażeń ale potrzebuje czasu by wystrzelic poraz kolejny,
trzecia to "moździerz" który potrzebuje długiego czasu ładowania ale atakuje przeciwników w niewielkim obszarze, a nie tylko pojedyńczych wrogów, ma on też największy zasięg. Czwarta wieża to mina która aktywuje się, kiedy przeciwnik na nią stanie i wybucha. Stawiana ona może być tylko na środku ścieżki. Pozostałe wieże stawiamy poza ścieżką.

Wieże można postawić po przez naciśnięcie kafelka planszy, który podświetli się na czerwono.

Każda z wież ma swój zasięg rażenia widoczny po postawieniu. 

Wieże mogą być jeden raz ulepszone, działa to przez kliknięcie na wieżę, którą chcemy ulepszyć i naciśnięciu przycisku "Ulepszenie". Ulepszenie zwiększa niektóre parametry zależnie od wieży.

Wieże są kupowane za pieniądze eliminacji przeciwników na planszy. 