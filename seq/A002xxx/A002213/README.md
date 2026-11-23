# A002213

> Number of tree-like polyhexes rooted at a hexagon and containing n hexagons.
> — [OEIS A002213](https://oeis.org/A002213)

Offset 1: 1, 1, 5, 20, 84, 354, 1540, 6704, 29610, 131745, 591049, 2669346, …

### Python 3 — 126 bytes

```python
L=[3,2];n=0
while 1:L+=((6*n+9)*L[-1]-5*n*L[n])//(n+3),;n+=1;print((2*L[-1]-3*L[n]-5*L[-3]+n%2*3*L[n//2]+n%3%2*4*L[n//3])//12)
```

**How it works**

- **Generating function** (Harary and Read 1970, as in the entry):
  G(x) = x + xU + (3/2)xU² + (1/2)xU(x²) + (1/3)xU³ + (2/3)xU(x³), where
  U = A − 1 and A(x) = Σ Aₖxᵏ = 1, 1, 3, 10, 36, … is the g.f. of
  [A002212](../A002212/). The root hexagon carries up to three branches;
  the U(x²) and U(x³) terms are the Pólya corrections for its symmetries.
- **No convolutions.** A satisfies xA² = (1 − x)(A − 1), so for m ≥ 1
  [xᵐ]A² = Aₘ₊₁ − Aₘ, and A³ = A·A² = (1 − x)(A² − A)/x gives
  [xᵐ]A³ = Aₘ₊₂ − 3Aₘ₊₁ + 2Aₘ. Expanding U² = A² − 2A + 1 and
  U³ = A³ − 3A² + 3A − 1: [xᵐ]U² = Aₘ₊₁ − 3Aₘ and
  [xᵐ]U³ = Aₘ₊₂ − 6Aₘ₊₁ + 8Aₘ. Putting these into G, for n ≥ 2:
  6a(n) = 2Aₙ₊₁ − 3Aₙ − 5Aₙ₋₁ + 3[n odd]A₍ₙ₋₁₎/₂ + 4[n ≡ 1 mod 3]A₍ₙ₋₁₎/₃.
- **n = 1 for free.** With A₀ replaced by 3/2 the same formula gives
  6a(1) = 6 − 3 − 15/2 + 9/2 + 6 = 6. A₀ enters nowhere else: the
  A002212 recurrence (k + 1)Aₖ = 3(2k − 1)Aₖ₋₁ − 5(k − 2)Aₖ₋₂ (proved
  on [its page](../A002212/)) multiplies A₀ by 0 at k = 2. So the program
  keeps `L` = 2A with `L[0]` = 3 and divides by 12.
- **The loop.** Each pass first appends 2Aₙ₊₂ by the recurrence (written
  with the old n, k = n + 2), steps n, and prints: `L[-1]`, `L[n]`,
  `L[-3]` are 2Aₙ₊₁, 2Aₙ, 2Aₙ₋₁. `n%2*3` and `n%3%2*4` are the
  divisibility factors (n%3%2 is 1 only for n%3 = 1), and both indices are
  floors: (n − 1)/2 = n//2 for odd n, (n − 1)/3 = n//3 for n ≡ 1.

**Notes**

- Exact integers: right for every n. The whole b-file (200 terms) comes in
  a few hundredths of a second; the bar is all of it in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 126 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002213), CC BY-SA 4.0.
