# A001599

> Harmonic or Ore numbers: numbers k such that the harmonic mean of the divisors of k is an integer.
> — [OEIS A001599](https://oeis.org/A001599)

Offset 1: 1, 6, 28, 140, 270, 496, 672, 1638, 2970, 6200, 8128, 8190, 18600, 18620, …

### Python 3 — 106 bytes

```python
D={};k=0
while 1:
 k+=1;L=D.pop(k,[])+[k]
 for d in L:D[k+d]=D.get(k+d,[])+[d]
 k*len(L)%sum(L)or print(k)
```

**How it works**

- The harmonic mean of the divisors of k is k·τ(k)/σ(k) (τ counts the
  divisors, σ adds them up), so k is a term when σ(k) divides k·τ(k).
- The divisors come from an incremental sieve: `D` maps each upcoming
  number to the divisors found for it so far. At k, `D.pop(k,[])` holds
  every divisor d < k (each one was passed on from its previous multiple),
  and `+[k]` adds k itself. Each divisor then moves on to its next
  multiple, `D[k+d]`. So `L` is the full divisor list of k, `len(L)` is
  τ(k) and `sum(L)` is σ(k).
- `k*len(L)%sum(L)or print(k)` prints k when the remainder is 0.

**Notes**

- Exact integer arithmetic over every k, so the program is right for every
  n; it rests on no conjecture (Ore's question whether 1 is the only odd
  term does not matter here).
- Each k costs τ(k) dict updates, and the dict holds one pending entry per
  divisor, about 150 bytes per k passed. a(28) = 695520 comes after about
  10 s here and a(32) = 1089270 after about 21 s, at 170 MB. To keep that
  memory in check the timeout is 20 s, and the bar is 28 terms.
- The entry is marked "changed": a comment of November 2026 corrects the
  10000-term b-file from a(4587) on. The first terms, which are all this
  program reaches, are not affected.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 106 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001599), CC BY-SA 4.0.
