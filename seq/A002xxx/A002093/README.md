# A002093

> Highly abundant numbers: numbers k such that sigma(k) > sigma(m) for all m < k.
> — [OEIS A002093](https://oeis.org/A002093)

Offset 1: 1, 2, 3, 4, 6, 8, 10, 12, 16, 18, 20, 24, …

### Python 3 — 76 bytes

```python
*r,m=1,0
for n in r:r+=n+1,;m<(m:=max(m,sum(d*(n%d<1)for d in r)))==print(n)
```

**How it works**

- n is highly abundant when σ(n) is larger than every σ(m) with m < n, so
  the program keeps the running maximum `m` of σ(1), …, σ(n−1) and prints n
  when σ(n) beats it.
- `r` is the list being looped over, and each pass appends n+1 to it, so
  the `for` never ends and r holds 1, …, n+1; `sum(d*(n%d<1)for d in r)`
  is σ(n) (n+1 never divides n), as in [A000203](../../A000xxx/A000203/).
- `m<(m:=max(m,σ))==print(n)` is a chained comparison: the left `m` is
  read before the walrus stores the new maximum, so the comparison is true
  exactly when σ(n) is a new record, and only then does `print(n)` run.
  `*r,m=1,0` sets r = [1] and m = 0.

**Notes**

- Integer arithmetic only, so it is correct for every n. Each σ(n) costs
  n steps, and the terms thin out: the 90th term, 12240, comes after about
  17 s here. The b-file has 10000 terms (up to about 7·10²⁷); the bar is
  90 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002093), CC BY-SA 4.0.
