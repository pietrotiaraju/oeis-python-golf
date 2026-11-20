# A002064

> Cullen numbers: a(n) = n*2^n + 1.
> — [OEIS A002064](https://oeis.org/A002064)

Offset 0: 1, 3, 9, 25, 65, 161, 385, 897, 2049, 4609, 10241, 22529, 49153, …

### Python 3 — 29 bytes

```python
n=0
while[print(n<<n|1)]:n+=1
```

**How it works**

- `n<<n` is n·2ⁿ. It is even for n ≥ 1 and 0 for n = 0, so `|1` adds 1:
  `n<<n|1` = n·2ⁿ + 1, one byte per operator.

**Notes**

- `n*2**n+1` is three bytes longer.
- Exact integer arithmetic, right for every n; the 4300-digit int-to-str
  limit stops the output near n = 14000. The b-file has 301 terms (n = 0
  to 300); the bar is the whole b-file in 60 s, a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002064), CC BY-SA 4.0.
