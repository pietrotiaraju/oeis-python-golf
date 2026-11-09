# A001320

> Number of self-complementary Boolean functions of n variables, up to equivalence under the group (C_2)^n of all 2^n complementations of variables.
> — [OEIS A001320](https://oeis.org/A001320)

Offset 1: 1, 3, 14, 240, 63488, 4227858432, 18302628885633695744, …

The group (C₂)ⁿ complements variables: f(x) is equivalent to f(x ⊕ c) for
every c in {0,1}ⁿ. A class is self-complementary when it also holds the
complement ¬f of its members (Harrison 1963). For n = 2 these are
{x₁, ¬x₁}, {x₂, ¬x₂} and {x₁ ⊕ x₂, ¬(x₁ ⊕ x₂)}, so a(2) = 3 as in the
entry; brute force over all functions gives 1, 3, 14, 240 for n ≤ 4.

### Python 3 — 36 bytes

```python
x=N=2
while[print(x-x//N)]:x*=x;N*=2
```

**How it works**

- Orbits by stabilizers: a set X splits into Σ_{f∈X} |G_f| / |G| orbits.
  If the class of f is self-complementary, the set S(f) of c with
  f(x ⊕ c) = ¬f(x) is not empty, and it is a coset of the stabilizer G_f
  (if c₀ is in it, c is in it exactly when c ⊕ c₀ fixes f), so
  |G_f| = |S(f)|.
- So a(n) = Σ_f |S(f)| / 2ⁿ = (1/2ⁿ) Σ_c #{f : f(x ⊕ c) = ¬f(x)}. No f
  works for c = 0. For c ≠ 0 the 2ⁿ points pair up as {x, x ⊕ c}, and f is
  free on one point of each of the 2ⁿ⁻¹ pairs: 2^(2ⁿ⁻¹) functions. Hence
  a(n) = (2ⁿ − 1)·2^(2ⁿ⁻¹)/2ⁿ, the formula in the entry, for every n ≥ 1.
- With N = 2ⁿ and x = 2^(N/2) this is x − x/N, and N divides x because
  2ⁿ⁻¹ ≥ n. The loop starts at n = 1 (x = N = 2, a(1) = 2 − 1 = 1); each
  step squares x and doubles N. `print` returns `None` and `[None]` is
  truthy, so the loop never ends by itself.

**Notes**

- `(N-1<<N//2)//N` with N alone is 37 bytes; `2**n-1<<2**~-n-n` with a
  counter n is 39 bytes.
- a(15) has 4933 digits, so printing it stops the program with Python's
  4300-digit int-to-str limit after 14 terms.
- The b-file is synthesized from the 9 terms of the entry; they print at
  once, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001320), CC BY-SA 4.0.
