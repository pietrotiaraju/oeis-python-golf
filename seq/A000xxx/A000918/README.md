# A000918

> a(n) = 2^n - 2.
> — [OEIS A000918](https://oeis.org/A000918)

Offset 0: -1, 0, 2, 6, 14, 30, 62, 126, 254, 510, 1022, 2046, …

### Python 3 — 26 bytes

```python
x=1
while[print(x-2)]:x*=2
```

**How it works**

- x runs over the powers of two 2ⁿ (`x*=2`) and the program prints x − 2,
  starting with 2⁰ − 2 = −1 at the offset 0.

**Notes**

- Other versions: running a(n+1) = 2a(n) + 2 directly, `x=-1` /
  `while[print(x)]:x+=x+2`, is 27 bytes (the start −1 costs one byte more
  than the print shift saves); `2**n-2` in a counting loop is 29.
- Exact integer arithmetic.
- The b-file has 1001 terms; they print at once. The bar is the whole
  b-file in 60 s. a(14285) is the first term with more than 4300 digits,
  so printing stops there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 26 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000918), CC BY-SA 4.0.
