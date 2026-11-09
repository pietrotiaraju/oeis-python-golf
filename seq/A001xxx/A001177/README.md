# A001177

> Fibonacci entry points: a(n) = least k >= 1 such that n divides Fibonacci number F_k (=A000045(k)).
> — [OEIS A001177](https://oeis.org/A001177)

Offset 1: 1, 3, 4, 6, 5, 12, 8, 6, 12, 15, 10, 12, 7, 24, 20, 12, 9, 12, 18, 30, …

### Python 3 — 62 bytes

```python
n=k=1
while[print(k)]:
 n+=1;a=b=k=1
 while a%n:a,b=b,a+b;k+=1
```

Siblings: the Pisano periods [A001175](../A001175/) and the zeros per period
[A001176](../A001176/).

**How it works**

- Start at F_1 = F_2 = 1 with k = 1 and step `a,b=b,a+b;k+=1` until n divides
  a = F_k. The first such k is printed.
- The loop always stops: F_k ≡ 0 (mod n) at k = π(n), the Pisano period of
  [A001175](../A001175/), and the entry point is at most 2n.
- For n = 1, `a%n` is 0 at once and a(1) = 1. `while[print(k)]:` prints that
  before the first pass.
- The numbers are kept exact: reducing with `b%n` would cost 2 bytes.

**Notes**

- Exact for every n.
- The whole b-file (10000 terms) in about 17 s on the PC it was written on;
  the bar is all 10000 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001177), CC BY-SA 4.0.
