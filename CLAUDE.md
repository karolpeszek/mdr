# CLAUDE.md — jak pisać sprawozdania z I Pracowni Fizycznej

Repozytorium zawiera sprawozdania z I Pracowni Fizycznej (fizyka, UJ). Autor: Karol Peszek, grupa B.
Każde ćwiczenie ma nazwę kodową z serialu *Severance* (Allentown, Trinity, Cork, Molde…), a stopka
każdej strony ma logo Lumon. Ten plik opisuje styl i sposób pisania, wyciągnięte ze sprawozdań 1–9.
Najlepszym wzorcem jest **`9. Cork/cork.tex`** (wersja już po poprawkach prowadzącego).

---

## 1. Struktura katalogu i pliki

```
N. Nazwakodowa/
├── nazwakodowa.tex          # sprawozdanie (snake_case, np. st_pierre.tex, todos_santos.tex)
├── nazwakodowa.ipynb        # analiza danych w Pythonie
├── nazwakodowa_notebook.pdf # wyeksportowany notebook (opcjonalnie)
├── <kod ćwiczenia>.pdf      # skrypt/instrukcja do ćwiczenia, np. o8.pdf, m21.pdf, m22.pdf
├── lumon.pdf                # logo do stopki (kopiowane z poprzedniego ćwiczenia)
├── schema.jpg               # zdjęcie układu pomiarowego
├── *.csv                    # surowe dane pomiarowe
└── *.pdf                    # wykresy wygenerowane przez notebook i rysunki ze skryptu
```

- Nowe sprawozdanie zaczynaj od kopii `.template/template.tex` — nie zmieniaj preambuły
  (pakiety, marginesy 2,5 cm, stopka z `lumon.pdf`, `siunitx` z przecinkiem dziesiętnym).
- Uzupełnij makra: `\tytul` (pełna nazwa ze skryptu), `\codeword`, `\nrCwiczenia` (np. `O8`, `M21`,
  `E11`, `C4`), `\autor`, `\nrGrupy`, `\dataWykonania` (data pomiarów słownie, np. `3 czerwca 2026`).
- Treść teoretyczną, wzory, procedurę i oznaczenia bierz ze skryptu do ćwiczenia (PDF w katalogu).
- Pliki CSV: nagłówek w pierwszym wierszu, kolumna wielkości i obok jej niepewność,
  np. `theta,u_theta,I,u_I`. Kropka dziesiętna. Nazwy plików po angielsku, snake_case.
- Pliki pośrednie LaTeX (`.aux`, `.log`, `.fls`, `.fdb_latexmk`, `.out`, `.synctex.gz`) są w `.gitignore`.

## 2. Obowiązkowa struktura sprawozdania

Siedem sekcji, zawsze w tej kolejności i z tymi nazwami (jak w szablonie):

1. **Cel ćwiczenia** — jeden krótki akapit (3–5 zdań): co zbadano, co zmierzono, co wyznaczono.
   Czas przeszły, strona bezosobowa („W niniejszej pracy zbadano…”, „Wyznaczono…”).
2. **Wstęp teoretyczny** — podsekcje dla każdego zjawiska/prawa. Każdy wzór, z którego
   korzysta się później, jest tu numerowany i opisany. Rysunki ze skryptu z dopiskiem
   „Źródło:~\cite{skrypt}.” w podpisie. Na końcu, jeśli trzeba, podsekcja z przyjętymi stałymi
   i wartościami tablicowymi (ze źródłem).
3. **Opis układu pomiarowego** — zdjęcie układu (`schema.jpg`), lista przyrządów w `itemize`
   (każdy z dokładnością/rozdzielczością, jeśli ma znaczenie), krótki opis połączeń.
4. **Procedura pomiarowa** — co faktycznie zrobiono, krok po kroku, czas przeszły bezosobowy.
   Podsekcje odpowiadają kolejnym częściom ćwiczenia. Podawaj zakresy i kroki pomiarów
   („od $-90^{\circ}$ do $90^{\circ}$ co $5^{\circ}$, w okolicach ekstremów co $2^{\circ}$”).
5. **Wyniki pomiarów** — wyłącznie surowe dane: tabele i wykresy punktów z słupkami błędów,
   **bez dopasowań**. Na początku sekcji jedno zdanie z niepewnościami przyrządów
   („We wszystkich pomiarach niepewność odczytu kąta wynosi $u_\theta = 1^{\circ}$…”).
   Podsekcje w tej samej kolejności i z tymi samymi nazwami co w Procedurze.
6. **Opracowanie wyników** — metoda dopasowania, wzory na wielkości wyznaczane i ich
   niepewności (propagacja), tabele parametrów dopasowania, wykresy z dopasowaną krzywą,
   wyniki końcowe. Krótki komentarz liczbowy po każdym wyniku.
   Jeśli rachunek niepewności jest rozbudowany, można wydzielić osobną sekcję
   **Rachunek niepewności** przed Opracowaniem (jak w Todos Santos).
7. **Wnioski** — podsekcje odpowiadające częściom ćwiczenia (te same nazwy co wyżej).
   Przy krótkim ćwiczeniu dopuszczalny jeden ciągły tekst (St. Pierre, Coleman).

Na końcu `thebibliography` (patrz §8). Podsekcje w sekcjach 4, 5, 6 i 7 mają **równoległe nazwy**,
żeby czytelnik mógł iść jedną częścią ćwiczenia przez całe sprawozdanie.

## 3. Język i styl

- **Strona bezosobowa, czas przeszły**: „zmierzono”, „wyznaczono”, „dopasowano”, „zaobserwowano”,
  „przyjęto”. **Nie** pisz w 1. osobie („możemy”, „zrobimy”, „otrzymaliśmy”) — tak było tylko
  w pierwszym sprawozdaniu i zostało porzucone.
- Wstęp teoretyczny w czasie teraźniejszym („Polaryzator liniowy jest materiałem…”).
- Rzeczowo i konkretnie: każde zdanie oceniające ma liczbę („tło jest pomijalne:
  $a_3/(a_1+a_3) \approx 0{,}08\,\%$”). Unikaj ozdobników i przesadnych określeń
  („kategorycznie”, „niezwykle”, „doskonała zgodność”, „rzetelna wielkość”).
- Terminologia: **niepewność** (wielkość $u$) a **błąd** (rzeczywiste odchylenie, błąd systematyczny,
  źródło błędu). Nie mieszaj.
- Definiuj każdy symbol zaraz po wzorze: „gdzie $a_1$ --- amplituda, $a_2$ --- przesunięcie…”.
- Myślnik: `---` ze spacjami. Zakres liczbowy: `--` (np. `4{,}3--4{,}6`).
- Twarde spacje: `Rysunek~\ref{…}`, `Tabela~\ref{…}`, `wzór~\eqref{…}`, `\cite` poprzedzony `~`.
  Po jednoliterowych spójnikach/przyimkach (`w~`, `z~`, `i~`, `a~`, `o~`) też stawiaj `~`.
- Odwołania zawsze przez `\ref`/`\eqref` z etykietami (`fig:…`, `tab:…`, `eq:…`, `sec:…`) —
  nigdy „równanie (8)” wpisane ręcznie.
- Odwołania do rysunków i tabel w tekście: „Rysunek~\ref{…}”, „Tabela~\ref{…}”
  (wielką literą, w odpowiedniej formie: „na Rysunku”, „w Tabeli”).
- Przed oddaniem sprawdź literówki — w dotychczasowych sprawozdaniach zdarzały się
  („daleoka”, „metodoą”, „różynymi”, „nieidelaności”).

## 4. Liczby, jednostki, niepewności

- Przecinek dziesiętny w tekście: `0{,}195`. W `\SI`/`\num`/kolumnach `S` wpisuj kropkę —
  `siunitx` sam zamieni ją na przecinek.
- Jednostki przez `siunitx`: `\SI{578}{\nano\meter}`, `\SIrange{300}{700}{\nano\meter}`.
  Stopnie: `$45^{\circ}$`.
- Wynik zapisuj jako $(x \pm u)$ jednostka, np. `$(13{,}77\pm0{,}11)$~D`, albo
  `$e_\text{exp} = 0{,}195 \pm 0{,}012$`. Niepewność zaokrąglaj do 1–2 cyfr znaczących,
  wartość do tego samego miejsca dziesiętnego.
- Notacja niepewności: $u_x$ lub $u(x)$; niepewność wielkości złożonej $u(f)$.
  Odchylenie standardowe serii: $\sigma(t)$.
- Indeksy tekstowe przez `\text{}`: `e_\text{exp}`, `e_\text{teor}`, `\theta_\text{rel}`,
  `T_d^\text{exp}`.
- Jednostki w nagłówkach tabel w nawiasach kwadratowych: `{$I$ [mV]}`.
- Ta sama jednostka w CSV, w notebooku (etykiety osi) i w sprawozdaniu — sprawdź to
  (w Cork wykresy miały „mA”, a tekst „mV”).

## 5. Rachunek niepewności i analiza

- Niepewności przyrządów podawaj jawnie (lista w `itemize` albo zdanie na początku Wyników).
- Niepewność wielkości złożonych: **prawo propagacji niepewności** z pochodnymi cząstkowymi,
  wzór zapisany ogólnie i numerowany, np.
  $u(W) = \left|\frac{\partial W}{\partial a}\right| u(a)$.
  Kąty w propagacji wyrażaj w radianach i zaznacz to.
- Dopasowania: `scipy.optimize.curve_fit` z `sigma=u, absolute_sigma=True`, niepewności
  parametrów $u_{a_i} = \sqrt{C_{ii}}$ z macierzy kowariancji — napisz to w tekście.
  Przy regresji liniowej ważonej podaj wagi ($w_i = 1/\sigma_i^2$).
- Model dopasowania zapisz jako numerowany wzór z nazwanymi parametrami ($a_1, a_2, a_3$) i podaj
  fizyczne znaczenie każdego parametru.
- Gdy niepewności z dopasowania są nierealistycznie małe (np. przez zaniżone $u_I$),
  **powiedz to wprost** w opracowaniu/wnioskach i wyjaśnij dlaczego.
- Średnia ważona: $\bar{x} = \frac{\sum x_i/u_i^2}{\sum 1/u_i^2}$,
  $u(\bar{x}) = \left(\sum 1/u_i^2\right)^{-1/2}$.
- Odrzucenie serii/punktu: osobna (pod)sekcja lub akapit z uzasadnieniem
  (np. „Odrzucenie serii 4” w Trinity).
- Wskazuj **dominujące źródło niepewności**, najlepiej ilościowo
  („$u(B_2)$ odpowiada za ${\approx}92\%$ wariancji $u^2(J_X)$”).

## 6. Porównanie z teorią / wartością tablicową

- Kryterium zgodności: test $3\sigma$ — jawnie wypisany:
  $$\frac{|x - x_\text{tab}|}{u(x)} \approx 20{,}3 > 3$$
  Dla dwóch wyników doświadczalnych: $|x_1 - x_2|/\sqrt{u_1^2 + u_2^2}$.
- Sformułowania: „zgodne w granicach niepewności”, „różni się o ${\approx}4{,}7\sigma$, co jest
  statystycznie istotne”, „nie jest zgodne w granicach niepewności”.
- Wartość tablicowa zawsze ze źródłem (`\cite`).

## 7. Wnioski — jak je pisać

To najważniejsza i najczęściej poprawiana część. Zasady (m.in. z uwag prowadzącego do Cork):

1. Każda podsekcja zaczyna się od **wyniku końcowego z niepewnością** i porównania z teorią.
2. Jeśli wynik jest zgodny — powiedz to jednym zdaniem i dodaj, co to potwierdza.
3. Jeśli wynik **nie jest zgodny** — podaj **jedną, konkretną, fizycznie uzasadnioną przyczynę**,
   najlepiej wykazaną wzorem lub rachunkiem (np. w Cork: z $I(\varphi) = \tfrac{I_0}{2}\sin^2(2\varphi)$
   wynika, że ćwierćfalówkę ustawiono na złe ekstremum, więc światło pozostało liniowe).
   **Nie wyliczaj listy kilku spekulatywnych przyczyn** („po pierwsze… po drugie… po trzecie…,
   obie mogą działać jednocześnie”) — prowadzący to usunął i zastąpił jednym dowodem.
4. Przyczyny błędów mają być **specyficzne dla tego pomiaru** (co zaobserwowano w laboratorium:
   wahania miernika > 10 %, wylana woda, porysowane soczewki, offset fotokomórek wyliczony
   z wyrazu wolnego), a nie ogólniki („błąd ludzki”, „niedokładność przyrządów”).
5. Jeśli można, **oszacuj wielkość** efektu systematycznego (np. $\delta = -B_1/A_1 \approx 4{,}2$ cm).
6. Gdy wynik ilościowo zawodzi, ale jakościowo zjawisko widać — napisz to na końcu jednym zdaniem.
7. Bez wniosków ogólnikowych typu „ćwiczenie pozwoliło w pełni zrealizować cele”,
   „wynik jest zadowalający i świadczy o poprawności metodyki”.

## 8. Rysunki, tabele, bibliografia

**Rysunki**
- `\begin{figure}[H]` + `\centering`; szerokość `0.72`–`0.95\textwidth`
  (dane surowe ~`0.82`, dopasowania ~`0.72`).
- Wykresy jako PDF z notebooka (wektorowo); zdjęcie układu jako JPG.
- Podpis zdaniem pełnym: co jest na wykresie, co oznaczają linie i obszary, czym są słupki błędów
  („Słupki błędów odpowiadają niepewnościom $u_\theta = 1^{\circ}$ i $u_I = \SI{0{,}1}{mV}$.”).
  `\label` bezpośrednio po `\caption`.
- Dwa podobne wykresy obok siebie: `subfigure` po `0.48\textwidth`.
- Do każdego rysunku i tabeli musi być odwołanie w tekście przed nim.

**Tabele**
- `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), bez pionowych linii.
- `\caption` **nad** tabelą; w podpisie niepewności pomiarów, jeśli wspólne dla całej tabeli.
- Kolumny liczbowe typu `S[table-format=…]`; wartość ± niepewność jako dwie kolumny
  rozdzielone `@{\,$\pm$\,}`; nagłówek obejmujący obie `\multicolumn{2}{c}{…}`.
- Tekst w nagłówkach kolumn `S` w klamrach: `{$\theta$ [$^{\circ}$]}`.
- Szeroka tabela: `\footnotesize` lub `\resizebox{\textwidth}{!}{…}`.

**Bibliografia** — ręczna `thebibliography`, minimum skrypt:
```latex
\begin{thebibliography}{9}
\bibitem{skrypt}
    \textit{Skrypt do ćwiczeń laboratoryjnych z fizyki, I Pracownia Fizyczna}, ćwiczenie O8.
\end{thebibliography}
```
Źródła internetowe z `\url{…}` i `[dostęp: 8 kwietnia 2026]`.

## 9. Notebook (analiza w Pythonie)

- Biblioteki: `numpy`, `pandas`, `matplotlib`, `scipy.optimize.curve_fit`.
- Na początku:
  ```python
  plt.rcParams.update({'figure.dpi': 150, 'font.size': 11, 'axes.grid': True, 'grid.alpha': 0.3})
  ```
- Dane wczytywane z CSV (`pd.read_csv`), nigdy wpisywane ręcznie w kod.
- Dla każdej części: wykres surowy (`*_raw.pdf`, tylko `errorbar`) do sekcji Wyniki
  oraz wykres z dopasowaniem (`*.pdf`) do sekcji Opracowanie.
- `ax.errorbar(..., fmt='o', ms=4, capsize=3, label='dane pomiarowe')`, krzywa dopasowania `'-', lw=2`;
  `fig.tight_layout()`, `fig.savefig('nazwa.pdf')`.
- Opisy osi i legendy po polsku, z jednostkami w nawiasach kwadratowych: `'kąt analizatora θ [°]'`.
- Wypisuj wyniki z niepewnościami (`print(f"a1 = {a1:.3f} ± {u_a1:.3f}")`), żeby łatwo przenieść je do tabel.
- Liczby w `.tex` muszą zgadzać się z wynikami notebooka — po każdej zmianie analizy
  przegeneruj wykresy i zaktualizuj tabele i tekst.

## 10. Lista kontrolna przed oddaniem

- [ ] 7 sekcji w kolejności szablonu, równoległe podsekcje w Procedurze / Wynikach / Opracowaniu / Wnioskach
- [ ] Wyniki = tylko surowe dane; dopasowania dopiero w Opracowaniu
- [ ] Każdy wynik końcowy w formie $(x \pm u)$ z jednostką, sensownie zaokrąglony
- [ ] Wzory na niepewności wielkości złożonych wypisane
- [ ] Porównanie z teorią/tablicą testem $3\sigma$, wartość tablicowa ze źródłem
- [ ] Wnioski: jedna konkretna przyczyna rozbieżności, uzasadniona fizycznie, bez list spekulacji
- [ ] Wszystkie rysunki/tabele mają podpis, etykietę i odwołanie w tekście
- [ ] Jednostki spójne między CSV, wykresami i tekstem
- [ ] Brak 1. osoby, brak literówek, `~` przed `\ref`/`\cite`
- [ ] Dokument kompiluje się bez ostrzeżeń o niezdefiniowanych referencjach
