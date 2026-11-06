# A000265

> Remove all factors of 2 from n; or largest odd divisor of n; or odd part of n.
> — [OEIS A000265](https://oeis.org/A000265)

Offset 1: 1, 1, 3, 1, 5, 3, 7, 1, 9, 5, 11, 3, 13, 7, 15, 1, …

### Python 3 — 32 bytes

```python
n=1
while[print(n//(n&-n))]:n+=1
```

**How it works**

- In two's complement, −n is ~n + 1: the trailing zeros of n stay zeros, the
  lowest 1 bit stays 1 and every bit above it flips. So `n&-n` keeps only the
  lowest set bit of n, which is 2^k for n = 2^k · m with m odd.
- `n//(n&-n)` divides that power of 2 out and leaves the odd part m. The
  division is exact, so `//` gives an integer (`/` would print `1.0`).
- The parentheses are needed: `//` binds tighter than `&`, so `n//n&-n`
  would be `(n//n)&-n` = 1 & −n.
- `print(...)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never stops (the [A000225](../A000225/) loop).
- Python integers are unbounded, so every term is exact.

**Notes**

- `n=0` + `while n:=n+1:print(n//(n&-n))` moves the step into the condition
  but is 33 bytes.
- The self-similar form a(2k) = a(k), a(2k+1) = 2k+1 grows the sequence in
  the list it walks: `a=[1]` + `for x in a:print(x);a+=x,len(a)+2` (at step
  k the list has 2k − 1 terms, and it appends a(2k) = x and
  a(2k+1) = len(a) + 2). It is 39 bytes.
- The b-file has 100000 terms (n = 1 to 100000) and the whole of it prints
  in well under a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000265), CC BY-SA 4.0.
