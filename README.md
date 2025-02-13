# BST Visualizer

<h2>Opis Projektu</h2>

<p>
BST Visualizer to aplikacja do wizualizacji drzew binarnych poszukiwań (Binary Search Trees, BST). Projekt umożliwia:
</p>
<ul>
  <li>Dodawanie węzłów do drzewa.</li>
  <li>Usuwanie węzłów.</li>
  <li>Znajdowanie węzłów w drzewie.</li>
  <li>Edytowanie wartości węzłów.</li>
  <li>Wyświetlanie statystyk drzewa.</li>
  <li>Usuwanie całego drzewa.</li>
  <li>Równoważenie drzewa.</li>
</ul>
<p>
Interfejs użytkownika został zbudowany przy użyciu biblioteki <code>tkinter</code> w Pythonie.
</p>

---

<h2>Wymagania</h2>

<ul>
  <li>Python 3.10 lub nowszy</li>
  <li>Biblioteka <code>tkinter</code></li>
</ul>

---

<h2>Instalacja</h2>

<ol>
  <li>Sklonuj repozytorium:
    <pre><code>git clone https://github.com/OlaMotorola/BSTVisualizer.git</code></pre>
  </li>
  <li>Przejdź do katalogu projektu:
    <pre><code>cd BSTVisualizer</code></pre>
  </li>
  <li>Uruchom aplikację:
    <pre><code>python gui.py</code></pre>
  </li>
</ol>

---

<h2>Funkcjonalności</h2>

<h3>1. Dodawanie Węzłów</h3>
<p>Użyj pola wejściowego, aby wpisać wartość liczbową, a następnie kliknij przycisk <b>Dodaj węzeł</b>. Węzeł zostanie dodany do drzewa i wyświetlony w oknie graficznym.</p>

<h3>2. Znajdowanie Węzłów</h3>
<p>Wprowadź wartość węzła w polu wejściowym i kliknij <b>Znajdź węzeł</b>. Jeśli węzeł istnieje, zostanie wyróżniony.</p>

<h3>3. Usuwanie Węzłów</h3>
<p>Podaj wartość węzła, który chcesz usunąć, w polu wejściowym i kliknij <b>Usuń węzeł</b>. Węzeł zostanie usunięty, a drzewo automatycznie zaktualizowane.</p>

<h3>4. Edycja Węzła</h3>
<p>Podaj starą wartość węzła oraz nową wartość, a następnie kliknij <b>Edytuj węzeł</b>. Węzeł zostanie zaktualizowany.</p>

<h3>5. Statystyki Drzewa</h3>
<p>Kliknij przycisk <b>Statystyki</b>, aby zobaczyć:</p>
<ul>
  <li>Liczbę węzłów</li>
  <li>Wysokość drzewa</li>
  <li>Minimalną i maksymalną wartość w drzewie</li>
</ul>

<h3>6. Usuwanie Całego Drzewa</h3>
<p>Kliknij <b>Wyczyść drzewo</b>, aby usunąć wszystkie węzły.</p>

<h3>7. Równoważenie Drzewa</h3>
<p>Kliknij <b>Zrównoważ drzewo</b>, aby zrównoważyć drzewo.</p>

---

<h2>Algorytm równoważenia drzewa</h2>
<p>Algorytm wykorzystuje podejście polegające na zamianie drzewa BST na listę węzłów w porządku in-order, a następnie budowie z tej listy zrównoważonego drzewa. Proces składa się z dwóch głównych kroków:</p>
<ol>
  <li>
    Zamiana drzewa na listę węzłów w porządku in-order
    <ul>
      <li>Metoda _flatten_to_spine tworzy listę węzłów w porządku in-order (lewe poddrzewo → korzeń → prawe poddrzewo).</li>
      <li>W tym celu _inorder_collect przechodzi rekurencyjnie przez wszystkie węzły drzewa, dodając je do listy.</li>
    </ul>
    <p>Efektem jest lista węzłów, które są posortowane według wartości kluczy.</p>
  </li>
  <li> Budowa zrównoważonego drzewa
    <ul>
      <li>Metoda _build_balanced_tree buduje zrównoważone drzewo z listy węzłów.</li>
      <li>Działa w sposób rekurencyjny:
        <ol>
          <li>Znajduje środkowy element listy (który stanie się korzeniem poddrzewa).</li>
          <li>Rekurencyjnie tworzy lewe i prawe poddrzewo, dzieląc listę na dwie części:
            <ul>
              <li>Elementy po lewej stronie środka stają się lewym poddrzewem.</li>
              <li>Elementy po prawej stronie środka stają się prawym poddrzewem.</li>
            </ul>
          </li>
          <li>Ustawia odniesienia parent dla każdego węzła.</li>
        </ol>
      </li>
    </ul>
    <p>Dzięki temu procesowi drzewo staje się zrównoważone, ponieważ węzły są rozkładane równomiernie po obu stronach każdego poddrzewa.</p>
  </li>
</ol>

---

<h2>Struktura Plików</h2>

<ul>
  <li><code>bst.py</code>: Implementacja drzewa BST wraz z funkcjami dodawania, usuwania, równoważenia i statystyk.</li>
  <li><code>gui.py</code>: Interfejs użytkownika oparty na <code>tkinter</code>.</li>
  <li><code>node.py</code>: Klasa <code>Node</code>, definiująca strukturę węzła drzewa z atrybutami: dane, lewy, prawy i rodzic.</li>   
  <li><code>README.md</code>: Dokumentacja projektu.</li>
</ul>

---

<h2>Przykładowy Widok</h2>

<p>
Po uruchomieniu aplikacji pojawia się okno z:
</p>
<ul>
  <li>Polem tekstowym do wprowadzania danych.</li>
  <li>Przyciskiem do każdej funkcjonalności.</li>
  <li>Obszarem graficznym wyświetlającym drzewo.</li>
</ul>

---

<h2>Autor</h2>

<b>Aleksandra Zając</b>


