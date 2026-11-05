# A000225

> a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that name is usually reserved for A001348.)
> — [OEIS A000225](https://oeis.org/A000225)

Offset 0: 0, 1, 3, 7, 15, 31, 63, 127, 255, 511, …

### Python 3 — 25 bytes

```python
n=0
while[print(n)]:n-=~n
```

**How it works**

- If n = 2^k − 1, then 2n + 1 = 2^(k+1) − 1, so each term is twice the
  previous one plus 1, starting from a(0) = 0.
- `~n` is −n − 1, so `n-=~n` sets n to n + n + 1 = 2n + 1: one byte under
  `n+=n+1` and two under `n=n*2+1`.
- `print(n)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never stops. It is the
  [A000079](../A000079/) loop with `n=0` and `n-=~n` in place of `n=1` and
  `n*=2`.
- Python integers are unbounded, so every term is exact.

**Notes**

- `n=1` + `while[print(n-1)]:n*=2` (or `n+=n`) keeps 2^n and subtracts the
  1 when printing; it is 26 bytes.
- `n=-1` + `while[print(~n)]:n+=n` runs over −2^n and prints its
  complement; also 26 bytes.
- `n=0` + `while[print(2**n-1)]:n+=1` is 29 bytes.
- The b-file has 1001 terms (n = 0 to 1000) and the whole of it prints
  instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 25 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000225), CC BY-SA 4.0.
