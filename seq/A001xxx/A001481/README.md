# A001481

> Numbers that are the sum of 2 squares.
> — [OEIS A001481](https://oeis.org/A001481)

Offset 1: 0, 1, 2, 4, 5, 8, 9, 10, 13, 16, 17, 18, 20, 25, 26, 29, 32, 34, 36, 37, 40, …

### Python 3 — 70 bytes

```python
s={n:=0}
while[s&{n-k for k in s}and print(n)]:n+=1;s|={n}&{len(s)**2}
```

**How it works**

- `s` is the set of squares ≤ n. It starts as {0} and holds 0², 1², …,
  (j − 1)² with j = `len(s)`, so the next square is j²; when n reaches it,
  `{n}&{len(s)**2}` is {n} and n joins the set (otherwise the intersection
  is empty).
- n is a sum of two squares x² + y² (with x, y ≥ 0, so 0 = 0² + 0² counts,
  as in the entry) exactly when some square k ≤ n has n − k also a square:
  the set `{n-k for k in s}&s` is then non-empty and `and print(n)` prints
  n. The list around it is always true, so the loop never ends.
- Exact integer arithmetic; each n costs about √n set operations.

**Notes**

- The b-file (10000 terms, up to 39592) prints in about a second; the bar
  is the whole b-file in 60 s.
- Adding every square at once, `s|={n*n}` as in
  [A000925](../../A000xxx/A000925/), is 60 bytes, but then `s` has n + 1
  elements and each n costs time proportional to n: about 6000 terms in a
  minute.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001481), CC BY-SA 4.0.
