# A001226

> Lerch's function q_2(n) = (2^{phi(t)} - 1)/t where t = 2*n - 1.
> — [OEIS A001226](https://oeis.org/A001226)

Offset 1: 1, 1, 3, 9, 7, 93, 315, 17, 3855, 13797, 195, 182361, 41943, 9709, 9256395, 34636833, 31775, 479349, …

### Python 3 — 79 bytes

```python
t=F=1
while[print(~-2**sum(1%t==pow(k,F,t)for k in range(t))//t)]:F*=t*-~t;t+=2
```

**How it works**

- For t = 2n − 1 the term is (2^φ(t) − 1)/t; `~-2**s//t` is (2ˢ − 1)//t.
- φ(t) counts the residues k with gcd(k, t) = 1. `F` is (t−1)!, a multiple
  of φ(t), so kᶠ ≡ 1 (mod t) for every k prime to t (Euler), while a k
  sharing a factor with t never gives 1. So `sum(1%t==pow(k,F,t)…)` is
  φ(t); for t = 1, `1%t` = 0 = 0ᶠ mod 1 counts φ(1) = 1.
- `F*=t*-~t;t+=2` multiplies in t and t + 1 before t steps to t + 2.

**Notes**

- `from math import*` with `gcd(k,t)<2` is 81 bytes.
- The whole b-file (200 terms) prints in about 6 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001226), CC BY-SA 4.0.
