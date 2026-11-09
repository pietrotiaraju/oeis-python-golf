# A001342

> E.g.f.: 24*exp(x)/(1-x)^5.
> — [OEIS A001342](https://oeis.org/A001342)

Offset 0: 24, 144, 984, 7584, 65304, 622704, 6523224, 74542464, 923389464, 12331112784, …

Equivalently a(n) = Σ_{k=0}^{n} (k+4)!·C(n,k), since 24/(1−x)⁵ =
Σ (k+4)!·x^k/k!.

### Python 3 — 45 bytes

```python
b=d=4;n=0
while[print(b:=b+5*d)]:d=n*d+b;n+=1
```

**How it works**

- The e.g.f. f = 24e^x/(1−x)⁵ has f′/f = 1 + 5/(1−x), so
  (1−x)·f′ = (6−x)·f. Comparing coefficients of x^n/n! (f′ shifts the
  index up, x·f′ gives n·a(n), x·f gives n·a(n−1)):
  a(n+1) = (n+6)·a(n) − n·a(n−1).
- With the difference d(n) = a(n) − a(n−1) this is
  d(n+1) = (n+5)·a(n) − n·a(n−1) = n·d(n) + 5·a(n). The program keeps a
  fifth of it, e(n) = d(n)/5, with e(n+1) = n·e(n) + a(n) and
  a(n+1) = a(n) + 5·e(n+1); 5·e satisfies the recurrence of d, so this
  is the same sequence.
- The loop prints b = b + 5·e, which is a(n), then computes e(n+1) from
  the new b with the counter at n. The start b = e = 4 prints
  4 + 20 = 24 = a(0) and shares one assignment; the next e is
  0·4 + 24 = 24, since n = 0 wipes out the old e, and a(1) = 24 + 120 =
  144.

**Notes**

- Without the factor 5 the start needs b + d = 24, as in `b=n=0;d=24` /
  `while[print(b:=b+d)]:d=n*d+5*b;n+=1`: 46 bytes. Keeping
  g(n) = a(n) − n·a(n−1), g(n+1) = g(n) + 4·a(n), as `a=6;g=n=0` /
  `while[print(a:=a*n+(g:=g+4*a))]:n+=1`, is also 46; the plain pair
  `a,b=b,n*(b-a)+6*b`, 49.
- Exact integer arithmetic, so the program is right for every n. It stops
  after a(1554): a(1555) is the first term with more than 4300 digits, the
  int-to-str limit of Python 3.11+.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001342), CC BY-SA 4.0.
