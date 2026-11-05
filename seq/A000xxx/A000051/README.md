# A000051

> a(n) = 2^n + 1.
> — [OEIS A000051](https://oeis.org/A000051)

Offset 0: 2, 3, 5, 9, 17, 33, 65, 129, 257, …

### Python 3 — 26 bytes

```python
n=2
while[print(n)]:n+=n-1
```

**How it works**

- If n = 2^k + 1, then 2n − 1 = 2^(k+1) + 1, so each term is twice the
  previous one minus 1, starting from a(0) = 2. `n+=n-1` takes that step.
- `print(n)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never stops. It is the
  [A000027](../A000027/) loop with `n=1` and `n+=1` replaced by `n=2` and
  `n+=n-1`.
- Python integers are unbounded, so every term is exact.

**Notes**

- `n-=1-n` and `n+=~-n` are the same length as `n+=n-1`.
- `n=1` + `while[print(n+1)]:n+=n` (or `n*=2`) keeps 2^n and adds the 1
  when printing; it is also 26 bytes.
- `n=1` + `while[print(n|1)]:n*=2` is 26 bytes too, but prints 1 instead
  of 2 for n = 0, since 2^0 = 1 already has its low bit set.
- `n=0` + `while[print(2**n+1)]:n+=1` is 30 bytes.
- The b-file has 101 terms (n = 0 to 100) and the whole of it prints
  instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 26 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000051), CC BY-SA 4.0.
