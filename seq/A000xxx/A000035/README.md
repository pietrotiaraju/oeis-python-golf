# A000035

> Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n.
> — [OEIS A000035](https://oeis.org/A000035)

Offset 0: 0, 1, 0, 1, 0, …

### Python 3 — 21 bytes

```python
while 1:print('0\n1')
```

**How it works**

- Each pass prints the whole period at once: the string `'0\n1'` holds both
  terms with a newline between them, and `print` adds the newline after the 1.
- It is the [A000034](../A000034/) program with `'1\n2'` replaced by `'0\n1'`.

**Notes**

- `while[print('0\n1')]:0` is one byte longer (22).
- `n=0` + `while[print(n)]:n^=1` (the [A000027](../A000027/) loop with
  `n+=1` replaced by `n^=1`) is 24 bytes; `while 1:print(0);print(1)` is 25.
- `while 1:print(*'01',sep='\n')` is 29 bytes.
- The b-file has 1001 terms (n = 0 to 1000) and the whole of it prints
  instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 21 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000035), CC BY-SA 4.0.
