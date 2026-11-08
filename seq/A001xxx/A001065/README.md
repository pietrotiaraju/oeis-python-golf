# A001065

> Sum of proper divisors (or aliquot parts) of n: sum of divisors of n that are less than n.
> — [OEIS A001065](https://oeis.org/A001065)

Offset 1: 0, 1, 1, 3, 1, 6, 1, 7, 4, 8, 1, 16, 1, 10, 9, 15, 1, 21, 1, 22, …

### Python 3 — 56 bytes

```python
n=1
while[print(sum(d*(n%d<1)for d in range(1,n)))]:n+=1
```

**How it works**

- a(n) = σ(n) − n is the sum of the divisors d < n: `d*(n%d<1)` is d when
  d divides n and 0 otherwise, summed over d = 1, …, n − 1.
- For n = 1 the range is empty and the sum is 0 = a(1).
- `while[print(…)]:n+=1` is the usual infinite loop: the list holding
  print's `None` is truthy.

**Notes**

- Exact integer arithmetic, straight from the definition.
- Term n costs n − 1 divisions, so the b-file (10 000 terms) prints in
  about 12 s; the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001065), CC BY-SA 4.0.
