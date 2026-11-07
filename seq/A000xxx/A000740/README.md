# A000740

> Number of 2n-bead balanced binary necklaces of fundamental period 2n, equivalent to reversed complement; also Dirichlet convolution of b_n=2^(n-1) with mu(n); also number of components of Mandelbrot set corresponding to Julia sets with an attractive n-cycle.
> — [OEIS A000740](https://oeis.org/A000740)

Offset 1: 1, 1, 3, 6, 15, 27, 63, 120, 252, 495, 1023, 2010, 4095, 8127, 16365, 32640, 65535, 130788, 262143, 523770, …

### Python 3 — 82 bytes

```python
f=lambda n:2**~-n-sum(f(d)for d in range(1,n)if n%d<1)
n=1
while[print(f(n))]:n+=1
```

**How it works**

- a(n) = Σ_{d|n} μ(n/d)·2^(d−1), so by Möbius inversion
  Σ_{d|n} a(d) = 2^(n−1) (the compositions of n, grouped by the gcd of
  their parts). The recursion is that identity solved for a(n):
  a(n) = 2^(n−1) − Σ a(d) over the proper divisors d of n, with no Möbius
  function needed.
- `2**~-n` is 2^(n−1). There is no cache: f(n) calls f on its proper
  divisors, then on theirs, which is cheap (about n log n steps per term).

**Notes**

- Exact integers; the whole b-file (3322 terms, up to 1000 digits) takes
  about 2 s and is the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000740), CC BY-SA 4.0.
