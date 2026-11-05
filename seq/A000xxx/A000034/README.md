# A000034

> Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2).
> — [OEIS A000034](https://oeis.org/A000034)

Offset 0: 1, 2, 1, 2, 1, …

### Python 3 — 21 bytes

```python
while 1:print('1\n2')
```

**How it works**

- Each pass prints the whole period at once: the string `'1\n2'` holds both
  terms with a newline between them, and `print` adds the newline after the 2.
- It is the [A000012](../A000012/) loop with `1` replaced by that string.

**Notes**

- `while[print('1\n2')]:0` is one byte longer (22), as in A000012.
- `while 1:print(1);print(2)` and `n=1` + `while 1:print(n);n^=3` are both
  25 bytes.
- `while 1:print(*'12',sep='\n')` is 29 bytes.
- The b-file has 10 000 terms (n = 0 to 9999) and the whole of it prints
  instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 21 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000034), CC BY-SA 4.0.
