# A000472

> a(n) = a(n-1)^2 + (a(n-2) + 1)*(a(n-1) - a(n-2)^2).
> — [OEIS A000472](https://oeis.org/A000472)

Offset 1: 2, 5, 28, 802, 643726, 414383582242, 171713753231982206218246, …

### Python 3 — 39 bytes

```python
a=2;d=1
while[print(a)]:a,d=a*a+d,d*-~a
```

**How it works**

- Put d(n) = a(n+1) − a(n)². The recurrence says exactly
  d(n) = (a(n−1) + 1)·d(n−1), so the pair (a, d) steps as
  a ← a² + d, d ← (a + 1)·d, with both right-hand sides read before the
  assignment.
- a(1) = 2 and a(2) = 5 give d(1) = 1, the start `a=2;d=1`.
- `d*-~a` is d·(a+1): `-~a` is a + 1 and binds tighter than `*`, 2 bytes
  under `d*(a+1)`.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 14 terms (up to a(14)); the bar is the whole b-file in
  60 s.
- The digit count roughly doubles each step: a(14) has 2975 digits and
  a(15) more than 4300, so printing stops after a(14) with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 41 | first entry |
| 2026-11-07 | Python 3 | 39 | `d*-~a` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000472), CC BY-SA 4.0.
