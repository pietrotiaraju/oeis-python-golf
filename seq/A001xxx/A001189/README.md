# A001189

> Number of degree-n permutations of order exactly 2.
> — [OEIS A001189](https://oeis.org/A001189)

Offset 1: 0, 1, 3, 9, 25, 75, 231, 763, 2619, 9495, 35695, 140151, 568503, 2390479, 10349535, 46206735, …

### Python 3 — 42 bytes

```python
a=b=n=1
while[print(a-1)]:a,b=a+n*b,a;n+=1
```

**How it works**

- A permutation of order exactly 2 is an involution other than the
  identity, so a(n) = I(n) − 1, with the involution numbers
  I(n) = I(n−1) + (n−1)·I(n−2) (point n is fixed, or swapped with one of
  the other n − 1 points).
- `a` and `b` hold I(n) and I(n−1); `a=b=n=1` is I(1) = I(0) = 1.

**Notes**

- One multiplication per term: the whole b-file prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001189), CC BY-SA 4.0.
