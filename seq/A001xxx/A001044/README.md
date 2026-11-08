# A001044

> a(n) = (n!)^2.
> — [OEIS A001044](https://oeis.org/A001044)

Offset 0: 1, 1, 4, 36, 576, 14400, 518400, 25401600, 1625702400, 131681894400, …

### Python 3 — 33 bytes

```python
a=n=1
while[print(a*a)]:a*=n;n+=1
```

**How it works**

- `a` holds n!, built as in [A000142](../../A000xxx/A000142/): it starts at
  0! = 1 and after each print is multiplied by the counter n, which then
  steps; the program prints its square `a*a`.
- `a=n=1` covers both 0! and 1!: the first step multiplies by n = 1, so the
  first two prints are both 1.

**Notes**

- Keeping the square itself, `while[print(a)]:a*=n*n;n+=1`, is a tie (33
  bytes); `from math import*` with `factorial(n)**2` is far longer.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s.
- a(860) is the first term with more than 4300 digits (4305) and Python's
  int-to-str limit stops the printing there; a(859) has 4299.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001044), CC BY-SA 4.0.
