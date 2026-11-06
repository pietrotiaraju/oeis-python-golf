# A000294

> Expansion of g.f. Product_{k >= 1} (1 - x^k)^(-k*(k+1)/2).
> — [OEIS A000294](https://oeis.org/A000294)

Offset 0: 1, 1, 4, 10, 26, 59, 141, 310, 692, 1483, 3162, 6583, 13602, …

This is MacMahon's guess for the solid partitions; the real counts are
[A000293](../A000293/), which differ from n = 6 on.

### Python 3 — 85 bytes

```python
*R,n=1,0
while[print(R[-1])]:n-=2;R+=sum(d*d*~-d*sum(R[d::d])for d in range(n,0))//n,
```

**How it works**

- The product is the Euler transform of the triangular numbers
  Tₖ = k(k + 1)/2, so the log-derivative recurrence is
  **m·a(m) = Σₖ k·Tₖ·Σⱼ a(m − jk) = Σₖ k²(k + 1)/2 · Σⱼ a(m − jk)**, the
  [A000219](../A000219/) program with weight k(k + 1)/2 for k.
- With d = −k, `d*d*~-d` is d²(d − 1) = −k²(k + 1), twice the weight with
  the sign flipped, and `R[d::d]` reads a(m − k), a(m − 2k), … back from
  the end of the list.
- The factor 2 goes into n: it steps by −2, so n = −2m and `//n` divides
  the doubled, negated sum by −2m exactly. `range(n,0)` then also runs
  d = −2m, …, −m − 1, but those slices start before the beginning of the
  list and are empty. This is 3 bytes under `n-=1` with `//n//2`.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 0.8·n^(3/4) digits (141 at n = 1000), so the 4300-digit int-to-str
  limit is near n = 10⁵, far beyond what the program reaches.
- About 7000 terms in 60 s here; the bar is the whole b-file (1001 terms),
  which takes under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000294), CC BY-SA 4.0.
