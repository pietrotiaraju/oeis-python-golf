# A001149

> A self-generating sequence: a(1)=1, a(2)=2, a(n+1) chosen so that a(n+1)-a(n-1) is the first number not obtainable as a(j)-a(i) for 1<=i<j<=n.
> — [OEIS A001149](https://oeis.org/A001149)

Offset 1: 1, 2, 3, 5, 8, 13, 17, 26, 34, 45, 54, 67, 81, 97, 115, 132, …

### Python 3 — 73 bytes

```python
a=[1,m:=2]
for x in a:
 while{m+z for z in a}&{*a}:m+=1
 print(x);a+=x+m,
```

**How it works**

- "First number not obtainable" is the smallest positive integer that is not
  a difference a(j) − a(i) of two terms so far: with that reading the rule
  gives every term of the b-file (a(3) = 1 + 2, a(4) = 2 + 3, a(5) = 3 + 5,
  a(6) = 5 + 8, a(7) = 8 + 9, …).
- `for x in a` walks the list while it grows. When it reaches x = a(k), the
  list holds a(1)…a(k+1), so x is the a(n−1) of the rule with n = k + 1,
  and the new term a(k+2) = x + m is appended, where m is the smallest
  missing difference of a(1)…a(k+1).
- m is a difference of the terms exactly when some z + m is a term too:
  `{m+z for z in a}&{*a}` is non-empty. The set of differences only grows,
  so the smallest missing one never goes down, and `m` keeps its value
  from one term to the next instead of starting again at 1. It does not
  even need a step back after a term: the new difference x + m − x = m is
  now taken, so the next search starts at a number known to be in the set.
- `a=[1,m:=2]` sets both the list and the first candidate (1 = 2 − 1 is
  already a difference) in one statement.

**Notes**

- No stored set of differences: testing a candidate m costs one pass over
  the terms, and m only climbs to about 10⁴ over the 2000 terms, so the
  whole b-file (Manfred Scheucher's 2000 terms) prints in about 2.4 s here.
  Keeping the set of differences and updating it with
  `s|={x+m-z for z in a}` is faster (0.9 s) but 13 bytes longer.
- Exact integers throughout; the program follows the definition, nothing
  else.
- Related: [A005282](https://oeis.org/A005282) (Mian–Chowla, all
  differences distinct), [A054540](https://oeis.org/A054540).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001149), CC BY-SA 4.0.
