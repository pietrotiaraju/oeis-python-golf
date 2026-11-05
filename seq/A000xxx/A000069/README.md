# A000069

> Odious numbers: numbers with an odd number of 1's in their binary expansion.
> — [OEIS A000069](https://oeis.org/A000069)

Offset 1: 1, 2, 4, 7, 8, 11, 13, 14, 16, …

### Python 3 — 41 bytes

```python
n=0
while[print(n|~n.bit_count()&1)]:n+=2
```

**How it works**

- Each pair {2k, 2k+1} holds exactly one odious number: the two differ only in
  the last bit, so one has an odd number of 1's and the other an even number.
  That gives the closed form a(k+1) = 2k + 1 − t(k) from the OEIS page, where
  t(k) is the parity of the 1's of k (the Thue–Morse sequence
  [A010060](https://oeis.org/A010060)).
- `n` runs over the even numbers 0, 2, 4, …, so `n` is 2k and has the same
  number of 1's as k. `n.bit_count()` (Python 3.10+) counts them.
- `~c&1` is 1 when the count `c` is even and 0 when it is odd. If `n` already
  has an odd count, `n|0` prints `n`; otherwise `n|1` sets the last bit and
  prints 2k+1, which then has an odd count.
- `print` runs in the loop condition as in [A000027](../A000027/): it returns
  `None` and `[None]` is a non-empty list, so the loop never stops.

**Notes**

- Stepping `n` by 1 and printing `n*2|~n.bit_count()&1` (or
  `n-~n-n.bit_count()%2`) is 43 bytes, and so is the plain filter
  `n=0` + `while[n.bit_count()%2and print(n)]:n+=1`.
- `bin(n).count('1')` is 4 bytes longer than `n.bit_count()`.
- The b-file has 10 001 terms (n = 1 to 10 001, up to 20 000) and the whole
  of it prints instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000069), CC BY-SA 4.0.
