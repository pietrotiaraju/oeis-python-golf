# A000165

> Double factorial of even numbers: (2n)!! = 2^n*n!.
> — [OEIS A000165](https://oeis.org/A000165)

Offset 0: 1, 2, 8, 48, 384, 3840, 46080, 645120, 10321920, 185794560, …

### Python 3 — 33 bytes

```python
a=1;n=2
while[print(a)]:a*=n;n+=2
```

**How it works**

- a(n) = 2·4·6·…·(2n), so each step multiplies by the next even number:
  `n` runs over 2, 4, 6, … and `a*=n` turns (2n−2)!! into (2n)!!.
- `while[print(a)]:` is a byte under `while 1:print(a);`: the one-element
  list `[None]` is truthy.
- Counting by ones instead (`a=n=1`, `a*=2*n;n+=1`) is the same length:
  the shorter start pays for the longer step. Printing `a//2` from
  `a=n=2` costs one byte more.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (404 terms) prints at once; the program stops after a(1423), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000165), CC BY-SA 4.0.
