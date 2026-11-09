# A001360

> Crystal ball sequence for hyperbolic tessellation 3^7 (from triangle group (2,3,7)).
> — [OEIS A001360](https://oeis.org/A001360)

Offset 0: 1, 8, 29, 85, 232, 617, 1625, 4264, 11173, 29261, 76616, 200593, …

### Python 3 — 33 bytes

```python
a=b=7
while[print(a-6)]:a+=b;b+=a
```

**How it works**

- The 3^7 tessellation has coordination sequence [A001354](../A001354/):
  1, then 7·F(2k) for k ≥ 1 (F = Fibonacci), from its growth series
  (1 + 4x + x²)/(1 − 3x + x²). The crystal ball adds them up, and the
  telescoping sum Σ_{k=1}^{n} F(2k) = F(2n+1) − 1 gives

  a(n) = 1 + 7·(F(2n+1) − 1) = 7·F(2n+1) − 6,

  which also holds at n = 0 (7·1 − 6 = 1).
- `a+=b;b+=a` steps a pair of consecutive Fibonacci numbers two places at
  once: from (F(2n+1), F(2n+2)) it makes (F(2n+3), F(2n+4)). Started at
  `a=b=7`, i.e. 7·(F(1), F(2)), `a` runs through 7·F(2n+1), and the print
  subtracts 6.

**Notes**

- Folding the −6 into the update instead, `a,b=1,7` /
  `while[print(a)]:a+=b;b+=a+6`, is 35 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (a(0) to a(1000)); the whole of it prints
  instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001360), CC BY-SA 4.0.
