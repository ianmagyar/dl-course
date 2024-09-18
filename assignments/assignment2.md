# Zadanie 2

V rámci cvičení získate prehľad o rôznych metódach využívaných v hlbokom učení ako aj o metodológii a praktikách, ktoré slúžia na vylepšenie výkonu modelov. Druhé zadanie vám poskytne príležitosť využiť tieto poznatky pri riešení reálneho problému. Na zadaní pracujú trojice. Polovicu bodov (20) získate do zápočtu, kým ďalších 20 bodov sa ráta ako praktická časť skúšky. Na vylepšení výsledkov teda môžete pracovať aj po ukončení semestra. Očakávanie je, že pri odovzdaní budete mať publikovateľné výsledky, ktoré môžu byť prospešné aj pre širšiu vedeckú komunitu.

## Téma projektu

V rámci zadania navrhujete tému sami, odporúčame však vybrať si problematiku, ktorá vás zaujíma a máte motiváciu ju riešiť, na druhej strane však predstavuje aj výzvu, aby ste pri jej riešení získali skúsenosti a nové vedomosti. Projekt môže byť **aplikačný**, kde preskúmate možnosti využitia hlbokého učenia pri riešení praktického problému, alebo **výskumný**, kde sa zameráte na návrh nových alebo vylepšenie existujúcich metód hlbokého učenia pre vyriešenie štandardného problému.

Pri výbere témy vychádzajte buď z vlastných záujmov, alebo nájdite oblasť hlbokého učenia, ktorá vás zaujme a chceli by ste ju lepšie preskúmať. Keďže na zadaní budete pracovať celý semester a časť skúškového obdobia, je kritické, aby ste robili na niečom, čo vás baví. Ak popri škole už pracujete, môžete sa inšpirovať aj problémami, ktoré riešite v práci, a nájsť možnosti využitia hlbokého učenia pri ich riešení. V takomto prípade si však dávajte pozor na prípadné citlivé dáta: keďže existuje možnosť publikovania vašich výsledkov, aj dáta musia byť verejne dostupné alebo zverejniteľné (ak napríklad v práci máte dataset, ktorý nemôžete použiť, skúste nájsť obdobné verejné dáta).

**Ako semestrálny projekt nemôžete použiť riešenie vypracované v rámci predmetu Tímový projekt.** Ak ale viete navrhnúť rozšírenie tamojšieho riešenia na očakávanej úrovni zložitosti, takéto riešenie možné je, prekonzultujte to však s vyučujúcimi.

### Ako si navrhnúť tému?

Ak hľadáte inšpiráciu, môžete si naštudovať články vydané na špičkových konferenciách, ako napr. [ICML](https://icml.cc/) alebo [NeurIPS](https://nips.cc/). Štúdia literatúry vám tiež dá lepšiu predstavu o tom, ako by mala vyzerať dokumentácia vašej práce. Ak už máte vytypovanú približnú problematiku, môžete urobiť širší rešerš pomocou kľúčových slov napríklad na [Google Scholari](http://scholar.google.com/). Pri návrhu témy je tiež kľúčovým krokom nájsť dáta, keďže ich vlastnosti značne ovplyvnia vaše ďalšie metodologické rozhodnutia. Ak dáta nie sú dostupné a musíte si vytvoriť vlastný dataset, rátajte s tým, že to môže byť zdĺhavý proces a ďalšiu prácu na projekte si naplánujte podľa toho. Vývoj modelu a vykonanie experimentov bude stále očakávaným výstupom bez ohľadu na to, koľko času potrebujete na prípravu údajov.

Ďalšie otázky, ktoré potrebujete brať do úvahy:

 * **výpočtová sila** - na internete nájdete niekoľko dostupných služieb s vyšším výpočtovým výkonom a v prípade potreby vám vieme poskytnúť aj školský hardvér na finálne alebo skoro finálne experimenty (nebudete mať možnosť každý jeden pokus testovať na našich serveroch). Projekt, ktorý vyžaduje niekoľkomesačné trénovanie na klustroch špičkových grafických kariet asi nebude vhodný pre tento predmet.
 * **dáta** - aj keď vytvorenie vlastného datasetu je zdĺhavý proces, ktorý vás uberie o cenný čas, neodporúčame ani druhý extrém, kde budete pracovať iba s úplne pripravenými dátami. V ideálnom prípade by ste mali použiť dostupný dataset, ktorý však potrebujete predspracovať, rozšíriť, augmentovať alebo iným spôsobom upraviť. Tak sa naučíte najviac aj o práce s dátami, ktorá je kritickou súčasťou vývoja riešení hlbokého učenia.
 * **pridaná hodnota vs replikácia výsledkov** - vzhľadom na to, že vaše výsledky by mali byť publikovateľné, je jasné, že potrebujete preukázať vlastnú tvorbu, teda niečo, čo ešte nikto pred vami neurobil. Práve preto nie je vhodné, aby ste v rámci zadania iba zreplikovali výsledky existujúcich článkov (na to máme osobitné zadanie). Samozrejme to neznamená, že by ste nemohli vychádzať z dostupnej literatúry, ale vašu prácu musíte jednoznačne odlíšiť od existujúceho stavu riešenia problematiky.

Ak počas výberu a návrhu témy budete mať akékoľvek ďalšie otázky, obráťte sa na vyučujúcich.

## Očakávané výstupy a pracovný plán

Na projekte pracuje trojica študentov. Práca musí byť zdokumentovaná priebežne vo forme git repozitáru, ktorý zazdieľate cvičiacemu (školský gitlab alebo github). Pre dokumentáciu vo forme článku použite LaTeX, odporúčame použiť Overleaf pre zdieľanie projektov (pridajte aj cvičiaceho). Pre formátovanie článku odporúčame použiť šablónu IEEE, prípadne ak nájdete časopis, v ktorom by ste chceli vašu prácu publikovať, tak môžete použiť ich šablónu.

Za zadanie môžete získať spolu **40** bodov, z toho 20 sa ráta do zápočtu a 20 do skúšky, pri hodnotení berieme do úvahy:

 * kvalitu práce - Bola vybraná vhodná metodológia? Bol použitý vhodný model? Je aplikácia zmysluplná a použiteľná? Poskytujú autori nové poznatky o probléme alebo o modeloch?
 * významnosť - Je riešený problém skutočný alebo "iba" ukážkový? Má práca význam pre širšiu komunitu? Môže mať práca výraznejší dopad?
 * jedinečnosť riešenia - Bol použitý štandardný postup pre riešenie bežného problému, alebo je problém alebo metóda významná a nová?

Aby sme vašu prácu mohli hodnotiť objektívne a férovo, je dôležité, aby ste tieto body odkomunikovali v dostatočnej miere. Práve preto bude veľmi dôležité poskytnúť kvalitný prehľad existujúcej literatúry, na základe čoho umiestnite vašu prácu v širšej oblasti.

Pre zabezpečenie systematickej práce sme zadefinovali niekoľko míľnikov a odovzdávok. Od vyučujúcich dostanete spätnú väzbu po každej odovzdávke a môžete ich poprosiť o pomoc a názor hocikedy počas riešenia projektu:

 1. návrh projektu - do 11. 10. - spísaný súhrn a stretnutie s cvičiacim
 2. prehľad literatúry - do 10. 11. - spísaný v šablóne
 3. prvé výsledky - do 1. 12. - kód: existujúci pipeline, krátke zhrnutie prvých skúseností
 4. progress report - do 20. 12. - zhrnutie dosiahnutých výsledkov a návrh ďalšieho postupu; stretnutie s cvičiacim
 5. finálna odovzdávka - začiatok skúškového obdobia - súčasť skúšky

### Návrh projektu
**Deadline:** do 11. 10.

**Odovzdáte:** pdf súbor + osobné stretnutie s cvičiacim

V návrhu projektu popíšete tému, ktorú budete v rámci zadania riešiť. Odovzdáte pritom pdf súbor (1-2 strany A4, cca. 500 slov), ktorý obsahuje:

 * Aký problém budete riešiť? Prečo je zaujímavý a relevantný?
 * Aké sú ciele projektu?
 * Aké dáta použijete? Máte k dispozícii existujúce datasety, alebo budete zbierať dáta sami?
 * Akú metódu alebo algoritmus použijete? Inšpirovali ste sa existujúcim riešením, ktorý viete použiť? Ako budete existujúce riešenia rozširovať a vylepšovať?
 * Akú literatúru si potrebujete naštudovať pre orientovanie sa v riešenej problematike? Ak už máte prečítané niekoľko článkov, môžete ich krátko popísať.
 * Ako budete vyhodnocovať vaše výsledky (metriky, analýza, atď.)? Ako definujete "dobré" a "neúspešné" výsledky?
 * Súbor ďalej môže obsahovať aj odkazy na datasety a/alebo články, ktoré ste našli.

Cieľom návrhu je odštartovať váš výskum, prvé metodologické rozhodnutia nebudú striktne hodnotené. To znamená, že ak počas vývoja prídete na to, že niektoré vaše voľby boli nesprávne, pokojne ich môžete zmeniť. Samotnú tému však po odovzdaní návrhu by ste už nemali meniť. Po odovzdaní súboru musíte absolvovať aj osobné strenutie s cvičiacim, ktorý slúži na to, aby ste získali spätnú väzbu a prípadne ste prispôsobili obtiažnosť úlohy očakávaniam.

### Prehľad literatúry
**Deadline:** do 10. 11.

**Odovzdáte:** pdf súbor v šablóne článku

V ďalšej fáze riešenia sa zameráte na štúdium existujúcej literatúry a podobných riešení, ktoré môžete využiť. Popíšete pritom *state of the art* a identifikujete nedostatky existujúcich prístupov, ktoré chcete adresovať vo vašom riešení. Dobrým príkladom takéhoto prehľadu je identifikácia problému v jednej doméne a následná identifikácia prístupu, ktorý úspešne vyriešil podobný problém v inej doméne. 

Rozsah prehľadu má byť 3-4 stĺpce bez ohľadu na použitú šablónu. Pre správny odborný štýl dávajte si pozor pri čítaní článkov na to, ako sú prehľady napísané v nich, čo funguje a čo nefunguje. V prehľade by ste mali referencovať primeraný počet článkov (minimálne 20-30), pričom nezoberte iba vety z ich abstraktov alebo záverov, ale porovnávajte ich, diskutujte o nich vlastnými slovami a zamerajte sa na ich relevantnosť pre vašu prácu.

### Prvé výsledky
**Deadline:** do 1. 12.

**Odovzdáte:** kód s celým postupom predspracovania údajov a trénovania modelu + súhrn skúseností a plán práce

Tretí míľnik zadania sa skladá z pripraveného skriptu pre spracovanie dát, definície a trénovania modelu s jednoduchým vyhodnocovaním. Zatiaľ nemusíte použiť finálny dataset a definitívnu podobu modelu, ide o to, aby ste získali skúsenosti a lepší odhad toho, čo obnáša vývoj finálneho riešenia. Na základe týchto skúseností spíšte krátky dokument (jedna strana A4), kde v jednom odseku napíšete vaše prvé skúsenosti -  na aké problémy ste narazili, ako ste ich riešili, aké problémy ešte pretrvávajú, a pod. Zároveň napíšte aj plán práce pre ďalší postup - čo ešte potrebujete urobiť do finálnej odovzdávky.

### Progress Report
**Deadline:** do 20. 12.

**Odovzdáte:** pdf súbor s metodológiou a dosiahnutými výsledkami + prezentácia projektu

Do konca semestra potrebujete získať prvotné výsledky na finálnom datasete a približne by ste mali sfinalizovať aj použitú metódu a typ modelu. Okrem toho spíšete metodológiu ako aj dosiahnuté výsledky (môžete tak urobiť v šablóne pre článok). Váš projekt a čiastočné výsledky odprezentujete aj na cvičení v 13. týždni, touto odovzdávkou uzavriete zápočet.

### Finálna odovzdávka
**Deadline:** do skúšky, dátum bude špecifikovaný neskôr

**Odovzdáte:** článok, kódy, natrénované modely + poster a obhajoba projektu

Posledná odovzdávka poslúži ako praktická časť skúšky, kde váš projekt odprezentujete aj s finálnymi výsledkami. Dokumentáciu pripravíte aj vo forme vedeckého článku, ktorý po menších upravách môže byť publikovaný. Okrem toho pripravíte poster, ktorý poslúži ako grafické zhrnutie vašich výsledkov. Súčasťou skúšky bude aj obhajoba riešenia, kde zájdeme aj do technických detailov a musíte preukázať hlboké pochopenie použitých metód. Pri prezentácii budete používať poster ako pomôcku a nie powerpoint prezentáciu.

Hodnotené budú:

 * motivácia a relevantnosť projektu;
 * použité dáta a ich popis;
 * výber metódy, modelu, hyperparametrov a pod.;
 * metodolické rozhodnutia;
 * podanie a analýza výsledkov;
 * diskusia a okomentovanie výsledkov;
 * pridaná hodnota práce.
