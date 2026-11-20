# A002123

> a(1) = 0, a(2) = 0; for n > 2, a(n) - a(n-3) - a(n-5) - ... - a(n-p) = n if n is prime, otherwise = 0, where p = largest prime < n.
> — [OEIS A002123](https://oeis.org/A002123)

Offset 1: 0, 0, 3, 0, 5, -3, 7, -8, 3, -15, 22, -15, 39, -35, 38, -72, …

### Python 3 — 95 bytes

```python
a=[0];*P,F,n=2,0
while 1:n-=1;P+=[n][:F%-n];F*=n*n;a[0]=n;a+=-sum(a[p]for p in P),;print(a[-1])
```

**How it works**

- **The data, not the title's signs.** The title reads
  a(n) − a(n − 3) − a(n − 5) − … = n·[n prime], but the terms satisfy it with
  plus signs: a(6) = −3, and a(6) + a(3) + a(1) = −3 + 3 + 0 = 0, while
  a(6) − a(3) − a(1) = −6. The entry's Haskell program uses
  a(n) = n·[n prime] − Σ_{odd p < n} a(n − p), and so do all 1000 terms of
  the b-file; this page follows it. Read with odd primes only, the same rule
  gives a(1) = a(2) = 0, the initial values. (In generating functions:
  A(x) = x·S′(x)/(1 + S(x)) with S = Σ_{odd p} x^p.)
- **Slot.** With a(0) set to −n, the term n·[n odd prime] is the p = n term
  of the sum: a(n) = −Σ_{odd p ≤ n} a(n − p). The counter runs downwards
  (n = −m), so `a[0]=n` is that slot and `a[p]`, with `P` holding the
  negated odd primes, is a(m − p).
- Odd primes come from Wilson's theorem with an extra factor 2:
  F = 2·((m − 1)!)², so F mod m is 2 when m is an odd prime, and 0 for
  m = 1, for m = 2, for m = 4 (F = 72) and for every other composite m.
  `[n][:F%-n]` therefore adds −m to `P` exactly once for an odd prime m
  (a slice `[:2]` of a one-element list) and nothing otherwise; `F*=n*n`
  moves F on to 2·(m!)². The starred assignment sets P = [], F = 2, n = 0.

**Notes**

- The whole b-file, 1000 terms (n = 1 to 1000), takes about 0.1 s here, so
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 95 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002123), CC BY-SA 4.0.
