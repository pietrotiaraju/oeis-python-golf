# A000915

> Stirling numbers of first kind s(n+4, n).
> — [OEIS A000915](https://oeis.org/A000915)

Offset 1: 24, 274, 1624, 6769, 22449, 63273, 157773, 357423, 749463, 1474473, 2749747, 4899622, …

### Python 3 — 63 bytes

```python
a=b=c=d=m=0
while[0<a!=print(a)]:a+=m*d;d+=m*c;c+=m*b;b+=m;m+=1
```

**How it works**

- Up to sign, s(m, k) is the coefficient of xᵏ in x(x+1)···(x+m−1), so
  s(n+4, n) is the fourth elementary symmetric function e₄ of 1, 2, …,
  n+3: the coefficient of x⁴ in (1+x)(1+2x)···(1+(n+3)x).
- The program builds that product one factor 1 + m·x at a time, cut at
  degree 4: a = e₄, d = e₃, c = e₂, b = e₁. Multiplying by 1 + m·x turns
  each eⱼ into eⱼ + m·eⱼ₋₁ (with e₀ = 1, so `b+=m`). Done top down, every
  line still reads the old value of the line below it, so four plain
  in-place updates with the same multiplier m need no tuple.
- The factors start at m = 0, which changes nothing, so all variables start
  at 0 in one chain `a=b=c=d=m=0`. After the pass with factor m = k,
  a = e₄(1, …, k) = s(k+1, k−3): it is 0 until four factors are in.
- `0<a!=print(a)` skips those zeros: a chained comparison stops at `0<a`
  when a = 0, so print is not called; for a > 0 it prints, and a != None
  is true. The first line is a(1) = 24 (factors 1–4), then one term per
  pass. That is 5 bytes; starting from the state after three factors
  (`a=0;b=d=6;c=11;m=4`) costs more.

**Notes**

- Other versions: the diagonal recurrence s(n+j, n) = s(n+j−1, n−1) +
  (n+j−1)·s(n+j−1, n) with a counter that changes between the lines,
  `n=1;a=b=c=d=0` / `while 1:b+=n;n+=1;c+=n*b;d+=c*-~n;a+=d*(n+2);print(a)`,
  is 67 bytes; the closed form C(n+4, 5)·(15n³ + 150n² + 485n + 502)/48 is
  over 75 bytes with `math.comb`.
- Exact integer arithmetic, so the program is right for every n. a(n) is a
  polynomial of degree 8 in n, so the 4300-digit int-to-str limit is out of
  reach.
- The b-file has 1000 terms; they print in under 0.1 s here. The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000915), CC BY-SA 4.0.
