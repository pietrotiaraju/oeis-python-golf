# A001670

> k appears k times (k even).
> — [OEIS A001670](https://oeis.org/A001670)

Offset 1: 2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8, 8, 10, 10, …

### Python 3 — 35 bytes

```python
k=2
while[exec('print(k);'*k)]:k+=2
```

**How it works**

- Block printing: for k = 2, 4, 6, … the string `'print(k);'*k` is k print
  statements in a row, and `exec` runs them, so k comes out k times.
- `exec` returns None, so `[None]` keeps the loop going and `k+=2` moves to
  the next even number. The same program as [A001650](../A001650/) with
  `k=2`.

**Notes**

- The b-file has 10000 terms; the bar is the whole b-file, printed in under
  a second. Correct for every n.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001670), CC BY-SA 4.0.
