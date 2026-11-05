# A000002

> Kolakoski sequence: a(n) is length of n-th run; a(1) = 1; sequence consists
> just of 1's and 2's.
> — [OEIS A000002](https://oeis.org/A000002)

Offset 1: 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, …

### Python 3 — 54 bytes

```python
x=y=-1
while 1:print(2-x%2);f=y&~-~y;x^=f;y=y+1|f&x>>1
```

**How it works**

This is David Eppstein's bit-trick generator, the Python program on the OEIS
entry, squeezed:

- The sequence describes its own runs, so it can be produced by a stack of
  copies of itself, each level reading the level above to know how long its
  runs are. Only O(log n) levels are ever active
  ([The Kolakoski tree](https://11011110.github.io/blog/2016/10/13/kolakoski-tree.html)).
- `x` and `y` keep one bit per level, and one step of the whole stack is a
  binary carry: `f = y & ~(y+1)` picks out the trailing 1-bits of `y` (the
  levels that move on), `x ^= f` flips their symbols, and
  `y = (y+1) | (f & x>>1)` sets up the next step from the level above
  ([derivation](https://11011110.github.io/blog/2016/10/14/kolakoski-sequence-via.html)).
- The output is the lowest bit of `x`: 1 when it is set, 2 when it is clear.

**Golf tricks**

- `~-~y` is `~(y+1)`: `-~y` is `y+1`.
- `y+1|f&x>>1` needs no parentheses: `>>` binds tighter than `&`, and `&`
  tighter than `|`.
- `2-x%2` prints 1 or 2 from the low bit (`x%2` is 0 or 1 even for negative x).

**Notes**

- Memory is O(log n): the program never stores the sequence.
- Checked against the whole b-file (10 502 terms) and, outside the verifier,
  against the plain list construction for the first 10⁶ terms.
- Other shapes tried, all building the list `[1,2,2]` and appending runs of
  `1+i%2`: printing with a lag of two (56 bytes), guarding the first two
  steps with `*(i>1)` (60), the same with `enumerate` (61).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000002), CC BY-SA 4.0.
