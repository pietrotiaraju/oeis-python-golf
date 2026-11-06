# A000231

> Number of inequivalent Boolean functions of n variables under action of complementing group.
> — [OEIS A000231](https://oeis.org/A000231)

Offset 0: 2, 3, 7, 46, 4336, 134281216, 288230380379570176, …

### Python 3 — 42 bytes

```python
N=1
while[print((2**N|N-1<<N//2)//N)]:N*=2
```

**How it works**

- N runs over 2^n, the number of inputs. The complementing group is
  (Z₂)ⁿ acting on the inputs by x ↦ x ⊕ c. By Burnside, c = 0 fixes all
  2^N functions, and each of the N − 1 other c splits the inputs into N/2
  pairs {x, x ⊕ c}, so it fixes 2^(N/2) functions:
  a(n) = (2^N + (N − 1)·2^(N/2))/N, the formula on the OEIS page.
- `N-1<<N//2` is (N − 1)·2^(N/2). At N = 1 it is 0, so the floor in `N//2`
  never matters, and the first term is 2^1/1 = 2.
- N − 1 < 2^(N/2) for every N = 2^n, so (N − 1)·2^(N/2) < 2^N and its bits
  sit below bit N: `|` adds the two parts, and since `|` binds looser than
  `<<` and `-`, no inner parentheses are needed.
- Division by N is exact (the result is an orbit count), so `//N` gives the
  term; N doubles at each step.

**Notes**

- The terms grow like 2^(2^n − n): a(13) has 2463 digits and a(14) has
  4928, past CPython's 4300-digit int-to-str limit, so the program prints
  14 terms (n = 0..13) and stops with a `ValueError`. The b-file has 12
  terms, so the bar is the whole b-file.
- A counter n with the formula written out
  (`2**2**n+~-2**n*2**(2**n>>1)>>n`) is 53 bytes; tracking y = 2^N and
  z = 2^(N/2) (`z+(y-z>>n)`, z only matters from n = 1 on) is 48.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000231), CC BY-SA 4.0.
