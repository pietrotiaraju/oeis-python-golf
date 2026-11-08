# A001120

> a(0) = a(1) = 1; for n > 1, a(n) = n*a(n-1) + (-1)^n.
> — [OEIS A001120](https://oeis.org/A001120)

Offset 0: 1, 1, 3, 8, 33, 164, 985, 6894, 55153, 496376, 4963761, …

### Python 3 — 36 bytes

```python
a=n=1
while[print(a)]:a=a*n^1%n;n+=1
```

**How it works**

- a(n) = n·a(n−1) + (−1)ⁿ for n ≥ 2. Every a(n) with n even is odd (a(0) = 1,
  and for even n ≥ 2, n·a(n−1) is even and the +1 makes it odd), so
  n·a(n−1) always has the parity of n, and adding (−1)ⁿ is the same as
  XOR 1, the derangement trick of [A000166](../../A000xxx/A000166/).
- n = 1 breaks the rule (a(1) = 1, not 1·1 − 1): `a*n^1%n` XORs with 1 % n,
  which is 0 at n = 1 and 1 from then on (`%` binds tighter than `^`).

**Notes**

- Starting from a virtual a(0) = 0 instead (`b=n=0`, `b=b*n^1`, printing
  `b+0**n`) is 39 bytes.
- The whole b-file (451 terms) prints instantly; the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001120), CC BY-SA 4.0.
