# A000408

> Numbers that are the sum of three nonzero squares.
> — [OEIS A000408](https://oeis.org/A000408)

Offset 1: 3, 6, 9, 11, 12, 14, 17, 18, 19, 21, …

### Python 3 — 88 bytes

```python
n=k=1;s={1}
while n:=n+1:s|={k*k};k+=k*k<=n;{n-a-b for a in s for b in s}&s and print(n)
```

**How it works**

- `s` collects positive squares. Each pass adds k² and moves k on once
  k² ≤ n; since n grows by 1, at the test `s` holds every positive square
  up to n, plus at most the next one. Squares larger than n never matter,
  because each of three positive squares adding up to n is less than n.
- `{n-a-b for a in s for b in s}&s` is non-empty exactly when
  n = a + b + c with a, b, c in `s`, that is, when n is a sum of three
  nonzero squares; `and print(n)` prints n only then.
- `while n:=n+1:` steps n in the header; n is never 0 there, so the
  condition is always true.

**Notes**

- `any(n-a-b in s for a in s for b in s)` is 5 bytes longer. The
  [A000404](../A000404/) layout, with 0 in `s` and the next square
  `len(s)**2`, would also count sums with zero parts.
- Halter-Koch (1982, cited in the entry) characterizes the exceptions as
  4ʲ(8m + 7) and 4ʲ·s for s in {1, 2, 5, 10, 13, 25, 37, 58, 85, 130} and
  possibly one more unknown s > 5·10¹⁰. A program built on that list,
  `while m%4<1:m//=4` and
  `m%8>6or m in{1,2,5,10,13,25,37,58,85,130}or print(n)`, is 94 bytes and
  would rest on that extra exception not existing.
- Exact integer arithmetic and a complete search, so the program is right
  for every n.
- A test builds about n sums, so the cost per term grows linearly: the
  whole b-file prints in about 16 s here and about 16 800 terms in 60 s.
  The b-file has 10000 terms (up to a(10000) = 12061); the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 117 | first entry |
| 2026-11-07 | Python 3 | 88 | one set of squares, pair sums by intersection |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000408), CC BY-SA 4.0.
