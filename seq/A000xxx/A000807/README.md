# A000807

> Quadratic invariants.
> — [OEIS A000807](https://oeis.org/A000807)

Offset 0: 1, 2, 14, 182, 3614, 99302, 3554894, 159175382, 8654995454, 558786468422, 42086200603694, 3645412584724022, 358877175474325214, 39758874175808713382, 4915216680878167372814, 673139563824188490513302, 101475126400695241802946494, 16744618803625299734467026182, 3009508006546547958833397673454, 586534509256110664710632345740022, …

### Python 3 — 69 bytes

```python
r=[t:=1]
while[print(r[0])]:
 for s in-1,1:r=[t:=t+x for x in[s*t]+r]
```

**The formula**

Jovovic's e.g.f. on the OEIS page is F(x) = exp(e^x + e^(−x) − 2): a(n)
is b(2n), where b(m) = m!·[x^m] F(x). F is even, so b(m) = 0 for odd m,
and F′ = 2 sinh(x)·F gives b(m) = 2·Σ_{j odd} C(m−1, j)·b(m−1−j). For
even m put i = m−1−j: the odd-i terms are zero anyway, so

b(m) = 2·Σ_i C(m−1, i)·b(i)   (m even),

twice a binomial transform, like the Bell numbers' B(m) = Σ C(m−1, i)·B(i).

**How it works**

- This is the Bell-triangle program of [A000110](../A000110/) with a
  different first column. In the triangle each row starts with b(m) and
  every next entry adds the entry above it, so the last entry of row m is
  Σ_i C(m, i)·b(i); `t` is that last entry.
- One loop pass builds two rows. Row 2n+1 must start with b(2n+1) = 0:
  prepending `-t` makes the running sum start at t − t. Row 2n+2 must start
  with b(2n+2) = 2t: prepending `t` starts it at t + t. Both are
  `[s*t]` for `s` in −1, 1.
- `r[0]`, the head of the even row, is then a(n+1).

**Notes**

- Integer additions only, exact for every n.
- The b-file has 289 terms (n = 0 to 288) and they print in a fraction of a
  second (row 2n has 2n + 1 entries); the bar is the whole b-file.
- Gutkovskiy's a(n) = 2·Σ C(2n−1, 2k−1)·a(n−k) with `math.comb` is
  100 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 69 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000807), CC BY-SA 4.0.
