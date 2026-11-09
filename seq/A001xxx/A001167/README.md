# A001167

> Smallest natural number requiring n words in English (as spoken in England).
> — [OEIS A001167](https://oeis.org/A001167)

Offset 1: 1, 21, 21000, 101, 121, 1101, 1121, 21121, 101101, 101121, 121121, …

### Python 3 — 186 bytes

```python
w=lambda n:n>99and w(n//10**(e:=~-len(str(n))//3*3or 2))+1+w(r:=n%10**e)+(0<r<100)or(n>0)+(n>20)
g=lambda k:k and g(k//3)*10+k%3
L=1
while 1:
 k=1
 while w(g(k))-L:k+=1
 print(g(k));L+=1
```

**Which names**

- British English with "and" ("one hundred and one", 4 words: a(4) = 101),
  including the "and" before a last part below 100 after a larger scale
  word ("one thousand and one"; without it 1001 would be a(3), not 21000).
- A compound like "twenty-one" counts as two words (a(2) = 21); "and" and
  each scale word (hundred, thousand, million, …) count as one.

**How it works**

- `w(n)` counts words with the same recursion as the letter count of
  [A001166](../A001166/): for n ≥ 100, e is the exponent of the largest scale
  word that fits, and w(n) = w(n // 10ᵉ) + 1 + w(r) + [0 < r < 100] with
  r = n mod 10ᵉ, the last term being the "and". Below 100 only 0, 1, 2, 10,
  11, 12, 20, 21 and 22 ever occur (see the next point), so the count is
  `(n>0)+(n>20)`: 0 words for an empty remainder, 2 for twenty-one and
  twenty-two, 1 for the rest. For other digits w would be wrong, and it is
  never asked.
- The smallest number with L words has only the digits 0, 1 and 2. In any
  number, replace every 3-digit group by 100 if it has a hundreds digit
  (plus nothing), then its last two digits by 1 if they are one word (1–20 or
  a round ten) or by 21 if they are two. No group grows, zero groups stay
  zero, a group keeps its hundreds part and its non-zero rest, so every word
  and every "and" stays: the result is no larger and has the same count.
- `g(k)` reads the base-3 digits of k as a decimal number, so k = 1, 2, 3, …
  runs through exactly those numbers in increasing order. For L = 1, 2, …
  the program scans k from 1 until w(g(k)) = L.

**Notes**

- Exact; scale names go up to vigintillion (10⁶³), so terms are only defined
  while they stay below 10⁶⁶, far beyond any scan.
- The scan restarts for every L and costs about 3 times more per extra
  digit: 24 terms (to a(24) = 121121121121) in about 10 s here, 25 in about
  29 s. The bar is 25 terms in 60 s; a(26) = 21121121121121 needs about 3·10⁶
  steps of k.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 186 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001167), CC BY-SA 4.0.
