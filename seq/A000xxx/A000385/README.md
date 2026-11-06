# A000385

> Convolution of A000203 with itself.
> — [OEIS A000385](https://oeis.org/A000385)

Offset 1: 1, 6, 17, 38, 70, 116, 185, 258, 384, 490, 686, 826, 1124, …

### Python 3 — 75 bytes

```python
r=[1]
for n in r:r+=n+1,;print(sum(d*(5*d*d-6*n-5)for d in r if~n%d<1)//12)
```

**How it works**

- a(n) = Σ σ(k)·σ(n + 1 − k) over k = 1…n, the convolution of σ
  ([A000203](../A000203/)) at m = n + 1.
- Besge's identity (1862; it follows from the Eisenstein series E₂² =
  E₄ + 12q·dE₂/dq, so it holds for every m):
  Σ_{k=1}^{m−1} σ(k)σ(m − k) = (5σ₃(m) − (6m − 1)σ(m))/12.
  This is the formula of Robert Israel on the OEIS page.
- Both divisor sums go into one: the program adds d(5d² − 6m + 1) =
  d(5d² − 6n − 5) over the divisors d of m = n + 1 and divides by 12,
  which is exact by the identity.
- The loop is the growing list of [A000203](../A000203/): at step n the
  list `r` is 1, 2, …, n + 1, so it holds every divisor of m = n + 1.
  `~n` is −(n + 1), so `~n%d<1` tests d | n + 1, a byte under `-~n%d<1`.

**Notes**

- Exact integers; correctness for every n is Besge's identity.
- 76 bytes (the first version): a counter m = 2, 3, … with
  `while[print(sum(5*d**3-6*m*d+d for d in range(1,m+1)if m%d<1)//12)]:m+=1`;
  `d*(5*d*d-6*m+1)for …` and negative divisors `range(-m,0)` with
  `m%-d<1` tie with it. A direct convolution
  of a list of σ values with `map(int.__mul__,s,s[::-1])` is about 20
  bytes longer.
- Each term tries m candidate divisors; the whole b-file (10000 terms)
  prints in under 10 s. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 76 | first entry |
| 2026-11-06 | Python 3 | 75 | growing list, divisibility of n + 1 as `~n%d` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000385), CC BY-SA 4.0.
