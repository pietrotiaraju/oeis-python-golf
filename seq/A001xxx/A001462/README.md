# A001462

> Golomb's sequence: a(n) is the number of times n occurs in the sequence, starting with a(1) = 1.
> — [OEIS A001462](https://oeis.org/A001462)

Offset 1: 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, …

### Python 3 — 46 bytes

```python
a=[0,1]
while[print(a[-1])]:a+=1+a[-a[a[-1]]],
```

**How it works**

- **Mallows' recurrence.** a(1) = 1 and a(n) = 1 + a(n − a(a(n − 1))) for
  n ≥ 2. Why it holds: the sequence is nondecreasing and value k fills a
  block of a(k) consecutive places, ending at S(k) = a(1) + … + a(k); so
  a(n) − a(n − 1) is 0 or 1 and a(k) ≤ a(k − 1) + 1. Let v = a(n − 1) and
  L = a(v), the length of block v. If n is still in block v, then
  S(v − 1) + 1 < n ≤ S(v), so n − L lies in (S(v − 1) + 1 − a(v), S(v − 1)],
  inside block v − 1 because a(v) ≤ a(v − 1) + 1: a(n − L) = v − 1 = a(n) − 1.
  If n = S(v) + 1 starts block v + 1, then n − L = S(v − 1) + 1 is the first
  place of block v: a(n − L) = v = a(n) − 1.
- **The list.** `a` holds a dummy a(0) = 0 and then a(1), …, a(n − 1), so
  `a[a[-1]]` is a(a(n − 1)) and, with k = a(a(n − 1)) between 1 and n − 1,
  `a[-k]` is a(n − k) (the negative index counts from the end; the dummy is
  never reached). Each pass prints the last term and appends the next one;
  `while[print(…)]:` is always true, since a one-element list is.

**Notes**

- Exact integer arithmetic and one list entry per term; the b-file
  (10000 terms) prints in well under a second. The bar is the whole b-file
  in 60 s.
- Building the runs directly, `a=[1,2,2]` with
  `for i,x in enumerate(a):print(x);a+=[i+3]*a[i+2]`, is 58 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001462), CC BY-SA 4.0.
