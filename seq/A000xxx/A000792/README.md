# A000792

> a(n) = max{(n - i)*a(i) : i < n}; a(0) = 1.
> — [OEIS A000792](https://oeis.org/A000792)

Offset 0: 1, 1, 2, 3, 4, 6, 9, 12, 18, 27, 36, 54, 81, 108, 162, 243, 324, 486, 729, 972, …

### Python 3 — 47 bytes

```python
q=[1,1,2,3,4]
while[print(q.pop(0))]:q+=3*q[1],
```

**How it works**

- a(n) is the largest product of a partition of n (OEIS). A part k ≥ 5
  can be split into 2 and k − 2 with 2(k−2) > k, a 4 into 2 + 2, a 1 never
  helps, and three 2's lose to two 3's. So for n ≥ 5 every best partition
  contains a 3, and a(n) = 3·a(n−3).
- `q` holds the next five terms. After `q.pop(0)` returns a(n), the list
  is a(n+1), …, a(n+4), and the next one is a(n+5) = 3·a(n+2) = `3*q[1]`;
  n + 5 ≥ 5 always, so the rule needs no exceptions after the five seeds.

**Notes**

- Exact integer arithmetic, one multiplication per term.
- The closed form `3**(n//3)*(3,4,6)[n%3]//3` (the `//3` also gives
  a(1) = 1) is 48 bytes; three variables with
  `max(z,2*y,3*x)` are 50.
- The whole b-file (6288 terms, about 1000 digits at the end) prints in
  under a second; it is the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000792), CC BY-SA 4.0.
