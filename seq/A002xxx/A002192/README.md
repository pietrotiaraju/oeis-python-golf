# A002192

> Least integer with A000203(a(n)) = A002191(n), where A002191 = range of the sum-of-divisors function A000203.
> — [OEIS A002192](https://oeis.org/A002192)

Offset 1: 1, 2, 3, 5, 4, 7, 6, 9, 13, 8, 10, 19, …

### Python 3 — 84 bytes

```python
r=[1];D={}
for n in r:r+=n+1,;D={sum(d*(n%d<1)for d in r):n,**D};n in D!=print(D[n])
```

**How it works**

- σ(n) ≥ n + 1 for n ≥ 2 (σ(1) = 1), so every k with σ(k) = v is at most
  v: the values v and their least preimages are settled in increasing
  order of v.
- `for n in r:r+=n+1,` walks n = 1, 2, 3, … with r = [1, …, n + 1] at
  step n (the [A000203](../../A000xxx/A000203/) trick); n + 1 never
  divides n, so `sum(d*(n%d<1)for d in r)` is σ(n).
- `D` maps each value seen so far to its least preimage:
  `D={σ(n):n,**D}` adds σ(n) ↦ n, but in a dict display later keys win,
  so a value already in `D` keeps its smaller preimage.
- After step n, D holds σ(k) for every k ≤ n, so if n is a value its
  least preimage is `D[n]`; `n in D!=print(D[n])` prints it only then.

**Notes**

- Exact integer arithmetic, right for every n.
- Step n costs O(n) (the divisor sum and copying `D`): 4000 terms come
  in about 25 s here. The b-file has 10000 terms; the bar is 4000 terms
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002192), CC BY-SA 4.0.
