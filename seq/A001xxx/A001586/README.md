# A001586

> Generalized Euler numbers, or Springer numbers.
> — [OEIS A001586](https://oeis.org/A001586)

Offset 0: 1, 1, 3, 11, 57, 361, 2763, 24611, 250737, 2873041, 36581523, …

### Python 3 — 80 bytes

```python
r=[1];k=s=-1
while[print(r[k])]:r=[s:=s+x for x in[-s]+r[:k-1:-1]+r[k::-1]];k-=1
```

**How it works**

- **A boustrophedon with a doubled middle.** Row m has 2m + 1 entries,
  row 0 is [1], and row m + 1 is the list of partial sums
  0, x₁, x₁ + x₂, … of row m read backwards *with its middle entry
  read twice*. The answer a(m) is the middle entry of row m:

  ```text
  [1]  →  [0, 1, 2]  →  [0, 2, 3, 4, 4]  →  [0, 4, 8, 11, 14, 16, 16]  →  …
  ```

- **Where it comes from.** Row m − 1 with its middle doubled counts the
  signed sequences x₁ > x₂ < x₃ > … of size m (absolute values a
  permutation of 1…m) by the rank of x₁ among −m…−1, 1…m: taking x₁
  away leaves such a sequence, read upside down, on the other letters
  that starts below x₁, and for x₁ > 0 its own negative is no longer
  available, which is what the doubled middle accounts for. The middle
  of row m adds up the upper half of row m − 1, i.e. the sequences
  with x₁ > 0: Arnold's type-B snakes, counted by a(m).
- **The generating function (a proof for every m).** Write the row
  as two halves that share the middle, β(m, t) = entry m − t and
  α(m, t) = entry m + t (0 ≤ t ≤ m). The rule says
  β(m, t) = β(m, t+1) + α(m−1, t) and α(m, t+1) = α(m, t) + β(m−1, t),
  with β(m, m) = 0 for m ≥ 1 (the leading 0) and α(m, 0) = β(m, 0).
  In coordinates A(i, j) = α(i+j, i), B(i, j) = β(i+j, j) these become
  A(i+1, j) − A(i, j+1) = B(j, i) and B(i+1, j) − B(i, j+1) = A(j, i),
  so the e.g.f.s satisfy (∂ₓ − ∂ᵧ)𝒜(x, y) = ℬ(y, x) and
  (∂ₓ − ∂ᵧ)ℬ(x, y) = 𝒜(y, x). Along each line x + y = s this is the
  oscillator equation, so 𝒜 = α(s)·cos x + β(s)·sin x and
  ℬ = β(s)·cos y − α(s)·sin y. The edges give ℬ(0, y) = 1 (row 0 is
  [1], the other first entries are 0) and 𝒜(0, y) = ℬ(y, 0), that is
  α = β and α(y)(cos y − sin y) = 1. The middles are 𝒜(0, y) = α(y),
  so Σ a(m)·yᵐ/m! = **1/(cos y − sin y)**, the entry's e.g.f.
  ([A001587](../A001587/) uses the same triangle with a weight and an
  input; there the input U(y) gives U(y)/(cos 3y − sin 3y).)
- **The slices.** With k = −m − 1, `r[k]` is the middle of row m,
  `r[:k-1:-1]` is the row from its end down to the middle and
  `r[k::-1]` from the middle down to the start: together, the row
  backwards with the middle twice.
- **The leading 0.** `s` still holds the last sum of the previous row,
  so starting the list with `-s` makes the first partial sum 0, three
  bytes under `[s:=0]+[…]`. `k=s=-1` gives s a starting value.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Row m costs O(m) big-integer additions; the whole b-file (433 terms,
  up to a(432)) prints in about a tenth of a second, and the program
  reaches a(1508) in about 2.5 s, where the next term passes Python's
  4300-digit int-to-str limit and it stops with a ValueError.
- The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 80 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001586), CC BY-SA 4.0.
