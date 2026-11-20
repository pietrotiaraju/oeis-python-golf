# A002121

> a(0) = 1, a(1) = 0, a(2) = -1; for n >= 3, a(n) = - a(n-2) + Sum_{ primes p with 3 <= p <= n} a(n-p).
> — [OEIS A002121](https://oeis.org/A002121)

Offset 0: 1, 0, -1, 1, 1, -1, 0, 2, 0, -2, 2, 4, -3, -2, 8, 1, …

### Python 3 — 93 bytes

```python
a=[1];*P,F,n=1,0
while[print(a[-1]*(-1)**n)]:n+=1;P+=F%n*[n];F*=n*n;a+=-sum(a[-p]for p in P),
```

**How it works**

- The generating function is 1/G(x) with G = 1 + Σ_k (−x)^prime(k)
  = 1 + x² − x³ − x⁵ − x⁷ − … (the entry's formula). This is the title's
  recurrence, a(n) = −a(n − 2) + Σ_{odd p ≤ n} a(n − p), which for n = 1, 2
  (with a(negative) = 0) also gives the initial values 0 and −1.
- **One sign for every prime.** Replacing x by −x, h(n) = (−1)^n·a(n) has
  generating function 1/(1 + Σ_k x^prime(k)), so h(0) = 1 and
  h(n) = −Σ_{p ≤ n} h(n − p) over all primes, with no special case for 2.
  The list holds h (`a[-p]` is h(n − p)), and the print multiplies by
  (−1)^n. A direct version with the sign `(p%2*2-1)` per prime is 1 byte
  longer.
- Primes come from Wilson's theorem, as in the [A000607](../../A000xxx/A000607/)
  record: F = ((m − 1)!)², so F mod m is 1 when m is prime and 0 otherwise
  (also for m = 1, and for m = 4, where F = 36); `F*=n*n` then moves F on
  to (m!)².
- The starred assignment sets P = [], F = 1, n = 0.

**Notes**

- The whole b-file, 1001 terms (n = 0 to 1000), takes about 0.1 s here, so
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002121), CC BY-SA 4.0.
