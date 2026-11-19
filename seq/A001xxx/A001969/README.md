# A001969

> Evil numbers: nonnegative integers with an even number of 1's in their binary expansion.
> — [OEIS A001969](https://oeis.org/A001969)

Offset 1: 0, 3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27, 29, 30, 33, 34, 36, …

### Python 3 — 40 bytes

```python
n=0
while[print(n|n.bit_count()&1)]:n+=2
```

**How it works**

- Each pair {2k, 2k+1} holds exactly one evil number: the two differ only in
  the last bit, so one has an even number of 1's and the other an odd
  number. That gives the closed form a(k+1) = 2k + t(k), where t(k) is the
  parity of the 1's of k (the Thue–Morse sequence
  [A010060](https://oeis.org/A010060)).
- `n` runs over the even numbers 0, 2, 4, …, so `n` is 2k and has the same
  number of 1's as k; `n.bit_count()` (Python 3.10+) counts them.
- `c&1` is 1 when the count `c` is odd. Then `n|1` sets the last bit and
  prints 2k+1, whose count is even; otherwise `n|0` prints `n` itself.
  `&` binds tighter than `|`, so no parentheses are needed.
- `print` runs in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never stops.

**Notes**

- This is the program of the odious numbers [A000069](../../A000xxx/A000069/)
  without its `~`, one byte shorter.
- The plain filter `n=0` + `while[n.bit_count()%2or print(n)]:n+=1` is 42
  bytes, and so is stepping `n` by 1 and printing `n*2|n.bit_count()&1`.
- The b-file has 10000 terms (up to 19998) and the whole of it prints
  instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001969), CC BY-SA 4.0.
