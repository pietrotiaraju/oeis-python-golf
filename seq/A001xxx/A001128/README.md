# A001128

> Reverse digits of previous term and multiply by previous term.
> — [OEIS A001128](https://oeis.org/A001128)

Offset 1: 2, 4, 16, 976, 662704, 269896807264, …

### Python 3 — 40 bytes

```python
x=2
while[print(x)]:x*=int(str(x)[::-1])
```

**How it works**

- Each term is the previous one times its digit reversal:
  `x*=int(str(x)[::-1])`, starting from 2.

**Notes**

- The number of digits doubles every step (a(12) has 760). a(15) has about
  6080 digits, past Python's 4300-digit int-to-str limit, so the program
  stops with a ValueError after printing a(1) to a(14). The b-file has 12
  terms and the bar is all 12 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001128), CC BY-SA 4.0.
