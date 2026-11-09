# A001315

> a(n) = Sum_{k=0..n} 2^binomial(n,k).
> — [OEIS A001315](https://oeis.org/A001315)

Offset 0: 2, 4, 8, 20, 100, 2116, 1114244, 68723671300, …

### Python 3 — 55 bytes

```python
y,*P=2,
while 1:print(sum(P:=[y*(y:=x)for x in P+[1]]))
```

**How it works**

- `P` is row n of Pascal's triangle with every entry C(n,k) replaced by
  2^C(n,k). Pascal's rule C(n+1,k) = C(n,k−1) + C(n,k) becomes a product,
  2^C(n+1,k) = 2^C(n,k−1) · 2^C(n,k), where the entries outside the row
  count as 2⁰ = 1. So each entry of the next row is the product of an
  entry with the one before it, over `P+[1]` (the 1 is the entry after
  the end).
- In `y*(y:=x)` the old `y` (the previous entry) is read before the
  walrus stores the current one, so each element is P[k−1] · P[k]. The
  walrus binds `y` at module level, so it survives between rows, and since
  the last `x` is the padding 1, every row leaves `y = 1`, the entry
  before the start of the next row.
- `y,*P=2,` starts with `y = 2` and `P = []`: the first pass gives
  [2 · 1] = [2], row 0 (2^C(0,0) = 2), and leaves `y = 1`. Then come
  [2, 2], [2, 4, 2], [2, 8, 8, 2], … Each new row is stored in `P` and
  its sum printed; all of it is exact integer arithmetic.

**Notes**

- Pairing the row with itself shifted, `P=[2]` /
  `while[print(sum(P))]:P=[*map(int.__mul__,P+[1],[1]+P)]`, is 60 bytes;
  the walrus product with `y,*P=1,2`, printing before each update, is 56.
  Summing `2**x` over a row of binomials is 71 bytes, and
  `from math import*` with `2**comb(n,k)` 77.
- The middle term is 2^C(n, ⌊n/2⌋): the program prints a(0) to a(16)
  (3875 digits) and then stops with a `ValueError` at the interpreter's
  4300-digit int-to-str limit (a(17) has 7318 digits).
- The b-file has 14 terms (n = 0 to 13); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001315), CC BY-SA 4.0.
