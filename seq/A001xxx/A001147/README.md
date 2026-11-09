# A001147

> Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1).
> — [OEIS A001147](https://oeis.org/A001147)

Offset 0: 1, 1, 3, 15, 105, 945, 10395, 135135, 2027025, 34459425, …

### Python 3 — 31 bytes

```python
x=n=1
while[print(x)]:x*=n;n+=2
```

**How it works**

- a(n) = 1·3·5·…·(2n−1), so each step multiplies by the next odd number:
  `n` runs over 1, 3, 5, … and `x*=n` turns (2n−3)!! into (2n−1)!!.
- The first factor is 1, so a(1) = a(0) = 1 and the seed is free:
  `x=n=1` starts both the product and the odd counter. (The even double
  factorials, [A000165](../../A000xxx/A000165/), need `a=1;n=2`.)
- `while[print(x)]:` prints in the loop test (`[None]` is a true list).
- Starting at `n=-1` and stepping first (`n+=2;x*=n`) is 3 bytes
  longer, all of it in the seed `x=1;n=-1`.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (401 terms, a(0)…a(400)) prints at once; the program stops after a(1423), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+ (an
  interpreter limit, not a wrong term). The bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001147), CC BY-SA 4.0.
