# A000902

> Expansion of e.g.f. (1/2)*(exp(2*x + x^2) + 1).
> — [OEIS A000902](https://oeis.org/A000902)

Offset 0: 1, 1, 3, 10, 38, 156, 692, 3256, 16200, 84496, 460592, 2611104, …

### Python 3 — 49 bytes

```python
a=1;n=b=0
while[print(a+1>>1)]:a,b=2*a+n*b,a;n+=2
```

**How it works**

- Let b(n) = n!·[xⁿ] exp(2x+x²) ([A000898](../A000898/)). Differentiating
  the e.g.f. gives E′ = (2+2x)E, so b(n+1) = 2b(n) + 2n·b(n−1), with
  b(0) = 1. The second line is the [A000898](../A000898/) program: `a` is
  b(k), `b` is b(k−1) and `n` holds 2k, so `n*b` is the 2k·b(k−1) term.
- Here a(n) = (b(n) + [n = 0])/2: b(0) = 1 gives a(0) = 1, and for n ≥ 1
  b(n) is even (the recurrence doubles both terms). So `a+1>>1` prints
  a(n) for every n: (1+1)>>1 = 1 at the start, and b/2 afterwards since
  adding 1 to an even number does not change its half.
- A recurrence on a(n) itself, a(n) = 2a(n−1) + (2n−2)a(n−2), only holds
  from n = 3 (it would need a(0) = 1/2), so the halving on output is cheaper
  than a special start.

**Notes**

- Exact integer arithmetic, correct for every n. Checked against the
  b-file and, up to a(999), against Bingham's sum
  Σ 2^(n−2r−1)·n!/(r!(n−2r)!).
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s. The program prints 2602 terms at once and then stops with a
  `ValueError` at the 4300-digit int-to-str limit of Python 3.11+.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000902), CC BY-SA 4.0.
