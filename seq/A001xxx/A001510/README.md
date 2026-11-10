# A001510

> a(n) = 2*a(n-1)*(a(n-1)-1) for n > 1, with a(0) = 1, a(1) = 2.
> — [OEIS A001510](https://oeis.org/A001510)

Offset 0: 1, 2, 4, 24, 1104, 2435424, 11862575248704, …

### Python 3 — 32 bytes

```python
a=1
while[print(a)]:a*=a*2-2or 2
```

**How it works**

- `a*=a*2-2` multiplies a by 2a − 2: that is the recurrence
  a(n) = 2·a(n−1)·(a(n−1) − 1).
- The recurrence does not hold at n = 1: from a(0) = 1 it would give 0.
  That is exactly the one step where the factor 2a − 2 is 0, so `or 2`
  replaces it by 2 and a(1) = 1·2 = 2. From then on a ≥ 2, the factor is
  at least 2 and the `or` never fires.

**Notes**

- With b(n) = 2a(n) − 1 the recurrence becomes b(n) = b(n−1)² − 2 with
  b(1) = 3, so for n ≥ 1, a(n) = (L(2ⁿ) + 1)/2 with L the Lucas numbers
  (L(2m) = L(m)² − 2). Running b = 2a instead, `b=2` /
  `while[print(b>>1)]:b*=b-2or 2`, is 33 bytes; printing a(0) apart,
  `print(1);a=2` / `while[print(a)]:a*=2*a-2`, is 37.
- Exact integer arithmetic, so the program is right for every n. The
  number of digits doubles at each step: a(14) has 3424 digits and a(15)
  6848, so Python's 4300-digit int-to-str limit stops the program after
  a(14).
- The b-file has 10 terms (a(0) to a(9)); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001510), CC BY-SA 4.0.
