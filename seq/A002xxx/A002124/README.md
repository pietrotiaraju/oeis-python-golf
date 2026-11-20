# A002124

> Number of compositions of n into a sum of odd primes.
> — [OEIS A002124](https://oeis.org/A002124)

Offset 0: 1, 0, 0, 1, 0, 1, 1, 1, 2, 1, 3, 4, 3, 7, 7, 8, …

### Python 3 — 86 bytes

```python
a=[1];*P,F,n=2,0
while[print(a[-1])]:n-=1;P+=[n][:F%-n];F*=n*n;a+=sum(a[p]for p in P),
```

**How it works**

- Splitting off the last part, a composition of n into odd primes is a
  composition of n − p followed by an odd prime p ≤ n, so a(0) = 1 and
  a(n) = Σ_{odd p ≤ n} a(n − p) (MacMahon's recurrence in the entry).
- The counter runs downwards (n = −m), `P` holds the negated odd primes,
  and `a[p]` is a(m − p) in the list a(0), …, a(m − 1).
- Odd primes come from Wilson's theorem with an extra factor 2:
  F = 2·((m − 1)!)², so F mod m is 2 when m is an odd prime, and 0 for
  m = 1, for m = 2, for m = 4 (F = 72) and for every other composite m.
  `[n][:F%-n]` therefore adds −m to `P` exactly once for an odd prime m
  (a slice `[:2]` of a one-element list) and nothing otherwise; `F*=n*n`
  moves F on to 2·(m!)². The starred assignment sets P = [], F = 2, n = 0.

**Notes**

- The whole b-file, 1001 terms (n = 0 to 1000), takes about 0.1 s here, so
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002124), CC BY-SA 4.0.
