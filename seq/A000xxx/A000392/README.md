# A000392

> Stirling numbers of second kind S(n,3).
> — [OEIS A000392](https://oeis.org/A000392)

Offset 0: 0, 0, 0, 1, 6, 25, 90, 301, 966, 3025, 9330, 28501, 86526, …

### Python 3 — 40 bytes

```python
n=0
while[print(3**n//6-~-2**n//2)]:n+=1
```

**How it works**

- By inclusion–exclusion over the empty boxes, the number of ways to put
  n labeled balls into 3 unlabeled non-empty boxes is
  S(n, 3) = (3ⁿ − 3·2ⁿ + 3 − 0ⁿ)/6, which for n ≥ 1 is
  (3ⁿ⁻¹ + 1)/2 − 2ⁿ⁻¹.
- For n ≥ 1, 3ⁿ is 3 mod 6, so `3**n//6` is (3ⁿ⁻¹ − 1)/2, and `~-2**n//2`
  is ⌊(2ⁿ − 1)/2⌋ = 2ⁿ⁻¹ − 1 (`**` binds tighter than the unary `~-`, so
  `~-2**n` is 2ⁿ − 1). The difference is (3ⁿ⁻¹ + 1)/2 − 2ⁿ⁻¹ = S(n, 3).
- At n = 0 both floors are 0, which is S(0, 3) = 0, so the 0ⁿ term
  needs no code.

**Notes**

- Exact integer arithmetic, correct for every n; only the 4300-digit
  int-to-str limit of Python 3.11+ stops it, after about 9000 terms. The
  whole b-file (201 terms, n = 0 to 200) prints at once; the bar is the
  whole b-file in 60 s.
- The plain `(3**n-3*2**n+3)//6` is a byte longer (at n = 0 the floor of
  1/6 is 0), and `(3**n+3)//6-2**n//2` two bytes. Keeping 3ⁿ and 2ⁿ in
  variables, `t=b=1` / `while[print(t//6-~-b//2)]:t*=3;b*=2`, is 41
  bytes; the recurrences a(n) = 3a(n−1) + 2ⁿ⁻² − 1 and
  a(n) = 5a(n−1) − 6a(n−2) + 1 need a second state or a fix for small n
  and come out longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000392), CC BY-SA 4.0.
