# A000354

> Expansion of e.g.f. exp(-x)/(1-2*x).
> — [OEIS A000354](https://oeis.org/A000354)

Offset 0: 1, 1, 5, 29, 233, 2329, 27949, 391285, 6260561, 112690097, …

### Python 3 — 36 bytes

```python
a=n=0
while[print(a:=a*n&-3|1)]:n+=2
```

**How it works**

- Multiplying the e.g.f. by 1 − 2x gives a(k) − 2k·a(k−1) = (−1)^k, so
  a(k) = 2k·a(k−1) + (−1)^k, the recurrence of the derangements
  [A000166](../A000166/) with 2k in place of k. Here `n` = 2k, so `a*n` is
  x = 2k·a(k−1).
- The ±1 is done with bits. Every a(k) is odd (x is even), so x/2 = k·a(k−1)
  has the parity of k and x ≡ 2k (mod 4): bit 1 of x is set exactly when k is
  odd. `&-3` clears bit 1 and `|1` sets bit 0, so `x&-3|1` is x + 1 for even k
  and x − 2 + 1 = x − 1 for odd k, which is x + (−1)^k.
- As in A000166 the loop starts one step early: at n = 0 the product is 0 and
  `0&-3|1` is a(0) = 1, whatever a(−1) is.

**Notes**

- The derangement trick `a*n^1` only adds (−1)^k when x has the parity of k;
  here x is always even, hence the mask. Adding bit 1 back by XOR,
  `a*n^1^n&2`, is 37 bytes.
- The signed terms b(k) = (−1)^k a(k) obey b(k) = 1 − 2k·b(k−1), and
  `b=n=0` + `while[print(abs(b:=1-n*b))]:n+=2` is 38 bytes; the recurrence
  with `(-1)**n` and a unit step is 41.
- Exact integers, so every term is right. a(1424) is the first term with more
  than 4300 digits, so Python 3.11+ stops there with a `ValueError` from the
  int-to-str limit, which is not counted as a failure.
- The b-file has 101 terms (n = 0 to 100) and prints at once; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000354), CC BY-SA 4.0.
