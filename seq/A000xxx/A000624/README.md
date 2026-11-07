# A000624

> Number of monosubstituted alkanes C(n)H(2n+1)-X of the form shown in the Comments lines that are not stereoisomers.
> — [OEIS A000624](https://oeis.org/A000624)

Offset 1: 0, 0, 0, 1, 1, 3, 4, 9, 13, 26, …

### Python 3 — 93 bytes

```python
A=1,
while[print(sum(map(int.__mul__,A[1:],A[-3:0:-2])))]:A+=sum(map(int.__mul__,A,A[::-2])),
```

**How it works**

- The form in the entry is the tertiary one: the carbon that holds X
  carries three nonempty alkyl groups. A(x) = ΣAₖxᵏ counts radicals
  with no asymmetric carbon ([A000621](../A000621/)):
  A = 1 + x·A(x)·A(x²).
- The central carbon is not asymmetric only if two of its three groups
  are equal, and no group may contain an asymmetric carbon. So the
  radical is an equal pair of non-stereoisomeric groups with i carbons
  each and a third one with j carbons, i, j ≥ 1, 2i + j = n − 1:
  **a(n) = [xⁿ⁻¹](A(x) − 1)(A(x²) − 1) = Σ AᵢAⱼ**.
- When the loop prints a(n), the tuple is A = (A₀,…,Aₖ) with
  k = n − 1. `A[1:]` is A₁, A₂, … and `A[-3:0:-2]` is Aₖ₋₂, Aₖ₋₄, …
  stopping before A₀; `map` pairs them up to the shorter one, which is
  exactly the sum above (empty for k < 3).
- The body appends Aₖ₊₁ = ΣᵢAᵢAₖ₋₂ᵢ with the full lists, as in
  A000621.

**Notes**

- Exact integer arithmetic, O(n) per term.
- The reference file has the 3000 terms of the OEIS b-file; the bar is
  all 3000 in 60 s (the program needs about 7 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000624), CC BY-SA 4.0.
