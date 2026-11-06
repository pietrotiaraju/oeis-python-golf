# A000363

> Number of permutations of [n] with exactly 2 increasing runs of length at least 2.
> — [OEIS A000363](https://oeis.org/A000363)

Offset 4: 5, 61, 479, 3111, 18270, 101166, 540242, 2819266, 14494859, …

### Python 3 — 49 bytes

```python
n=4
while[print(5**n-(2*n-1)*(3**n-n)-n>>4)]:n+=1
```

**How it works**

- The OEIS closed form (V. Kotesovec) is
  a(n) = (5ⁿ − (2n−1)·3ⁿ + 2n² − 2n − 2)/16.
- −(2n−1)·3ⁿ + 2n² − 2n is −(2n−1)(3ⁿ − n) − n, which is shorter to
  write. The −2 is left out: the numerator without it is 16·a(n) + 2,
  and the floor `>>4` still gives a(n).
- `>>` binds more loosely than `+` and `-`, so the whole numerator needs
  no parentheses, a byte under `(…)//16`.

**Notes**

- Why the closed form holds: by Gessel's run theorem, giving weight t
  to each increasing run of length ≥ 2 makes the e.g.f.
  1/C(x), with C(x) = Σ_k (1−t)ᵏ·(x^(2k)/(2k)! − x^(2k+1)/(2k+1)!)
  (the coefficients come from 1/(1 + z + tz²/(1−z)) = (1−z)/(1−(1−t)z²)).
  The t² part of 1/C(x) is an exponential polynomial built from
  x^j·e^x, x^j·e^(3x) (j ≤ 2) and e^(5x), and so is the closed form; both
  then satisfy one linear recurrence of order at most 9, and they agree
  for n = 4 … 30 (checked with exact fractions), so they agree for every
  n. A brute-force count agrees for n ≤ 9.
- Exact integer arithmetic. Only the 4300-digit int-to-str limit of
  Python 3.11+ stops it, after about 6000 terms. The whole b-file
  (997 terms, n = 4 to 1000) prints at once; the bar is the whole b-file
  in 60 s.
- The formula as written with `//16` is 54 bytes, and
  `5**n+3**n-2*n*(3**n-n+1)>>4` one byte longer than the record.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000363), CC BY-SA 4.0.
