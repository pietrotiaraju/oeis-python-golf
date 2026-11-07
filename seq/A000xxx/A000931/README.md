# A000931

> Padovan sequence (or Padovan numbers): a(n) = a(n-2) + a(n-3) with a(0) = 1, a(1) = a(2) = 0.
> — [OEIS A000931](https://oeis.org/A000931)

Offset 0: 1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 3, 4, …

### Python 3 — 39 bytes

```python
a=1;b=c=0
while[print(a)]:a,b,c=b,c,a+b
```

**How it works**

- (a, b, c) holds three consecutive terms (a(t), a(t+1), a(t+2)); the
  tuple shift `a,b,c=b,c,a+b` appends a(t+3) = a(t+1) + a(t). The start
  is the data's a(0), a(1), a(2) = 1, 0, 0.

**Notes**

- The cheap start `a=b=c=1` is possible in other coordinates, but it does
  not pay here: three in-place statements need 40 bytes
  (`a=b=c=1` / `while[print(a)]:a=b-a;c+=a;b=c-b`), the tuple
  `a,b,c=b-c,-c,-a` ties at 39, and walrus-in-print forms are 41 (all
  found by a search over chains with coefficients −1, 0, 1).
- Exact integer arithmetic.
- The b-file has 8181 terms; they print in about 0.3 s here. The bar is
  the whole b-file in 60 s. a(35217) is the first term with more than 4300
  digits, so printing stops there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000931), CC BY-SA 4.0.
