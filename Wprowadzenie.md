# Wprowadzenie #

Quantum Computing Simulator (QCS) to pakiet przeznaczony do symulacji obliczeń kwantowych. Podstawowy sposób pracy z pakietem polega na wykorzystaniu środowiska udostępnianego przez język Python. Pozwala to na tworzenie skryptów odpowiedzialnych za symulacje algorytmów kwantowych np.: w postaci obwodów kwantowych. Możliwa naturalnie jest także praca interaktywna np.: w środowisku IDLE.

Jednak pakiet QCS, jest zestawem funkcji opracowanych w języku C, co oznacza iż można tworzyć symulacje na poziomie biblioteki funkcji QCS.


# Podstawowe informacje #

Dalsze informacje
  * instalacja pakietu (Windows)
  * kompilacja
  * przykład Hello Qubits!

## Instalacja pakietu ##

## Kompilacja ##

## Przykład 1 -- Hello Qubits! ##

Skrypt w Pythonie budujący parę EPR (para splątanych qubitów, czyli tzw. para Einsteina-Podolkiego-Rosena) jest następujący:

```
#! /usr/bin/python

import qcs

q = qcs.QuantumReg(2)
q.Reset()
q.HadN(0)
q.CNot(0,1)
q.Pr()
```

## Przykład 2 -- Hello Qudits! ##

```
#! /usr/bin/python

import qcs

q = qcs.QuantumReg(2,3)
q.Reset()
q.HadN(0)
q.Pr()
```