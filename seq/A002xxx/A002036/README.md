# A002036

> Compressed primes: a(n) is the nearest integer to prime(n)/log prime(n).
> — [OEIS A002036](https://oeis.org/A002036)

Offset 1: 3, 3, 3, 4, 5, 5, 6, 6, 7, 9, 9, 10, 11, 11, 12, 13, 14, 15, 16, 17, …

### Python 3 — 154 bytes

```python
from decimal import*
c=getcontext();p=F=1
while p:=p+1:
 while round((y:=p/c.ln(p))-(d:=y/c.prec**9))<round(y+d):c.prec+=9
 F%p and print(round(y));F*=p*p
```

**How it works**

- **Primes.** F = ((p − 1)!)², so by Wilson's theorem F mod p is 1 for
  a prime p and 0 otherwise; `F*=p*p` moves on to the next p.
- **Correct rounding.** `c` is the active decimal context, P = `c.prec`
  digits (28 at start). The decimal module documents `ln` as correctly
  rounded, and `/` rounds correctly too, so y = p/ln p is computed with
  relative error below 10.1·10⁻ᴾ. The margin d = y/P⁹ is at least
  99·10⁻ᴾ·y for every P ≥ 28 (P⁹ < 10ᴾ/100 there), far more than that
  error plus the half-ulp roundings of y − d and y + d. So the computed
  y − d and y + d lie strictly below and above x = p/ln p.
- **Deciding the integer.** `round` is monotone, so when y − d and y + d
  round to the same integer, x rounds to it as well, and so does y,
  which is printed. Otherwise the precision goes up by 9 digits and
  everything is recomputed; P never goes down.
- **It always decides.** x is never a half-integer: x = k + ½ would make
  ln p = 2p/(2k + 1) a nonzero rational, so p = e^(2p/(2k+1)) would be
  transcendental (Hermite–Lindemann), not an integer. As P grows, d
  shrinks to 0 and y − d, y + d close in on x, so the loop ends for
  every p. No precision fixed in advance could be proved enough, which
  is why the program checks each p.

**Notes**

- Every comparison is exact, so the program is right for every n.
  Within the b-file the default 28 digits always decide at once.
- `c.ln(p)` takes the int directly; `Decimal(p).ln()` is 8 bytes
  longer. Nothing is printed for composite p, but its y is computed
  anyway, which is shorter than testing first.
- The b-file has 1000 terms (primes up to 7919); the bar is the whole
  b-file in 60 s, which takes under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 154 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002036), CC BY-SA 4.0.
