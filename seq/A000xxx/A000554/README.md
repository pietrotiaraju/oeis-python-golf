# A000554

> Number of labeled trees of diameter 3 with n nodes.
> — [OEIS A000554](https://oeis.org/A000554)

Offset 4: 12, 60, 210, 630, 1736, 4536, 11430, 28050, 67452, 159588, …

### Python 3 — 38 bytes

```python
n=4
while[print(~-2**n//8*n*~-n)]:n+=1
```

**How it works**

- **The count.** A tree of diameter 3 has a central edge uv, and every other
  node is a leaf joined to u or to v, with at least one on each side (with
  all of them on one side the diameter is 2). There are C(n, 2) choices of
  the edge and 2^(n−2) − 2 ways to split the other n − 2 nodes, so
  a(n) = C(n, 2)·(2^(n−2) − 2) = n(n − 1)(2^(n−3) − 1).
- `~-2**n` is 2^n − 1, since `**` binds tighter than the unary `-` and `~`.
  For n ≥ 3, (2^n − 1)/8 = 2^(n−3) − 1/8, so `~-2**n//8` is exactly
  2^(n−3) − 1, with no parentheses. `~-n` is n − 1.
- `print` sits in the loop condition: `[None]` is a non-empty list, so the
  loop never ends.

**Notes**

- Other versions: `n*~-n*~-2**(n-3)` is a byte longer, and
  `n*~-n*(2**n//8-1)` or `n*~-n*(2**n-8)>>3` two bytes; the first entry,
  `while 1:print(n*(n-1)*(2**(n-3)-1));n+=1`, was 44.
- Exact integer arithmetic, so the program is right for every n.
- a(14260) is the first term with more than 4300 digits, so printing stops
  there with Python's int-to-str limit, after about 5 s here. The b-file has
  997 terms (up to a(1000)); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 44 | first entry |
| 2026-11-07 | Python 3 | 38 | `~-2**n//8` for 2^(n−3) − 1 and the print in the loop condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000554), CC BY-SA 4.0.
