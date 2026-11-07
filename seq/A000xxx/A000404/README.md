# A000404

> Numbers that are the sum of 2 nonzero squares.
> — [OEIS A000404](https://oeis.org/A000404)

Offset 1: 2, 5, 8, 10, 13, 17, 18, 20, 25, 26, …

### Python 3 — 73 bytes

```python
n=0;s={0}
while n:=n+1:{n-x for x in s}&s and print(n);s|={n}&{len(s)**2}
```

**How it works**

- When n is tested, `s` holds 0 and the squares below n:
  {0, 1, 4, …, (j − 1)²} with (j − 1)² < n ≤ j².
- `{n-x for x in s}&s` is non-empty exactly when n = x + y with x, y in
  `s`. Neither can be 0, since the other would then be n, which is not in
  `s` yet; and every representation n = a² + b² with a, b ≥ 1 has a², b² < n,
  so both squares are in `s`. The test is therefore "n is a sum of two
  nonzero squares", and `and print(n)` prints n only then.
- `s` has j elements, so the next square is `len(s)**2` = j². If n equals
  it, `{n}&{len(s)**2}` is {n} and n joins `s` after its own test;
  otherwise the intersection is empty.
- `while n:=n+1:` steps n in the header; n is never 0 there, so the
  condition is always true.

**Notes**

- Keeping the next root in a counter instead,
  `n=k=1;s={1}` / `while n:=n+1:s|={k*k};k+=k*k<=n;{n-x for x in s}&s and print(n)`,
  is 75 bytes; `any(n-x in s for x in s)` in place of the intersection
  is 78.
- Exact integer arithmetic and a complete search over the squares below
  n, so the program is right for every n.
- A test costs about √n set operations: here the whole b-file prints in
  about 2 s and about 99 000 terms in 60 s. The b-file has 10000 terms
  (up to a(10000) = 40045); the bar is the whole b-file in 60 s.
- Compare [A000415](../A000415/), which also leaves out the squares, and
  [A000408](../A000408/) for three squares.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 91 | first entry |
| 2026-11-07 | Python 3 | 73 | set intersection, next square from `len(s)` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000404), CC BY-SA 4.0.
