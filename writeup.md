# WhiteHat Grand Prix 06 (2020)
WhiteHat Grand Prix - 06 - 2020

## Overview

**URL:** https://grandprix.whitehatvn.com/  
**Organisors:** Vietnam Today
**Duration:** 24 hours  
**Team mates:** Team Competition  

```
Title                         Category        Points  Flag
----------------------------- --------------- ------- ---------------------------------------
Prog1                           Prog            100    WhiteHat{Y0u_h4v3_4_Sm4rt_Br41n}
```
## Prog1

* **Category:** Prog
* **Points:** 100

### Challenge

```
PROGRAMING - WHITEHAT GRANDPRIX 06:

--> COUNT THE NUMBER OF POSSIBLE TRIANGLES <--

HOW MANY TRIANGLES ARE CREATED BY N (1..N) NUMBER. N < 10^6

Example:  N = 5
OUTPUT : 3 

(2,3,4),(3,4,5),(2,4,5)
................/\...................|\...................
.............../  \..................| \..................
............../    \.................|  \.................
............./      \................|   \................
............/        \...............|    \...............
.........../          \..............|     \..............
........../____________\.............|______\.............
    
n = 16
Answer:
```
> nc 15.164.75.32 1999



### Solution

[prog1.py](/writeupfiles/prog1.py)

If you look at the python code above, I've got 2 functions called CountTriangles() and CountTriangles2().
The first function was from https://www.geeksforgeeks.org/find-number-of-triangles-possible/. This was a very slow method for what we want since it used an array of non-sequencial integers. In our case, we are given a sequence from 1 to N. I first counted the triangles from N=1 to N=11 to look for patterns. What I found was a pattern 3,7,13,22,34,50,70,95,etc. After doing a bit of research, came across https://oeis.org/A002623. With this new formula, I defined the second function. Then the rest was just python programming using pwntools.

**Flag**
```
Plain Text: WhiteHat{Y0u_h4v3_4_Sm4rt_Br41n}
SHA1: WhiteHat{e6bee01defdbcb5fab218342855b49b1b3e6fe8b}
```
---
