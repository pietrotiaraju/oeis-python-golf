# A000100

> a(n) is the number of compositions of n in which the maximal part is 3.
> — [OEIS A000100](https://oeis.org/A000100)

Offset 0: 0, 0, 0, 1, 2, 5, 11, 23, 47, 94, 185, 360, 694, 1328, 2526, …

### Python 3 — 57 bytes

```python
a=b=x=y=0;z=1
while[print(b)]:a,b,x,y,z=b,a+b+x,y,z,x+y+z
```

**How it works**

- Compositions of n with parts at most 3 are counted by the tribonacci
  number T(n) = [A000073](../A000073/)(n+2) (1, 1, 2, 4, 7, …), and those
  with parts at most 2 by the Fibonacci number F(n) = A000045(n+1)
  (1, 1, 2, 3, 5, …). The ones whose largest part is exactly 3 are the
  difference: a(n) = T(n) − F(n).
- Write F = T − a in F(n) = F(n−1) + F(n−2) and use T(n) = T(n−1) +
  T(n−2) + T(n−3): what is left is a(n) = a(n−1) + a(n−2) + T(n−3).
  So a is a Fibonacci-like sum fed by a tribonacci stream.
- `a`, `b` hold a(n−1), a(n); `x`, `y`, `z` hold T(n−2), T(n−1), T(n).
  One tuple assignment steps both: `a+b+x` is a(n+1) and `x+y+z` is
  T(n+1).
- Run backwards, T is 0, 0, 1 at n = −2, −1, 0 and a(−1) = 0, so the
  whole start state is `a=b=x=y=0;z=1`.
- `print(b)` sits in the loop condition: `[None]` is a non-empty list, so
  the loop never ends.

**Notes**

- The sequence has an order-5 recurrence (g.f. x³/((1−x−x²)(1−x−x²−x³)),
  no common factor), so any linear update needs five numbers.
- Keeping T and F apart and printing the difference,
  `x=y=u=0;z=v=1` + `while[print(z-v)]:x,y,z,u,v=y,z,x+y+z,v,u+v`, is
  58 bytes; a(n) = a(n−1) + a(n−2) + a(n−3) + F(n−2) needs the start
  a(−2) = −1 and comes out longer still.
- A search over every update in which each new variable is a sum of old
  ones, with only 8 terms in all (one `+` fewer than here), found 240
  matrices with the right characteristic polynomial but none that prints
  this sequence from any integer start state.
- Exact integers, so every term is right. The whole b-file (201 terms)
  prints instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000100), CC BY-SA 4.0.
