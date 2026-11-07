# A000960

> Flavius Josephus's sieve: Start with the natural numbers; at the k-th sieving step, remove every (k+1)-st term of the sequence remaining after the (k-1)-st sieving step; iterate.
> — [OEIS A000960](https://oeis.org/A000960)

Offset 1: 1, 3, 7, 13, 19, 27, 39, 49, 63, 79, 91, 109, 133, 147, 181, 207, 223, 253, 289, 307, …

### Python 3 — 57 bytes

```python
n=p=1
while[print(p)]:
 p=k=n=n+1
 while k:p+=~-p//k;k-=1
```

**How it works**

- Step k removes every (k+1)-st term, so the term at position p after the
  step was at position p + ⌊(p−1)/k⌋ before it.
- Steps after step n−1 remove only positions > n, so a(n) is the term at
  position n after step n−1. Starting from p = n and undoing the steps
  k = n−1, …, 1 gives its starting position, which is its value:
  `p+=~-p//k`. This is the same as Paul D. Hanna's and Joshua Zucker's
  formulas in the OEIS entry.
- The loop starts at k = n, where ⌊(n−1)/n⌋ = 0 adds nothing, so
  `p=k=n=n+1` sets everything at once.

**Notes**

- n integer steps for the n-th term: the whole b-file (10000 terms) in
  about 18 s, and the bar is the whole b-file in 60 s.
- `exec('p+=~-p//k;k-=1;'*n)` on one line is 1 byte shorter, but it
  compiles a new string of 15n characters for every term and prints only
  3300 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000960), CC BY-SA 4.0.
