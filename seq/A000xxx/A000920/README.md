# A000920

> Differences of 0: 6!*Stirling2(n,6).
> — [OEIS A000920](https://oeis.org/A000920)

Offset 1: 0, 0, 0, 0, 0, 720, 15120, 191520, 1905120, 16435440, 129230640, 953029440, …

### Python 3 — 58 bytes

```python
n=1
while[print(6**n+~5**n*6+15*(2**n+1<<n)-20*3**n)]:n+=1
```

**How it works**

- 6!·S(n, 6) is the number of maps of an n-set onto a 6-set, and by
  inclusion–exclusion it is Σₖ (−1)ᵏ C(6, k)(6−k)ⁿ =
  6ⁿ − 6·5ⁿ + 15·4ⁿ − 20·3ⁿ + 15·2ⁿ − 6 for n ≥ 1 (the k = 6 term 0ⁿ is 0).
- Two bytes come off the plain sum: `~5**n*6` is (−5ⁿ − 1)·6 = −6·5ⁿ − 6,
  which absorbs the constant, and `15*(2**n+1<<n)` is 15·(4ⁿ + 2ⁿ), since
  `+` binds tighter than `<<`: (2ⁿ + 1)·2ⁿ.

**Notes**

- Other versions: the plain six-term sum is 60 bytes. The surjection
  recurrence T(n, k) = k·(T(n−1, k) + T(n−1, k−1)) unrolled over six
  variables, `a=b=c=d=e=0` / `while[print(a)]:a=6*(a+b);b=5*(b+c);…;e+=e+2`,
  is 74 bytes.
- Exact integer arithmetic.
- The b-file has 1000 terms; they print at once. The bar is the whole
  b-file in 60 s. a(5526) is the first term with more than 4300 digits, so
  printing stops there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000920), CC BY-SA 4.0.
