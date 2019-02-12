# Lab 0: Getting ready!

V rámci tohto predmetu budeme programovať v jazyku Python a pri vytváraní a trénovaní modelov hlbokého učenia budeme používať framework TensorFlow a knižnicu Keras. Tento návod vám pomôže pri nastavení programovacieho prostredia.

## Krok 1: Inštalácia Pythonu
Na tomto predmete budeme používať Python verziu 3.6, ktorú si môžete stiahnuť z [web stránky jazyka](https://www.python.org/downloads/release/python-368/). My ale odporúčame nainštalovať inú distribúciu Pythonu [Anaconda](https://www.anaconda.com), ktorá obsahuje niekoľko predinštalovaných knižníc pre prácu s údajmi a strojové učenie.

### Krok 1.1: Nainštalujte si Anacondu
Anaconda je voľne dostupná z [tejto stránky](https://www.anaconda.com/distribution/). Dajte si pozor, aby ste nainštalovali verziu 3.

### Krok 1.2: Preinštalujte si Anacondu na verziu 3.6
Anaconda je dostupná iba pre najnovšie verzie Pythonu, teda v čase písania tohto návodu je to 3.7. Anacondu ale viete preinštalovať na ľubovoľnú verziu. Spustite príkazový riadok Anacondy (Anaconda Prompt) s admin právami a zadajte príkaz

```conda install python=3.6```

Skontrolujte si, či sa staršia verzia Pythonu nainštalovala správne pomocou príkazu:

```python --version```

V príkazovom riadku Anacondy by sa vám mal zobraziť výpis tvaru:

```Python 3.6.X :: Anaconda, Inc.```

### Krok 1.3: Aktualizujte vybrané knižnice
Cez príkazový riadok Anacondy aktualizujte niektoré knižnice, ktoré budeme používať počas semestra:

```
python -m pip install numpy --upgrade
python -m pip install matplotlib --upgrade
python -m pip install scipy --upgrade
```

## Krok 2: Inštalácia TensorFlow a Keras
TensorFlow a Keras ako aj ďalšie knižnice nainštalujete pomocou `pip`. Do príkazového riadku Anacondy zadajte príkazy:

```
python -m pip install tensorflow
python -m pip install keras
```

Knižnice `TensorFlow` a `Keras` sa nainštalujú automaticky spolu s potrebnými dependencies. V prípade problémov sa obráťte na stránky [TensorFlow](https://www.tensorflow.org/install/pip) a [Keras](https://keras.io/#installation).

## Krok 3: Skontrolujte si inštaláciu
V príkazovom riadku spusťte Python zadaním príkazu `python` a následne skúsťte naimportovať nainštalované knižnice:

```
import tensorflow
import keras
```

Prvý import môže potrvať niekoľko sekúnd. Ak počas importu sa vyskytnú problémy s niektorou knižnicou, potrebujete si ju aktualizovať podľa príkazov uvedených v bode 1.3.

Python zastavíte zadaním príkazu `exit()`.