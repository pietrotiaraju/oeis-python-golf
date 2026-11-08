# A000980

> Number of ways of writing 0 as Sum_{k=-n..n} e(k)*k, where e(k) is 0 or 1.
> — [OEIS A000980](https://oeis.org/A000980)

Offset 0: 2, 4, 8, 20, 52, 152, 472, 1520, 5044, 17112, 59008, 206260, 729096, …

### Python 3 — 73 bytes

```python
r=2,;z=()
while[print(max(r))]:z+=0,;exec("r=*map(sum,zip(r+z,z+r)),;"*2)
```

**How it works**

- A zero-sum subset of {−n, …, n} may or may not contain 0 (factor 2);
  its positive part P and its negative part −N are subsets of {1, …, n}
  with sum(P) = sum(N). So a(n) = 2 Σₛ qₛ², where qₛ counts subsets of
  {1, …, n} with sum s: the coefficients of Q = ∏_{k=1..n} (1 + xᵏ).
- Q is palindromic (qₛ = q_{T−s}, T = n(n+1)/2), so Σₛ qₛ² is the
  coefficient of x^T in Q², and by Cauchy–Schwarz every other coefficient
  Σₛ qₛ q_{k−s} of Q² is at most Σₛ qₛ². So a(n) is simply the largest
  coefficient of 2Q²: `max(r)`.
- `r` is the tuple of coefficients of 2Q², starting from `2,`. Multiplying
  by 1 + xʲ adds the tuple to itself shifted by j, `zip(r+z,z+r)` with
  `z` = j zeros, and the `exec` string does it twice: (1 + xʲ)².
- `z` grows by one zero per pass (`z+=0,`), so it is the counter and the
  padding at once. Tuples rather than lists: `r=*map(…),` is 1 byte under
  `r=[*map(…)]`, and `r=2,;z=()` 1 byte under `r=[2];z=[]`.

**Notes**

- Exact integer additions; besides the counting above only
  Cauchy–Schwarz is used.
- The first entry kept Q itself and printed `sum(x*x*2for x in q)`
  (76 bytes, about 670 terms in 60 s); the tuple of 2Q² is twice as long
  and takes two passes, so this one is slower: 613 terms in 60 s here.
  Packing ∏(1 + Bᵏ) into one big integer is longer (about 100 bytes),
  because the base B has to grow with n and the product has to be rebuilt
  for every term.
- The b-file has 1669 terms; the bar is 520 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 76 | first entry |
| 2026-11-07 | Python 3 | 73 | largest coefficient of 2Q² (Cauchy–Schwarz) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000980), CC BY-SA 4.0.
