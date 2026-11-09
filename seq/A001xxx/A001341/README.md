# A001341

> Expansion of e.g.f. 6*exp(x)/(1-x)^4.
> — [OEIS A001341](https://oeis.org/A001341)

Offset 0: 6, 30, 174, 1158, 8742, 74046, 696750, 7219974, 81762438, 1005151902, …

Equivalently a(n) = Σ_{k=0}^{n} (k+3)!·C(n,k), since 6/(1−x)⁴ =
Σ (k+3)!·x^k/k!.

### Python 3 — 45 bytes

```python
b=n=0;d=6
while[print(b:=b+d)]:d=n*d+4*b;n+=1
```

**How it works**

- The e.g.f. f = 6e^x/(1−x)⁴ has f′/f = 1 + 4/(1−x), so
  (1−x)·f′ = (5−x)·f. Comparing coefficients of x^n/n! (f′ shifts the
  index up, x·f′ gives n·a(n), x·f gives n·a(n−1)):
  a(n+1) − n·a(n) = 5·a(n) − n·a(n−1), that is
  a(n+1) = (n+5)·a(n) − n·a(n−1).
- With the difference d(n) = a(n) − a(n−1) this becomes
  d(n+1) = (n+4)·a(n) − n·a(n−1) = n·d(n) + 4·a(n), and
  a(n+1) = a(n) + d(n+1).
- The loop prints b = b + d, which is a(n), then computes d(n+1) from the
  new b with the counter at n. The start b = 0, d = 6 prints a(0) = 6; the
  next d is 0·d + 4·6 = 24, since n = 0 wipes out the old d, so no a(−1)
  is needed.

**Notes**

- Keeping g(n) = a(n) − n·a(n−1) instead, g(n+1) = g(n) + 3·a(n), gives
  `a=2;g=n=0` / `while[print(a:=a*n+(g:=g+3*a))]:n+=1`, 46 bytes; the
  plain pair `a,b=b,n*(b-a)+5*b`, 48; the closed form
  (n³ + 3n² + 5n + 2)·b(n) + n² + 3n + 4 with b = A000522, 63.
- Exact integer arithmetic, so the program is right for every n. It stops
  after a(1555): a(1556) is the first term with more than 4300 digits, the
  int-to-str limit of Python 3.11+.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001341), CC BY-SA 4.0.
