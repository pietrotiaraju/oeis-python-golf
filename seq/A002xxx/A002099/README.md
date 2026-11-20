# A002099

> G.f.: -1 + Product_{k>=1} (1 + prime(k)*x^prime(k)).
> — [OEIS A002099](https://oeis.org/A002099)

Offset 0: 0, 0, 2, 3, 0, 11, 0, 17, 15, 14, 51, 11, 77, 35, 103, 131, …

### Python 3 — 98 bytes

```python
*Q,F,n=1,1,0
while[print(Q[n]-0**n)]:n+=1;k=F%n*n;Q=[x+k*y for x,y in zip(Q+[0]*n,[0]*n+Q)];F*=n*n
```

**How it works**

- `Q` is the whole polynomial ∏_{p ≤ n} (1 + p·x^p) over the primes found so
  far, never truncated. At step n, k = n if n is prime and 0 otherwise, and
  `zip(Q+[0]*n,[0]*n+Q)` pairs each coefficient of Q with the coefficient n
  places lower, so the new list is Q + k·x^n·Q: the product times
  (1 + n·x^n) when n is prime, and Q itself, n zeros longer, when it is not.
- Primes p > n only change the coefficients of x^(>n), so after step n the
  coefficient Q[n] is final. It is a(n) for n ≥ 1; for n = 0 the "−1" of the
  generating function turns Q[0] = 1 into a(0) = 0, which is `-0**n`
  (0**0 = 1).
- Primes come from Wilson's theorem, as in the [A000607](../../A000xxx/A000607/)
  record: F = ((m − 1)!)², so F mod m is 1 when m is prime and 0 otherwise
  (also for m = 1, and for m = 4, where F = 36); `k=F%n*n` reads it before `F*=n*n` moves F on
  to (m!)².
- The starred assignment sets Q = [1], F = 1, n = 0.

**Notes**

- After n steps the list has 1 + n(n + 1)/2 entries; the whole b-file,
  501 terms (n = 0 to 500), takes about 2.5 s here, so the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 98 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002099), CC BY-SA 4.0.
