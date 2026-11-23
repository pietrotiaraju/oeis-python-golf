# A002215

> Number of polyhexes with n hexagons, having reflectional symmetry (see Harary and Read for precise definition).
> — [OEIS A002215](https://oeis.org/A002215)

Offset 1: 1, 1, 2, 3, 6, 10, 20, 36, 72, 137, 274, 543, …

### Python 3 — 73 bytes

```python
x=1;y=m=2
while[print(x),print(y//2)]:m+=1;x,y=y,((6*m-9)*y-5*(m-3)*x)//m
```

**How it works**

- **Generating function** (Harary and Read 1970, eq. (16), quoted in the
  entry): z + (1 + 2z)U(z²), where U(z) = A(z) − 1 and A = 1, 1, 3, 10,
  36, … is the g.f. of [A002212](../A002212/). So a(1) = 1, and for k ≥ 1
  a(2k) = Aₖ and a(2k + 1) = 2Aₖ.
- **Pairs.** Each pass prints a(2k + 1), a(2k + 2) = 2Aₖ, Aₖ₊₁ for
  k = 0, 1, 2, …. With A₀ read as 1/2 the first pair is 1, 1, which is
  a(1), a(2). So `x`, `y` hold 2Aₖ, 2Aₖ₊₁ (starting 1, 2), and the
  prints are `x` and `y//2`.
- **Recurrence.** (k + 1)Aₖ = 3(2k − 1)Aₖ₋₁ − 5(k − 2)Aₖ₋₂ (proved on
  the [A002212 page](../A002212/)); with m = k + 1 it reads
  m·Aₖ = (6m − 9)Aₖ₋₁ − 5(m − 3)Aₖ₋₂. It is linear, so it holds for the
  doubled values too, and at k = 2 (m = 3) the A₀ term has coefficient
  0, so the 1/2 does no harm. `y=m=2` starts m one below its first use.

**Notes**

- Exact integers: right for every n. The whole b-file (200 terms) comes in
  a few hundredths of a second; the bar is all of it in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002215), CC BY-SA 4.0.
