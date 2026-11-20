# A001920

> Expansion of 1/(1+759*x^2+2576*x^3+759*x^4+x^6).
> — [OEIS A001920](https://oeis.org/A001920)

Offset 0: 1, 0, -759, -2576, 575322, 3910368, -429457542, -4448043600, 315448497771, …

### Python 3 — 68 bytes

```python
a=[1]+[0]*5
while[print(a[0])]:a=[-759*(a[1]+a[3])-2576*a[2]-a[5]]+a
```

**How it works**

- **The recurrence.** Multiplying the series by its denominator gives 1, so
  a(n) + 759a(n − 2) + 2576a(n − 3) + 759a(n − 4) + a(n − 6) is 1 for n = 0
  and 0 for n > 0, with a(n) = 0 for n < 0.
- **The list, newest first.** `a` starts as a(0), a(−1), …, a(−5) =
  1, 0, 0, 0, 0, 0, so `a[k]` is always a(n − k). Each pass prints `a[0]` =
  a(n) and puts a(n + 1) = −759(a(n − 1) + a(n − 3)) − 2576a(n − 2) −
  a(n − 5) in front; those terms are `a[1]`, `a[3]`, `a[2]` and `a[5]`, one
  byte each shorter than the negative indices of an appended list, which
  pays for `a=[…]+a` over `a+=…,`. The two 759s share one multiplication.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The coefficients 1, 759, 2576, 759, 1 are the weight distribution of the
  extended binary Golay code (codewords of weight 0, 8, 12, 16, 24), so the
  denominator is its weight enumerator with y⁴ = x.
- Appending at the end (`a=[0]*5+[1]`, `a+=…,` with `a[-2]` … `a[-6]`) is
  71 bytes; six variables in a tuple update are 73. Rebuilding the list
  costs time linear in n per term, which stays small: the terms grow by
  about 1.44 digits each, and Python's 4300-digit int-to-str limit stops
  the program at about n = 2980.
- The b-file has 701 terms (n = 0 to 700); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001920), CC BY-SA 4.0.
