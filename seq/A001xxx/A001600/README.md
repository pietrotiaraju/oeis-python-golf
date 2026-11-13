# A001600

> Harmonic means of divisors of harmonic numbers.
> — [OEIS A001600](https://oeis.org/A001600)

Offset 1: 1, 2, 3, 5, 6, 5, 8, 9, 11, 10, 7, 15, 15, 14, 17, 24, 24, 21, 13, 19, 27, 25, …

### Python 3 — 118 bytes

```python
D={};k=0
while 1:
 k+=1;L=D.pop(k,[])+[k]
 for d in L:D[k+d]=D.get(k+d,[])+[d]
 h=k*len(L);h%sum(L)or print(h//sum(L))
```

**How it works**

- The harmonic mean of the divisors of k is k·τ(k)/σ(k), where τ(k) counts
  the divisors and σ(k) adds them up. The harmonic numbers
  ([A001599](../A001599/)) are the k where this is an integer, and the
  term is that integer, in the order of the k.
- The divisors come from an incremental sieve: `D` maps each upcoming
  number to the divisors found for it so far. At k, `D.pop(k,[])` holds
  every divisor d < k (each one passed on from its previous multiple), and
  `+[k]` adds k itself; then each divisor moves on to its next multiple,
  `D[k+d]`. So `L` is the full divisor list, `len(L)` = τ(k) and
  `sum(L)` = σ(k).
- With h = k·τ(k), the program prints h/σ(k) when σ(k) divides h.

**Notes**

- Every k is tested with exact integers, so the program is right for every
  n; no conjecture about harmonic numbers is used.
- Each k costs τ(k) dict updates, and the dict keeps one pending entry per
  divisor, about 150 bytes per k passed: the 28th term (k = 695520) comes
  after about 10 s here, at about 110 MB. The timeout is 20 s to keep the
  memory in check, and the bar is 28 terms, as for A001599.
- The terms are small (the b-file's 937 terms are at most 1074), so a table
  of 28 of them is shorter than the program, which therefore goes through
  review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 118 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001600), CC BY-SA 4.0.
