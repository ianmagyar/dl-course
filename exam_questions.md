**Okruh 1: Základy neurónových sietí**

1. Štruktúra umelého neurónu, úlohy a podstata jednotlivých častí: vstup, synaptické váhy, vstupná funkcia, aktivačná funkcia, výstupná funkcia, bias.
2. Perceptron ako neurónová sieť: možné výstupy a chyby, priebeh a spôsob trénovania; limity využitie perceptronu.
3. Najčastejšie aktivačné funkcie: ich definícia a využitie, derivácia, výhody a nevýhody. (*funkcia identity*, *sign*, *sigmoidálna funkcia*, *hyperbolický tangens*, *ReLU*, *funkcia softmax*)
4. Štruktúra neurónových sietí, spôsob výpočtu neurónovej siete.
5. Princípy trénovania neurónových sietí: backpropagation, základné princípy, najpodstatnejšie vzorce (výpočet zmeny váhy, aktualizácia váhy).
6. Univerzálna aproximačná teoréma a jej dôsledky na hlboké učenie.
7. Najčastejšie problémy pri trénovaní neurónových sietí a ich riešenie: pretrénovanie, vanishing a exploding gradient, chýbajúca konvergencia, uviaznutie v lokálnom optime, dlhé trénovanie.

**Okruh 2: Konvolučné neurónové siete**

8. Použitie konvolučných sietí (CNN), nedostatky tradičných sietí, ktoré konvolučné siete riešia, výhody CNN.
9. Najvýznamnejšie vlastnosti CNN, využitie parametrov v porovnaní so základnými sieťami.
10. Štruktúra konvolúcie: kernel, operácia konvolúcie, rozmery výstupu, úloha jednotlivých filtrov.
11. Padding: podstata, úloha, fungovanie, typy (*valid*, *half*, *full*).
12. Pooling: podstata, efekt na výstup vrstvy, typy (*max*, *average*).
13. Hyperparametre konvolučného bloku a ich najčastejšie nastavenie.
14. Podstata a rola nekonvolučnej časti CNN.
15. Aplikácia algoritmu backpropagation na jednotlivé vrstvy v CNN (*aktivačná vrstva*, *pooling vrstva*, *konvolučná vrstva*) - iba princípy, nie vzorce.
16. Najčastejšie CNN a ich hlavné vlastnosti. (*LeNet-5*, *AlexNet*, *VGG*, *GoogLeNet / Inception*, *ResNet*)
17. Typy úloh riešiteľných CNN.

**Okruh 3: Trénovanie hlbokých neurónových sietí**

18. Problematika trénovania hlbokých sietí, nevýhody algoritmu backprop.
19. Hyperparametre hlbokých sietí a spôsob ich aktualizácie.
20. Základné predspracovanie údajov: aditívne predspracovanie a normalizácia príznakov.
21. Inicializácia váh a biasov.
22. Vanishing a exploding gradient: čo spôsobuje tieto chyby a ako tento problém vyriešime?
23. Prístupy gradientového zostupu: aký problém riešia a akým spôsobom, aké majú nedostatky? (*learning rate decay*, *momentum-based learning*, *parameter-specific gradient descent*, *gradient clipping*)
24. Najvýznamnejšie optimalizátory: aký problém riešia a akým spôsobom, aké majú nedostatky? (*AdaGrad*, *RMSProp*, *AdaDelta*, *Adam*)
25. Stochastický gradientový zostup a využitie mini-batch trénovania: výhody a nevýhody týchto prístupov.
26. Úloha a typy normalizácií v rámci neurónových sietí. (*batchnorm*, *layer normalization*, *instance normalization*, *group normalization*, *weight normalization*)
27. Vyváženie biasu a variance.
28. Problém generalizácie, jeho príčiny a spôsob jeho riešenia. (*regularizácia*, *early stopping*, *ensemble metódy – bagging a dropout*, *continuation learning*, *curriculum learning*, *pretrénovanie*)
29. Prístupy vyhodnotenia hlbokých sietí: hold-out a krížová validácia.

**Okruh 4: Embeddingy**

30. Nekontrolované predtrénovanie po jednotlivých vrstvách siete: princíp fungovania a deep belief siete.
31. Štruktúra autoenkódera a jeho fungovanie.
32. Čo je to sparse reprezentácia v autoenkóderoch a ako sa dá využiť pre embedding?
33. One-hot encoding: princíp, výhody a nevýhody.
34. Dense embedding: princíp, výhody a nevýhody.
35. Vyjadrenie podobnosti a vzdialenosti v embedding priestore: Euklidovská a kosínusová vzdialenosť (aj vzorce).
36. Typy embeddingu textov (na úrovni slov, kontextu, viet a dokumentov).
37. Typy embeddingu obrázkov a videí.
38. Typy grafových embeddingov (uzlov a hrán).
39. Typy audio a rečových embeddingov.
40. Typy multimodálnych embeddingov.
41. Pozičný embedding a jeho podstata pre transformery.

**Okruh 5: Rekurentné siete**

42. Problémy spracovania časových radov tradičnými neurónovými sieťami.
43. Základný princíp fungovania rekurentných neurónových sietí (RNN): mapovanie vstupu na výstup, rozmery vstupu a výstupu, rôzne kombinácie vstupov a výstupov.
44. RNN ako sieť s premenlivou hĺbkou, problém exploding a vanishing gradient.
45. Architektúra RNN, proces výpočtu výstupu.
46. Princíp aplikácie backpropagation na RNN (bez vzorcov).
47. Porovnanie typov RNN: základná, obojsmerná, viacvrstvová, LSTM, GRU (na úrovni princípov, nie vzorcov).
48. Spôsoby využitia RNN: image captioning, strojový preklad, question-answering, klasifikácia postupností, klasifikácia tokenov, predikcia časových radov.

**Okruh 6: Self-supervised learning**

49. Typy učenia neurónových sietí: kontrolované, nekontrolované, self-supervised (porovnať ich).
50. Aplikácia prístupu self-supervised learning na textoch.
51. Aplikácia prístupu self-supervised learning na obrazových dátach.
52. Kontrastívna chyba a jej význam pre self-supervised learning.
53. Problém dimensional collapse: príčiny a možné riešenia.

**Okruh 7: Attention mechanizmus**

54. Inšpirácia a podstata attention mechanizmu pre neurónové siete.
55. Využitie attention mechanizmu pre obrázky.
56. Využitie attention mechanizmu pre texty.
57. Attention vrstva ako časť neurónovej siete: podstata, výpočet kontextového vektora cez analytický prístup a cez attention váhy.
58. Attention mechanizmy bez učenia a s učením: porovnanie, výhody a nevýhody.
59. Scaled dot-product attention: význam informačných skupín query, key a value; výpočet výstupu attention vrstvy.

**Okruh 8: Transformery**

60. Štruktúra transformerových architektúr: podstata enkódera a dekódera.
61. Princíp fungovania transformerov, porovnanie výhod s architektúrami RNN.
62. Multi-head attention: princíp fungovania a význam viacerých attention hláv.
63. Rozmery vstupu a výstupu transformerov, limity na dĺžku vstupných dát.

**Okruh 9: Generatívna umelá inteligencia**

64. Problematika generatívnych neurónových sietí, porovnanie s autoenkódermi.
65. GAN siete: štruktúra, úloha generátora a diskriminátora, princíp trénovania, priebeh trénovania.
66. Spôsob riešenia podmieneného generovania pri GAN.
67. Variačné autoenkódery: štruktúra, úloha enkódera a dekódera, latentný priestor, princíp trénovania, fungovanie generátora po trénovaní, výhody a nevýhody.
68. Autoregresívne modely: štruktúra, princíp trénovania, fungovanie generátora po trénovaní, výhody a nevýhody.

**Okruh 10: Hlboké učenie posilňovaním**

69. Základný princíp učenia posilňovaním: prostredie, agent, stav, akcia, odmena, pozorovanie.
70. Aplikácia učenia posilňovaním pri trénovaní neurónových sietí: základný princíp a výhody/nevýhody.
71. Hlboké Q-siete (DQN): štruktúra, spôsob trénovania (vysvetliť na základe pseudokódu), výhody a nevýhody.
72. Využitie pamäte pri trénovaní DQN: motivácia a princíp fungovania.
73. Využitie target sietí pri trénovaní DQN: motivácia a princíp fungovania.
74. Typy hlbokých sietí s učením posilňovaním: value-based, policy-based, actor-critic architektúry.
