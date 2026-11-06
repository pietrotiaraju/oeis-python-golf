# A000317

> a(n+1) = a(n)^2 - a(n)*a(n-1) + a(n-1)^2.
> — [OEIS A000317](https://oeis.org/A000317)

Offset 1: 1, 2, 3, 7, 37, 1159, 1301767, 1693089917617, …

### Python 3 — 41 bytes

```python
a,b=1,2
while[print(a)]:a,b=b,a*a-a*b+b*b
```

**How it works**

- A window of two terms: a = a(n−1) is printed, b = a(n) is the next one, and
  `a,b=b,a*a-a*b+b*b` moves the window one step with the recurrence.
- The seeds are a(1) = 1 and a(2) = 2, as in the OEIS data and the Magma
  program on the entry.
- `while[print(…)]:` is a non-empty list, so it is always true.

**Notes**

- Integers only, so every term is exact.
- a² − ab + b² takes 11 bytes in every form tried: `a*a-a*b+b*b`,
  `a*(a-b)+b*b`, `a*a+b*(b-a)`; `(a-b)**2+a*b` is 12.
- Updating in place instead of the tuple, with the old value read before the
  walrus overwrites it, is a byte longer: `b=b*b+a*(a-(a:=b))` and
  `b=a*a-a*b+b*(a:=b)` are 18 bytes against 17 for `a,b=b,a*a-a*b+b*b`.
- Starting one step early cannot save the seeds: a(0) would have to satisfy
  x² − x + 1 = 2, which has no integer root.
- a(n) roughly doubles its digits each step, so a(17) (about 6260 digits) runs
  into Python's 4300-digit limit for converting an int to a string: the
  program prints a(1)…a(16) and stops with a `ValueError`. That is an
  interpreter limit, not a wrong term. The b-file has 14 terms (n = 1 to 14);
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000317), CC BY-SA 4.0.
