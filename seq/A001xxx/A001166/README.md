# A001166

> Smallest natural number requiring n letters in English.
> — [OEIS A001166](https://oeis.org/A001166)

Offset 3: 1, 4, 3, 11, 15, 13, 17, 24, 23, 73, 3000, 11000, 15000, 101, 104, …

### Python 3 — 247 bytes

```python
c=b'033544355436688779886655576678778;;::999;<<A=<?=><'
f=lambda n:n>99and f(n//10**(e:=~-len(str(n))//3*3or 2))+c[28+e//3]%48+f(r:=n%10**e)+3*(0<r<100)or n>19and c[n//10+18]%48+f(n%10)or c[n]%48
L=3
while 1:
 n=1
 while f(n)-L:n+=1
 print(n);L+=1
```

**Which names**

- British English with "and", as the entry's comment says ("one hundred
  and one"): a(16) = 101. Letters only: spaces and hyphens do not count.
- The "and" also goes before a last part below 100 after a larger scale
  word ("one thousand and one", "one million and fifty", but "one thousand
  one hundred and four"). Without it "one thousand one" would have 14
  letters and a(14) would be 1001, not 11000.
- Positive numbers only, so "zero" plays no part.
- Scale words: thousand, then million, billion, …, vigintillion (10⁶³), with
  the dictionary spellings sexdecillion and novemdecillion.

**How it works**

- This is the letter count of [A000916](../../A000xxx/A000916/), whose odd
  terms are this sequence; here only the numbers are printed.
- `f(n)` is the letter count of the name of n, and f(0) = 0 (an empty
  remainder). The bytes of `c` minus 48 (`%48`) are the word lengths: places
  0–19 hold zero (never spoken), one, …, nineteen; 20–27 twenty … ninety,
  reached by `n//10+18`; 28–49 hundred, thousand, million, …, vigintillion,
  reached by `28+e//3`.
- For n ≥ 100, e is the exponent of the largest word that fits, and
  f(n) = f(n // 10ᵉ) + word + f(r) + 3·[0 < r < 100] with r = n mod 10ᵉ: the
  3 is the "and". For hundreds r < 100 always, so "and" comes whenever r > 0;
  above, only when the rest is below 100.
- For L = 3, 4, …: count n up from 1 until f(n) = L.

**Notes**

- Exact; every term whose number is below 10⁶⁶ is found. At 10⁶⁶ `c[50]`
  raises an `IndexError`: the program stops rather than invent a name.
- The scan restarts at 1 for every L; the 55 terms of the b-file (up to
  a(57) = 117373) take a few seconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 247 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001166), CC BY-SA 4.0.
