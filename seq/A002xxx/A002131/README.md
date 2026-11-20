# A002131

> Sum of divisors d of n such that n/d is odd.
> — [OEIS A002131](https://oeis.org/A002131)

Offset 1: 1, 2, 4, 4, 6, 8, 8, 8, 13, 12, 12, 16, …

### Python 3 — 63 bytes

```python
r=[1]
for n in r:r+=n+1,;print(sum(n//d%2*d>>n%d*d for d in r))
```

**How it works**

- a(n) = Σ d over the divisors d of n with n/d odd.
- `r` is the list being looped over, and each pass appends n+1 to it, so
  the `for` never ends and r holds 1, …, n+1 (the loop of
  [A000203](../../A000xxx/A000203/)); n+1 never divides n.
- `n//d%2*d>>n%d*d`: `n//d%2*d` is d when ⌊n/d⌋ is odd and 0 otherwise,
  and the shift by (n mod d)·d (a shift binds looser than `*`) leaves it
  alone when d divides n and clears it when it does not, since then the
  shift is at least d bits and the value is at most d < 2^d. When d | n,
  ⌊n/d⌋ = n/d, so the sum is exactly the definition.

**Notes**

- Integer arithmetic only, so it is correct for every n; O(n) per term.
- Summing n/d over the odd d in `r[::2]` (`n//d*(n%d<1)for d in r[::2]`)
  is 3 bytes longer.
- The b-file has 10000 terms; the bar is the whole b-file in 60 s, about
  15 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002131), CC BY-SA 4.0.
