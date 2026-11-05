# A000178

> Superfactorials: product of first n factorials.
> — [OEIS A000178](https://oeis.org/A000178)

Offset 0: 1, 1, 2, 12, 288, 34560, 24883200, 125411328000, …

### Python 3 — 38 bytes

```python
a=f=n=1
while[print(a)]:f*=n;a*=f;n+=1
```

**How it works**

- a(n) = 0!·1!·…·n! = a(n−1)·n!, so `f` keeps n! (`f*=n`) and `a` keeps
  the running product of the factorials (`a*=f`).
- `while[print(a)]:` prints first and then steps: `print` returns `None`,
  and the one-element list `[None]` is truthy, one byte under
  `while 1:print(a);`.
- Starting from `a=f=n=1`, the first pass prints a(0) = 1 and multiplies by
  1! = 1, so a(1) = 1 comes out right without a special case.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (47 terms) prints at once; the program stops after a(81), when the next
  term passes the 4300-digit int-to-str limit of Python 3.11+. The bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000178), CC BY-SA 4.0.
