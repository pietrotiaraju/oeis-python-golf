# A000261

> a(n) = n*a(n-1) + (n-3)*a(n-2), with a(1) = 0, a(2) = 1.
> — [OEIS A000261](https://oeis.org/A000261)

Offset 1: 0, 1, 3, 13, 71, 465, 3539, 30637, 296967, 3184129, 37401155, …

### Python 3 — 46 bytes

```python
n=a=0;s=1
while[print(a)]:a=s-a;s=n*s+4*a;n+=1
```

**How it works**

- With the counter n starting at 0, the pair (a(n+1), a(n+2)) steps as
  a(n+3) = (n+3)·a(n+2) + n·a(n+1). The plain version keeps both terms,
  `a,b=b,n*(a+b)+3*b`, and costs 48 bytes.
- Here the second variable is the sum s = a(n+1) + a(n+2) instead.
  The next sum is (n+4)·s − 4·a, where the n·a terms cancel, and that is
  n·s + 4·(s − a). Since s − a is exactly the next term, the update splits
  into two short statements: `a=s-a` first, then `s=n*s+4*a` with the new a.
  This saves the parentheses and the tuple assignment, two bytes in all.
- The start (a, s) = (0, 1) is (a(1), a(1) + a(2)); at n = 0 the old s is
  multiplied by 0, so only a = 1 − 0 = 1 matters for the next step.
- `while[print(a)]:` is a byte under `while 1:print(a);`: the one-element
  list `[None]` is truthy. Folding the counter into the update with
  `(n:=n+1)` costs two bytes more than `;n+=1`, since n would have to
  start at −1.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (102 terms) prints at once; the program stops after 1557 terms, when
  a(n) passes the 4300-digit int-to-str limit of Python 3.11+. The bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000261), CC BY-SA 4.0.
