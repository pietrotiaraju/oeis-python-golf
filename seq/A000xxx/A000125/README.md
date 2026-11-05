# A000125

> Cake numbers: maximal number of pieces resulting from n planar cuts through
> a cube (or cake): C(n+1,3) + n + 1.
> — [OEIS A000125](https://oeis.org/A000125)

Offset 0: 1, 2, 4, 8, 15, 26, 42, 64, 93, 130, 176, 232, 299, 378, 470, 576, …

### Python 3 — 37 bytes

```python
n=0
while[print(n*(n*n+5)//6+1)]:n+=1
```

**How it works**

- a(n) = C(n,0) + C(n,1) + C(n,2) + C(n,3) = C(n+1,3) + n + 1
  = (n³ + 5n)/6 + 1, the closed form on the OEIS entry.
- n³ + 5n = (n³ − n) + 6n, and n³ − n = (n − 1)n(n + 1) is a product of
  three consecutive integers, so it is divisible by 6. The `//6` is
  therefore exact for every n: no rounding is involved.
- `n*(n*n+5)` is that numerator in 9 bytes; `(n**3+5*n)` needs the
  parentheses before `//` and is a byte longer.
- `while[print(...)]:` prints in the loop condition: `[None]` is a non-empty
  list, so it is true, and it saves a byte over `while 1:print(...);`.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The difference recurrence from the OEIS Python program,
  `a=b=c=1` and `a+=b;b+=c;c+=1`, is 38 bytes with the same loop.
- A brute-force search over arithmetic expressions in `n` (with the start of
  `n` shifted by up to 9, counting up or down) found nothing shorter than the
  14-byte `n*(n*n+5)//6+1` up to 9 bytes, and no 13-byte `A//d+c`, `A±B` or
  `A*B` built from pieces of up to 8 bytes.
- The b-file has the 1001 terms a(0)..a(1000), all printed in a few
  milliseconds; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000125), CC BY-SA 4.0.
