# A000379

> Numbers where total number of 1-bits in the exponents of their prime
> factorization is even; a 2-way classification of integers: complement of
> A000028.
> — [OEIS A000379](https://oeis.org/A000379)

Offset 1: 1, 6, 8, 10, 12, 14, 15, 18, 20, 21, 22, 26, 27, 28, 32, 33, …

### Python 3 — 88 bytes

```python
f=[0,n:=1]
while[f[n]>0==print(n)]:n+=1;f+=-sum(f[d]for d in range(1,n)if n%d<(d*d!=n)),
```

**How it works**

- The program of the complement [A000028](../A000028/) with the test
  flipped: it prints the n with f(n) = +1 instead of −1.
- f(n) = (−1)^(Σ popcount(eᵢ)) for n = Π pᵢ^eᵢ. It is multiplicative with
  f(pᵉ) = t(e), the ±1 Thue–Morse sign. Over the divisors of pᵉ the signs
  t(0), …, t(e) cancel in pairs, leaving 0 for odd e and t(e/2) for even e,
  so **Σ_{d|n} f(d) = f(√n) when n is a square and 0 otherwise**: the
  divisors other than √n always sum to 0.
- So f(n) = −Σ f(d) over the divisors d < n with d² ≠ n, from f(1) = 1,
  with no factoring. `n%d<(d*d!=n)` is "d divides n and d ≠ √n", and
  `f+=…,` appends f(n) as a one-tuple; the 0 in `f=[0,n:=1]` is padding
  so that `f[d]` is f(d).
- `[f[n]>0==print(n)]` is a non-empty list, so the loop never stops, and
  the chained comparison calls `print(n)` only when f(n) > 0. Here n = 1,
  with f(1) = 1, is printed first, as the sequence wants.

**Notes**

- Exact integers; the recurrence is proved above for every n.
- Each term sums over n − 1 candidate divisors, so the time grows like
  n². The b-file has 10000 terms (up to 19999); on a machine busy with
  other jobs the program printed 9853 to 10000 of them in 60 s (A000028,
  the same loop, does its whole b-file in about 20 s alone). The bar is
  8000 terms in 60 s.
- A recursive `lambda` with the same sum, without the list, is 93 bytes
  and much slower.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 88 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000379), CC BY-SA 4.0.
