# A000272

> Number of trees on n labeled nodes: n^(n-2) with a(0)=1.
> — [OEIS A000272](https://oeis.org/A000272)

Offset 0: 1, 1, 1, 3, 16, 125, 1296, 16807, 262144, 4782969, …

### Python 3 — 36 bytes

```python
n=0
while[print(n**max(0,n-2))]:n+=1
```

**How it works**

- Cayley's formula gives n^(n-2) labeled trees on n ≥ 1 nodes, and the
  sequence sets a(0) = 1. The plain `n**(n-2)` breaks on the first two
  terms: `0**-2` raises `ZeroDivisionError` and `1**-1` is the float `1.0`.
- Clamping the exponent with `max(0,n-2)` fixes both at once: n = 0 gives
  `0**0`, which Python defines as 1, and n = 1 gives `1**0` = 1. From
  n = 2 on the exponent is n-2 and nothing changes, so every term is an
  exact `int`.
- `while[print(...)]:` loops forever (a one-element list is truthy) and is a
  byte under `while 1:print(...);`.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The whole
  b-file (389 terms) prints at once; the bar is the whole b-file in 60 s.
- a(1373) is the first term with more than 4300 digits, so Python 3.11+
  stops there with a `ValueError` from the int-to-str limit.
- Other routes tried: an exponent counter `n=e=0` /
  `while[print(n**e)]:n+=1;e+=n>2` ties at 36 bytes; printing a(0) first
  and using `n**n//n//n` from n = 1 (`n=1;print(1)`) is 42; guarding with
  `n>1and n**(n-2)or 1` or `n**(n>1and n-2)` is longer than `max`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000272), CC BY-SA 4.0.
