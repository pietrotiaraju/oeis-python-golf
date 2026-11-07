# A000801

> a(n) = Sum_{k = 1..n} floor(2^k / k).
> — [OEIS A000801](https://oeis.org/A000801)

Offset 1: 2, 4, 6, 10, 16, 26, 44, 76, 132, 234, 420, 761, 1391, 2561, 4745, 8841, …

### Python 3 — 38 bytes

```python
s=k=0
while 1:k+=1;s+=2**k//k;print(s)
```

**How it works**

- The definition, term by term: `k` counts 1, 2, 3, …, `s` adds ⌊2ᵏ/k⌋
  with exact integer floor division `//`, and each partial sum is printed.

**Notes**

- `print(s:=s+2**k//k)` and the `while[print(s)]:` header (which needs the
  start `s=2;k=1`) are both 39 bytes.
- Python's 4300-digit limit on int-to-str conversion stops the program at
  a(14298), the first term with 4301 digits, after printing a(1) to
  a(14297) in about 3 s. The limit is not counted as a failure.
- The b-file has 500 terms (up to a(500)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000801), CC BY-SA 4.0.
