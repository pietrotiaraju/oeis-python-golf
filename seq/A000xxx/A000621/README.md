# A000621

> Number of monosubstituted alkanes C(n-1)H(2n-1)-X with n-1 carbon atoms that are not stereoisomers.
> — [OEIS A000621](https://oeis.org/A000621)

Offset 1: 1, 1, 1, 2, 3, 5, 8, 14, 23, 39, …

### Python 3 — 60 bytes

```python
A=1,
while[print(A[-1])]:A+=sum(map(int.__mul__,A,A[::-2])),
```

**How it works**

- Following Blair and Henze, a radical is "not a stereoisomer" when it
  has no asymmetric carbon atom, that is, every carbon carries two
  identical substituents. Let A(x) = ΣAₖxᵏ count these radicals by
  number of carbons, with A₀ = 1 for a hydrogen; a(n) = Aₙ₋₁.
- The carbon that holds X has three other substituents, and two of them
  must be equal. Any branch containing an asymmetric carbon would make
  the whole radical a stereoisomer, so the equal pair is one
  non-stereoisomeric radical taken twice (series A(x²)) and the third
  is any non-stereoisomeric radical (series A(x)). Deeper carbons see
  the side that holds X as a unique substituent, so the same rule
  applies to them. Hence **A(x) = 1 + x·A(x)·A(x²)**, the functional
  equation in the OEIS entry (equivalently A = 1/(1 − x·A(x²))).
- With the tuple A = (A₀,…,Aₖ), `A[::-2]` is (Aₖ, Aₖ₋₂, …), and `map`
  stops at the shorter argument, so the sum is
  [xᵏ]A(x)A(x²) = ΣᵢAᵢAₖ₋₂ᵢ = Aₖ₊₁ with no index bounds.
- `while[print(A[-1])]:` prints the newest term before each step.

**Notes**

- Exact integer arithmetic; the convolution is O(n) per term.
- The reference file has the 3000 terms of the OEIS b-file; the bar is
  all 3000 in 60 s (the program needs about 4 s here). Python's
  4300-digit limit for printing integers would stop it near
  n ≈ 19000.
- The same series gives [A000624](../A000624/) and
  [A000627](../A000627/), and with the steric radicals of
  [A000625](../A000625/) also [A000620](../A000620/),
  [A000622](../A000622/) and [A000623](../A000623/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000621), CC BY-SA 4.0.
