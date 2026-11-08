# A001129

> Iccanobif numbers: reverse digits of two previous terms and add.
> — [OEIS A001129](https://oeis.org/A001129)

Offset 0: 0, 1, 1, 2, 3, 5, 8, 13, 39, 124, 514, 836, …

### Python 3 — 65 bytes

```python
a,b=0,1
while[print(a)]:a,b=b,int(str(a)[::-1])+int(str(b)[::-1])
```

**How it works**

- Fibonacci with both summands reversed: a(n) = rev(a(n−1)) + rev(a(n−2)),
  with `int(str(x)[::-1])` as rev (`int` drops the leading zeros), and the
  pair moved along as in [A000045](../../A000xxx/A000045/).

**Notes**

- A lambda `r=lambda x:int(str(x)[::-1])` costs 3 bytes more than writing
  the reversal twice.
- The whole b-file (1001 terms) prints instantly; the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001129), CC BY-SA 4.0.
