# readability
Readability formulas.

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
h     - Print this message.
s     - Scan for sources.
l     - List available sources.
#|all - Run n-th source or all.
q     - Quit.
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
==> q
```

