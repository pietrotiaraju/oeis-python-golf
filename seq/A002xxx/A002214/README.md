# A002214

> Number of unrooted hexagonal polyominoes with n cells and no reflections allowed.
> — [OEIS A002214](https://oeis.org/A002214)

Offset 1: 1, 1, 2, 7, 18, 64, 226, 856, 3306, 13249, 53794, 222717, …

### Python 3 — 120 bytes

```python
L=[3,2];n=0
while 1:L+=((6*n+9)*L[-1]-5*n*L[n])//(n+3),;n+=1;print((6*L[n]-5*L[-3]-L[-1]+3*L[n//2]+n%3%2*4*L[n//3])//12)
```

**How it works**

- **Generating function** (Harary and Read 1970; the form in the entry is
  Emeric Deutsch's): G(x) = x + xU + (1/2)(3x − 1)U² + (1/2)(1 + x)U(x²)
  + (1/3)xU³ + (2/3)xU(x³), where U = A − 1 and A(x) = Σ Aₖxᵏ = 1, 1, 3,
  10, 36, … is the g.f. of [A002212](../A002212/).
- **No convolutions.** A satisfies xA² = (1 − x)(A − 1), so for m ≥ 1
  [xᵐ]A² = Aₘ₊₁ − Aₘ, and A³ = A·A² = (1 − x)(A² − A)/x gives
  [xᵐ]A³ = Aₘ₊₂ − 3Aₘ₊₁ + 2Aₘ. Expanding U² = A² − 2A + 1 and
  U³ = A³ − 3A² + 3A − 1: [xᵐ]U² = Aₘ₊₁ − 3Aₘ and
  [xᵐ]U³ = Aₘ₊₂ − 6Aₘ₊₁ + 8Aₘ. Putting these into G, for n ≥ 2 (where
  exactly one of the U(x²) terms is present, with index ⌊n/2⌋ ≥ 1):
  6a(n) = 6Aₙ − 5Aₙ₋₁ − Aₙ₊₁ + 3A⌊ₙ/₂⌋ + 4[n ≡ 1 mod 3]A₍ₙ₋₁₎/₃.
- **n = 1 for free.** With A₀ replaced by 3/2 the same formula gives
  6a(1) = 6 − 15/2 − 3 + 9/2 + 6 = 6. A₀ enters nowhere else: the
  A002212 recurrence (k + 1)Aₖ = 3(2k − 1)Aₖ₋₁ − 5(k − 2)Aₖ₋₂ (proved
  on [its page](../A002212/)) multiplies A₀ by 0 at k = 2. So the program
  keeps `L` = 2A with `L[0]` = 3 and divides by 12.
- **The loop.** Each pass first appends 2Aₙ₊₂ by the recurrence (written
  with the old n, k = n + 2), steps n, and prints: `L[n]`, `L[-3]`,
  `L[-1]` are 2Aₙ, 2Aₙ₋₁, 2Aₙ₊₁. `n%3%2` is 1 only for n%3 = 1, and then
  (n − 1)/3 = n//3.
- The same expansion gives [A002213](../A002213/) (rooted at a hexagon),
  and with [A002215](../A002215/) it gives [A002216](../A002216/).

**Notes**

- Exact integers: right for every n. The whole b-file (200 terms) comes in
  a few hundredths of a second; the bar is all of it in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 120 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002214), CC BY-SA 4.0.
