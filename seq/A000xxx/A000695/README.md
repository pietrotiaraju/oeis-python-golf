# A000695

> Moser-de Bruijn sequence: sums of distinct powers of 4.
> — [OEIS A000695](https://oeis.org/A000695)

Offset 0: 0, 1, 4, 5, 16, 17, 20, 21, 64, 65, 68, 69, 80, …

### Python 3 — 38 bytes

```python
n=0
while[print(int(f'{n:b}',4))]:n+=1
```

**How it works**

- The sums of distinct powers of 4, in increasing order, are the numbers
  whose base-4 digits are all 0 or 1, and the n-th of them has the binary
  digits of n as its base-4 digits: a(n) = Σ bᵢ4ⁱ when n = Σ bᵢ2ⁱ. Reading
  the same digit string in a bigger base keeps the order.
- `f'{n:b}'` is n in binary (3 bytes shorter than `bin(n)[2:]`), and
  `int(…,4)` reads it in base 4.
- `while[print(…)]:` is always true, as the list is never empty; it saves a
  byte over `while 1:print(…);n+=1`.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1024 terms; they print in a fraction of a second. The bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000695), CC BY-SA 4.0.
