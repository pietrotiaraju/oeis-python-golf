# A000028

> Let k = p_1^e_1 p_2^e_2 p_3^e_3 ... be the prime factorization of n.
> Sequence gives k such that the sum of the numbers of 1's in the binary
> expansions of e_1, e_2, e_3, ... is odd.
> — [OEIS A000028](https://oeis.org/A000028)

Offset 1: 2, 3, 4, 5, 7, 9, 11, 13, 16, 17, 19, 23, 24, 25, 29, 30, 31, …

### Python 3 — 88 bytes

```python
f=[0,n:=1]
while[f[n]<0==print(n)]:n+=1;f+=-sum(f[d]for d in range(1,n)if n%d<(d*d!=n)),
```

**How it works**

- Let f(n) = (−1)^(Σ popcount(eᵢ)), so the sequence is the n with f(n) = −1.
  f is multiplicative and f(pᵉ) = t(e), the ±1 Thue–Morse sign.
- Over the divisors of pᵉ, Σ t(j) for j = 0…e cancels in pairs
  (t(2i+1) = −t(2i)): it is 0 when e is odd and t(e) = t(e/2) when e is even.
  Multiplying over the primes gives **Σ_{d|n} f(d) = f(√n) if n is a square,
  else 0**, that is, the divisors other than √n always sum to 0.
- For n ≥ 2 this solves for f(n): **f(n) = −Σ f(d)** over the divisors
  d < n with d² ≠ n, starting from f(1) = 1. No factoring is needed.
- `f=[0,n:=1]` sets n = 1 and f = [0, 1], so `f[d]` is f(d); the 0 is padding.
- `n%d<(d*d!=n)` is "d divides n and d ≠ √n": for d = √n the right side is
  `False`, and `n%d<0` never holds.
- `f+=-sum(…),` appends f(n) as a one-tuple. The loop condition
  `[f[n]<0==print(n)]` is a non-empty list, so always true; the chained
  comparison calls `print(n)` only when f(n) < 0. It prints the previous n
  before the body moves on, and skips n = 1.

**Notes**

- Each term sums over n − 1 candidate divisors, so the whole b-file (10 000
  terms, up to 20 000) prints in about 20 s; the bar is the whole b-file in
  60 s.
- This recurrence is the Lambek–Moser splitting in the comments of the OEIS
  page: A000028 and its complement A000379 are the unique split of the
  positive integers where products of two distinct elements of either class
  occur equally often.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 88 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000028), CC BY-SA 4.0.
