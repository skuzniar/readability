# Readability Calculator

An interactive program to calculate readability scores of text samples using various formulas. To start the program run:

```
python readability-calculator.py sources
```

To show more details run:

```
python readability-calculator.py --details sources
```

To enable verbose output run:

```
python readability-calculator.py --verbose sources
```

Here is a sample session where we compute scores for one of the samples.

```
python readability-calculator.py sources
==> ?
h           - Print this message.
s           - Scan for sources.
l           - List available sources.
#|all [xyz] - Run n-th source or all sources.
              An optional argument can be used to only run a single readability formula:
                  ari - Automated Readability Index
                  fre - Flesch Reading Ease Score
                  gfi - Gunning Fog Index
                  fkg - Flesch-Kincaid Grade Level
                  clr - Coleman-Liau Readability Index
                  smo - SMOG Index
                  olf - Original Linsear Write Formula
q           - Quit.
==> l
  1 - sources/long.txt
  2 - sources/short.txt
==> 1
Running [sources/long.txt]
   Automated Readability Index Grade level =  8.42
                 Flesch Reading Ease score = 61.05
             Gunning Fog Index Grade level = 11.50
                Flesch-Kincaid Grade level =  8.00
Coleman-Liau Readability Index Grade level =  9.96
                    SMOG Index Grade level = 11.31
      Original Linsear Write Formula score = 82.59 
==> 2 olf
Running [sources/short.txt]
      Original Linsear Write Formula score = 79.75
==> q
```

