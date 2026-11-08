# A001001

> Number of sublattices of index n in generic 3-dimensional lattice.
> — [OEIS A001001](https://oeis.org/A001001)

Offset 1: 1, 7, 13, 35, 31, 91, 57, 155, 130, 217, 133, 455, 183, 399, 403, 651, …

### Python 3 — 78 bytes

```python
r=[1]
for n in r:r+=n+1,;print(sum(d*e for e in r for d in r[e-1::e]if n%d<1))
```

**How it works**

- A sublattice of index n has a unique Hermite normal form: a triangular
  basis matrix with diagonal d₁, d₂, d₃ (d₁d₂d₃ = n) whose off-diagonal
  entries are reduced modulo the diagonal entries, d₂·d₃² choices in all.
  So a(n) = Σ d₂d₃² over d₁d₂d₃ = n. Putting d = d₂d₃, the inner sum is
  Σ_{d₃|d} d·d₃ = d·σ(d), so a(n) = Σ_{d|n} d·σ(d): a sum of d·e over the
  pairs e | d | n.
- `r` is the counter list of [A000203](../../A000xxx/A000203/): `for n in r`
  appends n+1 before the sum, so r = [1, …, n+1], and n+1 never divides n.
- The outer loop takes e from r and `r[e-1::e]` lists its multiples
  e, 2e, 3e, … up to n+1; keeping the d with d | n gives exactly the pairs
  e | d | n (e | d | n forces e | n, so no test on e is needed).

**Notes**

- Exact integer arithmetic; only the normal form above is used.
- A term costs n/1 + n/2 + … ≈ n ln n steps: 9500 to 10 300 terms in
  60 s. The b-file has 10 000 terms; the bar is 7500 terms in 60 s.
- Restricting the inner loop to divisors with an empty slice,
  `for d in r for e in r[n%d*d:d]if d%e<1` (r[n%d*d:d] is empty unless
  d | n), is 79 bytes and twice as fast. The plain double loop
  `for d in r for e in r if n%d+d%e<1` is 75 bytes but costs n² per term
  (about 1070 terms in 60 s), far below the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001001), CC BY-SA 4.0.
