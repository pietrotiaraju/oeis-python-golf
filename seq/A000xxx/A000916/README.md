# A000916

> a(2n) = n+2, a(2n-1) = smallest number requiring n+2 letters in English.
> — [OEIS A000916](https://oeis.org/A000916)

Offset 1: 1, 3, 4, 4, 3, 5, 11, 6, 15, 7, 13, 8, 17, 9, 24, 10, 23, 11, 73, 12, 3000, 13, 11000, 14, 15000, 15, 101, 16, …

### Python 3 — 256 bytes

```python
c=b'033544355436688779886655576678778;;::999;<<A=<?=><'
f=lambda n:n>99and f(n//10**(e:=~-len(str(n))//3*3or 2))+c[28+e//3]%48+f(r:=n%10**e)+3*(0<r<100)or n>19and c[n//10+18]%48+f(n%10)or c[n]%48
L=3
while 1:
 n=1
 while f(n)-L:n+=1
 print(n);print(L);L+=1
```

**Which names**

- British English, with "and" (Sean A. Irvine's comment): "one hundred
  and one" has 16 letters, so a(27) = 101. Letters only: spaces and hyphens
  do not count.
- The "and" also goes before a last part below 100 after a larger scale
  word: "one thousand and one", "one million and fifty", but "one thousand
  one hundred and four" (28 letters, a(51) = 1104). The data need this:
  without it "one thousand one" would have 14 letters and a(23) would be
  1001, not 11000.
- Positive numbers only: "zero" has 4 letters, yet a(3) = 4.
- Scale words: thousand, then the short-scale names million, billion, …,
  vigintillion (10⁶³), with the dictionary spellings sexdecillion and
  novemdecillion (as in [A000052](../A000052/)). Larger names are not
  standard, so the program stops there (see the notes).

**How it works**

- `f(n)` is the letter count of the name of n, and f(0) = 0 (an empty
  remainder). The bytes of `c` minus 48 (`%48`) are the word lengths:
  places 0–19 hold zero (0, never named), one, …, nineteen; 20–27 hold
  twenty … ninety, reached by `n//10+18`; 28–49 hold hundred, thousand,
  million, …, vigintillion, reached by `28+e//3`. `;<=>?A` are 11, 12, 13,
  14, 15 and 17 (quattuordecillion).
- For n ≥ 100, `e` is the exponent of the largest word that fits:
  ~-len(str(n))//3*3 is the number of digits minus one rounded down to a
  multiple of 3, and `or 2` makes it 2 (hundred) for 3-digit numbers. Then
  f(n) = f(n // 10ᵉ) + word + f(r) + 3·[0 < r < 100], r = n mod 10ᵉ: the 3
  is the "and". For hundreds r < 100 always, so "and" comes whenever r > 0;
  above, only when the rest is below 100.
- 20–99: tens word + `f(n%10)` (0 for a round ten); below 20 the table.
  `n>19and…or c[n]%48` puts the table last, so f(0) needs no special case.
- For L = 3, 4, …: count n up from 1 until f(n) = L, print n and then L
  (the even terms).

**Notes**

- Exact; for every L whose smallest number is below 10⁶⁶ the program
  finds it. From 10⁶⁶ on `c[50]` raises an `IndexError`: the program stops
  rather than invent a name. A 3-digit group has at most 27 letters
  ("three hundred and seventy-three"), so below 10⁶⁶ no name has more
  than 22·27 + 230 = 824 letters (the 21 scale words add 230): the terms
  for more letters do not exist in this naming system, and the program
  would end there after an astronomically long scan.
- Up to 10⁹ the short and long scales agree; the first term that could
  depend on the choice is for 97 letters (96 is the most below 10⁹,
  373,373,373).
- The scan restarts at 1 for every L. The b-file (56 terms, up to
  a(55) = 1111) prints in 0.2 s; in 60 s it reaches about 130 terms
  (a(129) = 1117373, 67 letters).
- The b-file has 56 terms, synthesized from the OEIS data; the bar is all
  56.
- `%48` is used twice; raw control bytes would drop it but need escapes
  for the values 0, 10 and 13, for about the same total.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 256 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000916), CC BY-SA 4.0.
