# A002191

> Possible values for sum of divisors of n.
> — [OEIS A002191](https://oeis.org/A002191)

Offset 1: 1, 3, 4, 6, 7, 8, 12, 13, 14, 15, 18, 20, …

### Python 3 — 75 bytes

```python
r=[1];f=[]
for n in r:r+=n+1,;f+=sum(d*(n%d<1)for d in r),;n in f!=print(n)
```

**How it works**

- σ(n) ≥ n + 1 for n ≥ 2 (σ(1) = 1), so v is a value of σ exactly when
  σ(n) = v for some n ≤ v.
- `for n in r:r+=n+1,` walks n = 1, 2, 3, … with r = [1, …, n + 1] at
  step n (the [A000203](../../A000xxx/A000203/) trick); n + 1 never
  divides n, so `sum(d*(n%d<1)for d in r)` is σ(n).
- `f` collects σ(1), …, σ(n), which covers every possible preimage of n,
  so `n in f` decides n, and the chain `n in f!=print(n)` prints it only
  then.

**Notes**

- Exact integer arithmetic, right for every n.
- Step n costs O(n) (the divisor sum and the list search): 2000 terms
  (v ≤ 7884) come in 5 s here and 4500 in about 25 s. The b-file has
  10000 terms; the bar is 4500 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002191), CC BY-SA 4.0.
