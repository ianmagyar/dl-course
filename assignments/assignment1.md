# Zadanie 1 - Replikácia článku

Úlohou v prvom zadaní je replikovať postup popísaný vo vybranom vedeckom článku a overiť výsledky popísané autormi článku. Naučíte sa pritom vytvárať a natrénovať modely na základe inštrukcií, a získate skúsenosti so správnou metodológiou vyhodnocovania modelov. Tiež si vyskúšate prácu s reálnymi dátami, a získate lepšiu predstavu o správnom štruktúrovaní vedeckých článkov a o dokumentácii výskumnej činnosti, čo budete potrebovať pri vypracovaní druhého zadania.

Na vypracovaní zadania budete pracovať vo dvojiciach tak, aby vami vybraný článok porovnával niekoľko rôznych metód a úlohu rozdelíte tak, aby obaja členovia tímu získali skúsenosti s celým postupom.

Primárnym cieľom zadania je, aby ste výsledky zreplikovali jedna ku jednej, teda aby ste použili rovnaké dáta, modely a postup pri trénovaní. Overíte tak správnosť uvedených výsledkov v článku. Ak vám vychádzajú iné výsledky ako tie uvedené v článku, musíte ich vedieť odôvodniť, prípadne poukázať na chyby, ktoré urobili autori článku. Alternatívne, ak napríklad dáta použité v článku nie sú dostupné alebo nemôžete použiť rovnakú architektúru ako pôvodní autori, ale trváte na replikácii daného článku, tak môžete prispôsobiť dáta alebo topológiu, v takomto prípade však musíte porovnať a vysvetliť rozdielnosť pôvodných a vašich výsledkov.

## Články

Článok, ktorý zreplikujete, si môžete vybrať sami, avšak nemal by byť starší ako 3 roky (rok vydania minimálne 2022). Dbajte aj na to, aby ste si vybrali článok s datasetom a modelom, ktorý budete môcť natrénovať a vyhodnotiť s dostupnou infraštruktúrou. Druhou podmienkou je, aby článok nemal zverejnené kódy priamo od autorov. Ak neviete nájsť vhodný článok, môžete si nechať poradiť od vyučujúcich predmetu.

## Pracovný plán

Prácu počas semestra si môžete naplánovať ľubovoľne, avšak musíte dodržať nasledovné míľniky:

 1. výber článku - do konca druhého týždňa semestra (6. 10.)
 2. zhrnutie článku vlastnými slovami (musí byť iný ako abstrakt) - do konca piateho týždňa semestra (27. 10.)
 3. finálne odovzdanie - deviaty týždeň semestra (24. 11.)
 4. obhajoba zadania - do konca semestra (20. 12.)

## Odovzdanie

Vypracovanie zadania zahŕňa dve odovzdávky v piatom a deviatom týždni semestra.

Prvá odovzdávka je krátky report pozostávajúci zo zhrnutia článku vlastnými slovami, kde reflektujete na obsah článku. Očakávanie je, že do vypracovania tohto zhrnutia budete mať detailný prehľad o riešenom probléme, o použitej metóde a vykonaných experimentoch. Práve preto, ak sú nejasnosti súvisiace s článkom, mali by ste si ich ozrejmiť do odovzdania tohto reportu. Zhrnutie musí obsahovať informácie:

 * riešený problém;
 * použitá metóda a jej porovnanie so state of the artom - identifikujte jedinečnosť riešenia, v čom sa riešenie líši od ostatných metód použitých pre riešenie problému; nespoliehajte sa iba na referencie uvedené v článku, pridajte novšie články, alebo iné články súvisiace s problematikou;
 * použité dáta;
 * metodológia trénovania a vykonaných experimentov - popíšte vlastné postrehy, či sa vám zdá byť metodológia vhodná, alebo rovno ste zbadali nevhodný postup;
 * očakávané ťažkosti pri replikácii výsledkov a ako ich plánujete riešiť.

Finálne odovzdanie vypracovaného riešenia je do konca deviateho týždňa semestra, a obsahuje:

 * `requirements` súbor so všetkými potrebnými knižnicami a nástrojmi potrebné pre spustenie experimentov (iba relevantné knižnice, nie automaticky generovaný zoznam z virtuálneho prostredia);
 * python skripty pre spustenie experimentov, definíciu modelov a spracovanie dát; musia to byť súbory `.py` a nie jupyter notebooky;
 * dokumentácia k vlastnému riešeniu:
    * krátky abstrakt;
    * vymenovanie zmien v metodológii oproti pôvodnému článku;
    * prehľad dosiahnutých výsledkov a ich porovnanie s pôvodnými výsledkami - tu rozdiely musíte aj okomentovať, a musíte vykonať aj krížovú validáciu na vlastných výsledkoch.

## Hodnotenie

Za zadanie môžete získať celkovo 10 bodov a to nasledovne:

 * krátky report v 5. týždni - 1 bod,
 * dokumentácia a výsledky - 5 bodov,
 * obhajoba a diskusia riešenia - 4 body.

V rámci obhajoby (10. - 13. týždeň) musíte preukázať pochopenie použitej metódy a vedieť okomentovať a obhájiť dosiahnuté výsledky.
