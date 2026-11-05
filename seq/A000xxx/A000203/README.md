# A000203

> a(n) = sigma(n), the sum of the divisors of n. Also called sigma_1(n).
> — [OEIS A000203](https://oeis.org/A000203)

Offset 1: 1, 3, 4, 7, 6, 12, 8, 15, 13, 18, …

### Python 3 — 56 bytes

```python
r=[1]
for n in r:r+=n+1,;print(sum(d*(n%d<1)for d in r))
```

**How it works**

- `r` is the list being looped over, and each pass appends n+1 to it, so the
  `for` never runs out: it is an infinite loop over n = 1, 2, 3, … that also
  hands you the candidate divisors. After the append, `r` holds 1, …, n+1.
- The extra n+1 never divides n (for n ≥ 1, n mod (n+1) = n), so summing over
  all of `r` is the same as summing over 1, …, n. That makes the loop 2 bytes
  under `n=1` / `while[print(sum(…for d in range(1,n+1)))]:n+=1`.
- `d*(n%d<1)` is d when d divides n and 0 otherwise; `)for` needs no space.

**Notes**

- Integer arithmetic only, so it is correct for every n. It is O(n) per term:
  about 22000 terms in 60 s here, and the bar is 15000.
- Same length, also correct: `d>>n%d*d for` (a non-divisor is shifted right
  by at least its own bit length), and printing before the append. Longer:
  `d for d in r if n%d<1` (+2), `0**(n%d)` (+1), and
  `from math import*` with `sum({gcd(n,k)for k in r})` (+19).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000203), CC BY-SA 4.0.
