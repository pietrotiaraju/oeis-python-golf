# A002120

> a(1) = 0, a(2) = -2; for n > 2, a(n) + a(n-2) - a(n-3) - a(n-5) - ... - a(n-p) = (-1)^(n+1)*n if n is prime, otherwise = 0, where p = largest prime < n.
> — [OEIS A002120](https://oeis.org/A002120)

Offset 1: 0, -2, 3, 2, 0, 1, 7, 2, -6, 8, 22, -7, 0, 33, 3, -14, …

### Python 3 — 101 bytes

```python
a=[0];*P,F,n=1,0
while 1:n+=1;P+=F%n*[n];F*=n*n;a[0]=n;a+=-sum(a[-p]for p in P),;print(a[-1]*(-1)**n)
```

**How it works**

- **The rule.** Write s_p = (−1)^(p+1): −1 for p = 2 and +1 for the odd
  primes. The title says a(n) = Σ_{p < n} s_p·a(n − p) + s_n·n·[n prime] for
  n > 2. If the slot a(0) is set to n, the last term is the p = n term of the
  sum: a(n) = Σ_{p ≤ n} s_p·a(n − p). For n = 1 this gives 0 and for n = 2 it
  gives −a(0) = −2, the two initial values, so one rule covers every n. (In
  generating functions: A(x)·G(x) = −x·G′(x) with G = 1 + Σ_k (−x)^prime(k),
  the denominator of [A002121](../A002121/).)
- **One sign for every prime.** Put u(m) = (−1)^m·a(m). Then
  u(n) = Σ_p s_p·(−1)^p·u(n − p), and s_p·(−1)^p = −1 for every prime p, so
  u(n) = −Σ_{p ≤ n} u(n − p), with the slot u(0) = a(0) = n. The list holds
  u: `a[0]=n` sets the slot, `a[-p]` is u(n − p), and the print multiplies by
  (−1)^n. This saves the per-prime sign `(p%2*2-1)` (2 bytes net).
- Primes come from Wilson's theorem, as in the [A000607](../../A000xxx/A000607/)
  record: F = ((m − 1)!)², so F mod m is 1 when m is prime and 0 otherwise
  (also for m = 1, and for m = 4, where F = 36); `F*=n*n` then moves F on
  to (m!)².
- The starred assignment sets P = [], F = 1, n = 0.

**Notes**

- The whole b-file, 1000 terms (n = 1 to 1000), takes about 0.1 s here, so
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 101 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002120), CC BY-SA 4.0.
