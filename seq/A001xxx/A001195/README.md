# A001195

> a(n) = floor(n*log((14/11)*n^(10/9))).
> — [OEIS A001195](https://oeis.org/A001195)

Offset 1: 0, 2, 4, 7, 10, 13, 16, 20, 24, 27, 31, 36, 40, 44, 48, 53, …

### Python 3 — 144 bytes

```python
h=lambda c,k=9:(11**9)**n*c**k<(14**9*n**10)**n*F**k and-~h(c,k+9)
A=2;F=J=n=1
while 1:
 while(s:=h(A))>h(A+1):J+=1;A=J*A+1;F*=J
 print(+s);n+=1
```

**How it works**

- a(n) is the largest k with e^(9k) < Qₙ = (14⁹·n¹⁰/11⁹)ⁿ, the ninth power
  of e^k ≤ ((14/11)·n^(10/9))ⁿ. Equality never happens: e^m is irrational
  for every integer m ≠ 0, and Qₙ > 1.
- e is trapped between rationals: with F = J! and A = Σⱼ₌₀ᴶ J!/j!,
  A/F < e < (A+1)/F for J ≥ 1 (the tail of Σ 1/j! is below 1/J!).
  `J+=1;A=J*A+1;F*=J` moves to the next J.
- `h(c)` counts the k = 1, 2, … with (c/F)^(9k) < Qₙ, in integers:
  11^(9n)·c^(9k) < (14⁹·n¹⁰)ⁿ·F^(9k), stopping at the first failure. With
  c = A it can only overcount and with c = A + 1 only undercount, so once
  the two agree the count is exact. Both bounds tend to e, so for each n
  the refining loop ends.
- The bounds stay valid for every n, so `A`, `F` and `J` are kept from one
  term to the next instead of starting again. `+s` turns a count of
  `False` (a(1) = 0) into 0.

**Notes**

- No floating point: the logarithm is never computed, only compared
  exactly through powers of the bounds of e. J stays small, and the 58
  terms of the b-file take about 3 s here.
- `h` recurses once per k, so Python's default recursion limit stops the
  program near n = 150, where a(n) passes 1000 (an interpreter limit, far
  beyond the b-file).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 144 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001195), CC BY-SA 4.0.
