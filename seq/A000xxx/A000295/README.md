# A000295

> Eulerian numbers (Euler's triangle: column k=2 of A008292, column k=1 of A173018).
> — [OEIS A000295](https://oeis.org/A000295)

Offset 0: 0, 0, 1, 4, 11, 26, 57, 120, 247, 502, 1013, 2036, 4083, 8178, …

### Python 3 — 30 bytes

```python
n=0
while[print(2**n+~n)]:n+=1
```

**How it works**

- a(n) = 2ⁿ − n − 1, and `~n` is −n − 1, so `2**n+~n` is the whole
  formula.
- `while[print(…)]:` prints at the top of every pass; `[None]` is a
  non-empty list, so the loop never stops on its own.

**Notes**

- The recurrence a(n) = 2·a(n − 1) + n − 1 (`a=n=0` /
  `while[print(a)]:a+=a+n;n+=1`) is 33 bytes.
- 2ⁿ passes 4300 digits at n = 14 284, so the program prints 14 285 terms
  and then stops with CPython's int-to-str `ValueError`. The b-file has 501
  terms and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000295), CC BY-SA 4.0.
