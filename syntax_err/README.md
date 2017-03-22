## Opravte syntaktické chyby v nasledujúcich programoch

### Počet komponentov
Na vstupe dostanete neorientovaný graf, nie nutne spojitý. Program má za úlohu spočítať z koľkých komponentov sa skladá. Na vstupe budú čísla *m*, *n* udávajúce počet hrán a vrcholov. Za nimi nasleduje *m* riadkov s hranami *a b*. (Hrana z vrcholu *a* do vrcholu *b*)

0 < *m n* < 10 000
0 < *a b* <= n

#### Vstupy
'''
6 9
1 2
1 3
3 4
5 6
7 8
8 9

>>> 3

7 10
1 6
2 5
3 4
4 5
6 7
8 9
10 10

>>> 4
'''



### Bináre vyhľadávanie
V <a href="binary_search.txt">súbore</a> je na prvom riadku postupnosť čísel. Na ďalších riadkoch sú čísla, o ktorých má procgram povedať, či sa v postupnosti nachádzajú. Ak áno, vypíše index čísla ak nie, vypíše -1.
