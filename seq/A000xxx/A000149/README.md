# A000149

> a(n) = floor(e^n).
> — [OEIS A000149](https://oeis.org/A000149)

Offset 0: 1, 2, 7, 20, 54, 148, 403, 1096, 2980, 8103, 22026, 59874, …

### Python 3 — 77 bytes

```python
n=0
while 1:
 N=F=P=d=1
 while-N%F<P:P*=n;N=N*d+P;F*=d;d+=1
 print(N//F);n+=1
```

**How it works**

- The inner loop sums the series e^n = Σ n^k/k! over the common
  denominator F = d!: N/F is the partial sum up to the term n^d/d!, and
  P = n^d, so P/F is the last term added. Moving to the next term
  multiplies N and F by the new index and adds the new n^d to N.
- N/F is a lower bound for e^n, and N/F + P/F is an upper bound once
  d ≥ 2n − 1: the tail Σ_{k>d} n^k/k! is below
  (n^d/d!)·n/(d+1−n) ≤ n^d/d!.
- The loop stops when both bounds have the same floor, that is when
  N mod F + P ≤ F with N mod F > 0. `-N%F` is F − N mod F (or 0 when F
  divides N), so `while-N%F<P` keeps going exactly until then. Stopping at
  equality is safe because the tail bound is strict, so e^n stays below
  the integer N/F + P/F.
- Before d = 2n − 1 the upper bound may be wrong, but there
  P/F = n^d/d! ≥ 1 (pair the factors of (2n−2)! as i·(2n−1−i) < n²), so
  `-N%F<P` holds and the loop cannot stop early.
- For n = 0 every term after the first is 0, so the loop stops at d = 1
  with N/F = 1 = e^0. For n ≥ 1, e^n is irrational, so its fractional part
  is not 0 and the loop always ends.

**Notes**

- Everything is exact integer arithmetic; each term needs about e·n terms
  of the series. The whole b-file (301 terms) prints in under a second and
  about 1100 terms come out in 60 s. The bar is the whole b-file in 60 s.
- The test `N%F+P>=F` (both floors differ) is two bytes longer than
  `-N%F<P` and needs the space after `while`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 77 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000149), CC BY-SA 4.0.
