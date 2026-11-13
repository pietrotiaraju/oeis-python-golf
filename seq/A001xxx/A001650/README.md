# A001650

> k appears k times (k odd).
> — [OEIS A001650](https://oeis.org/A001650)

Offset 1: 1, 3, 3, 3, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9, 9, …

### Python 3 — 35 bytes

```python
k=1
while[exec('print(k);'*k)]:k+=2
```

**How it works**

- Block printing: for k = 1, 3, 5, … the string `'print(k);'*k` is k print
  statements in a row, and `exec` runs them, so k comes out k times.
- `exec` returns None, so `[None]` keeps the loop going and `k+=2` moves to
  the next odd number.

**Notes**

- A counter that tracks where the block of k ends (the n-th term is
  2⌈√n⌉ − 1) is 42 bytes; `print(*[k]*k,sep='\n')` is 3 bytes longer than
  the exec string.
- The b-file has 10000 terms; the bar is the whole b-file, printed in under
  a second. Correct for every n.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001650), CC BY-SA 4.0.
