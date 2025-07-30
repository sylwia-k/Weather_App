#Weather API App

##Opis projektu
Jest to prosty program napisany w Pythonie z wykorzystaniem biblioteki PyQt5 i aplikacji Qt Designer, który umożliwia wpisanie nazwy miasta i wyświetlenie aktualnej pogody w podanym miejscu za pomocą OpenWeatherMap API.

##Funkcjonalność:
- Okno startowe z polem tekstowym do wpisania nazwy miasta
- Przycisk do pobrania danych pogodowych
- Drugie okno wyświetlające:
- Temperaturę w Kelwinach
- Opis warunków pogodowych (np. "clear sky")
- Wilgotność powietrza (%)
- Obsługa błędów — jeśli miasto nie zostanie znalezione, pokazuje się okno z informacją o błędzie
- Okno aplikacji bez standardowej ramki, z zaokrąglonymi rogami i przezroczystym tłem (wizualny efekt)
  
##Struktura projektu
- welcome.py — główne okno, gdzie użytkownik wpisuje miasto i uruchamia pobieranie pogody
- weather_ui.py — okno wyświetlające dane pogodowe (temperatura, wilgotność, opis)
- notfound.py — okno wyświetlające komunikat o błędzie, gdy miasto nie istnieje lub API zwróci błąd

##Jak działa program?
- Użytkownik wpisuje nazwę miasta i kliknie przycisk "Check".
- Program wysyła zapytanie do OpenWeatherMap z podaną nazwą miasta.
- Jeśli miasto zostanie znalezione, otwiera się nowe okno z wyświetlonymi danymi pogodowymi.
- W przypadku błędu (np. złej nazwy miasta) pokazuje się okno z informacją o błędzie.
- Aplikacja jest zaprojektowana tak, aby okna miały niestandardowy wygląd (bez ramki, z przezroczystością i zaokrąglonymi rogami).
