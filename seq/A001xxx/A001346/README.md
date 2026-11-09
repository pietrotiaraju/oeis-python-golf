# A001346

> a(n) = Sum_{k = 0..4} (n+k)! C(4,k).
> — [OEIS A001346](https://oeis.org/A001346)

Offset -1: 23, 65, 261, 1370, 8742, 65304, 557400, 5343120, 56775600, 661933440, …

For n ≥ 0, a(n) = n! + 4·(n+1)! + 6·(n+2)! + 4·(n+3)! + (n+4)!. At n = −1
the k = 0 term would be (−1)!, so the sum does not define a(−1); the OEIS
gives a(−1) = 23 (Marcus's PARI program on the entry), which is the sum
with (−1)! read as −1: −1 + 4·0! + 6·1! + 4·2! + 3! = 23.

### Python 3 — 60 bytes

```python
g=1;x=3
while[print(g*x*(x*-~x-4)+g//(x-3or-1))]:x+=1;g*=x-3
```

**How it works**

- Write j = n + 1. Dividing each (j−1+k)! by (j−1)! leaves a rising
  product, so for j ≥ 1
  a(j−1) = (j−1)!·(1 + 4j + 6j(j+1) + 4j(j+1)(j+2) + j(j+1)(j+2)(j+3))
  = (j−1)! + j!·R(j) with R(j) = j³ + 10j² + 29j + 24.
- The loop counter `x` is j + 3 = n + 4, and R(x − 3) = x³ + x² − 4x
  = x(x(x+1) − 4), which is `x*(x*-~x-4)` (`-~x` is x + 1).
- `g` is j! (it starts at 0! = 1 and `g*=x-3` multiplies by the new j).
  For j ≥ 1, (j−1)! = j!/j is `g//(x-3)`, an exact division.
- At j = 0, x − 3 is 0 and `or` falls back to −1, so the last term is
  1//−1 = −1: that is (−1)! read as −1, and the print gives
  3·8 − 1 = 23 = a(−1). No term is stored.
- `print` returns `None` and `[None]` is truthy, so the loop never ends.
  Exact integers, so every term is right. (`3or` makes Python warn about
  the number literal on stderr; it still parses as `3 or`.)

**Notes**

- The same (−1)! reading gives a(−1) = 2, 7, 88 in
  [A001344](../A001344/), [A001345](../A001345/) and
  [A001347](../A001347/); 23 is also a(−1) + a(0) = 7 + 16 of A001345, the
  Pascal step C(4, k) = C(3, k) + C(3, k−1) that links the two sums for
  n ≥ 0.
- Keeping (j−1)! and j! in two variables, `f=-1;g=1;x=3` /
  `while[print(f+g*x*(x*-~x-4))]:x+=1;f,g=g,g*(x-3)`, is 61 bytes. The
  form of [A001344](../A001344/), which stores a(−1) and counts by j:
  `f*n*(n+3)*(n*n+7*n+8)+f` is 62 bytes, with (j+1)(j+4)(j+5) + 4 64 and
  Horner 65; with the counter at j + 3 it is 63.
- Python's 4300-digit int-to-str limit stops the program at a(1555), the
  first term with more than 4300 digits, after printing a(−1) to a(1554).
- The b-file has 102 terms (n = −1 to 100); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001346), CC BY-SA 4.0.
