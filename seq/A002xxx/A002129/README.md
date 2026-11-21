# A002129

> Generalized sum of divisors function: excess of sum of odd divisors of n over sum of even divisors of n.
> — [OEIS A002129](https://oeis.org/A002129)

Offset 1: 1, -1, 4, -5, 6, -4, 8, -13, 13, -6, 12, -20, …

### Python 3 — 65 bytes

```python
r=[1]
for n in r:r+=n+1,;print(sum(-(-1)**d*d*(n%d<1)for d in r))
```

**How it works**

- a(n) = Σ_{d | n} (−1)^(d+1)·d: odd divisors count with +, even ones with −.
- `r` is the list being looped over, and each pass appends n+1 to it, so
  the `for` never ends and r holds 1, …, n+1 (the loop of
  [A000203](../../A000xxx/A000203/)); n+1 never divides n, so summing over
  all of r is summing over 1, …, n.
- `-(-1)**d*d` is +d for odd d and −d for even d (`**` binds tighter than
  the unary minus), and `*(n%d<1)` keeps only divisors.

**Notes**

- Integer arithmetic only, so it is correct for every n; O(n) per term.
- `d*(n%d<1)*(d%2*2-1)` is 1 byte longer and a little faster.
- The b-file has 10000 terms; the bar is the whole b-file in 60 s, about
  21 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002129), CC BY-SA 4.0.
