# A002122

> a(n) = Sum_{t=0..n} g(t)*g(n-t) where g(t) = A002121(t).
> — [OEIS A002122](https://oeis.org/A002122)

Offset 0: 1, 0, -2, 2, 3, -4, -1, 8, -1, -10, 9, 16, -18, -12, 42, 4, …

### Python 3 — 119 bytes

```python
a=[1];*P,F,n=1,0
while[print(sum(map(int.__mul__,a,a[::-1]))*(-1)**n)]:n+=1;P+=F%n*[n];F*=n*n;a+=-sum(a[-p]for p in P),
```

**How it works**

- The self-convolution of [A002121](../A002121/), whose terms g(t) satisfy
  g(t) = (−1)^t·h(t) with h(0) = 1 and h(n) = −Σ_{p ≤ n} h(n − p) over all
  primes (see that page). Since (−1)^t·(−1)^(n−t) = (−1)^n,
  a(n) = (−1)^n·Σ_t h(t)·h(n − t).
- The loop is the A002121 record; the print pairs the list h(0), …, h(n)
  with its reverse, `map(int.__mul__,a,a[::-1])`, and multiplies the sum by
  (−1)^n.
- Primes come from Wilson's theorem, as in the [A000607](../../A000xxx/A000607/)
  record: F = ((m − 1)!)², so F mod m is 1 when m is prime and 0 otherwise
  (also for m = 1, and for m = 4, where F = 36); `F*=n*n` then moves F on
  to (m!)².
- The starred assignment sets P = [], F = 1, n = 0.

**Notes**

- The whole b-file, 1001 terms (n = 0 to 1000), takes about 0.2 s here, so
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 119 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002122), CC BY-SA 4.0.
