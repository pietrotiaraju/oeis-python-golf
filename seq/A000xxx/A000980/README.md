# A000980

> Number of ways of writing 0 as Sum_{k=-n..n} e(k)*k, where e(k) is 0 or 1.
> — [OEIS A000980](https://oeis.org/A000980)

Offset 0: 2, 4, 8, 20, 52, 152, 472, 1520, 5044, 17112, 59008, 206260, 729096, …

### Python 3 — 76 bytes

```python
q=1,;z=()
while[print(sum(x*x*2for x in q))]:z+=0,;q=*map(sum,zip(q+z,z+q)),
```

**How it works**

- A zero-sum subset of {−n, …, n} may or may not contain 0 (factor 2);
  its positive part P and its negative part −N are subsets of {1, …, n}
  with sum(P) = sum(N). So a(n) = 2 Σₛ qₛ², where qₛ counts subsets of
  {1, …, n} with sum s: the coefficients of ∏_{k=1..n} (1 + xᵏ).
- `q` is the tuple of those coefficients. Multiplying by 1 + xʲ adds the
  tuple to itself shifted by j: `zip(q+z,z+q)` with `z` = j zeros.
- `z` grows by one zero per pass (`z+=0,`), so it is the counter and the
  padding at once. Tuples rather than lists: `q=*map(…),` is 1 byte under
  `q=[*map(…)]`, and `q=1,;z=()` 1 byte under `q=[1];z=[]`.
- `sum(x*x*2for x in q)` is 1 byte under `2*sum(x*x for x in q)` (the
  `2for` only draws a `SyntaxWarning` on stderr).

**Notes**

- Exact integer additions; no theorem needed.
- The tuple holds n(n+1)/2 + 1 coefficients of about n bits each: 667
  terms in 60 s here, using under 70 MB. Packing ∏(1 + Bᵏ) into one big
  integer is longer here (about 100 bytes), because the base B has to grow
  with n and the product has to be rebuilt for every term.
- The b-file has 1669 terms; the bar is 520 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000980), CC BY-SA 4.0.
