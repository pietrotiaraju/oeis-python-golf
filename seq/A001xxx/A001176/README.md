# A001176

> Number of zeros in fundamental period of Fibonacci numbers mod n.
> — [OEIS A001176](https://oeis.org/A001176)

Offset 1: 1, 1, 2, 1, 4, 2, 2, 2, 2, 4, 1, 2, 4, 2, 2, 2, 4, 2, 1, 2, …

### Python 3 — 74 bytes

```python
n=z=1
while[print(z)]:
 n+=1;a=b=1;z=0
 while a%n|~-b%n:a,b=b%n,a+b;z+=a<1
```

Siblings: the Pisano periods [A001175](../A001175/) and the entry points
[A001177](../A001177/).

**How it works**

- Run the Fibonacci pair modulo n through one full period, exactly as in
  [A001175](../A001175/): from (F_1, F_2) = (1, 1) until it is (0, 1) again,
  that is, k = 2, 3, …, π(n). After each step `a` is F_k mod n, and
  `z+=a<1` counts the zeros. The last step lands on F_π ≡ 0, so it is counted.
- The first index of the period, k = 1, has F_1 = 1, which is a zero only for
  n = 1. That case is the `z=1` printed by `while[print(z)]:` before the first
  pass (the period mod 1 is 1, with one zero); inside the loop n ≥ 2 and z
  starts at 0.
- Here the residues are reduced (`b%n`): the exact version needs `a%n<1` for
  the count, so it is no shorter.

**Notes**

- Exact for every n. The zeros are at the multiples of the entry point
  [A001177](../A001177/), so the count is π(n)/α(n), which is always 1, 2 or 4.
- The b-file has 1000 terms; all of them come in under a second, and the bar
  is all 1000 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001176), CC BY-SA 4.0.
