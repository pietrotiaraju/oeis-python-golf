# A001240

> Expansion of 1/((1-2x)(1-3x)(1-6x)).
> — [OEIS A001240](https://oeis.org/A001240)

Offset 1: 1, 11, 85, 575, 3661, 22631, 137845, 833375, 5019421, 30174551, 181222405, 1087861775, 6528756781, 39177307271, …

### Python 3 — 39 bytes

```python
p=1;q=3
while[print(~-p*q+p)]:p*=2;q*=3
```

**How it works**

- Partial fractions give [xᵐ] 1/((1−2x)(1−3x)(1−6x)) = 2ᵐ − 3·3ᵐ + 3·6ᵐ
  = (2ᵐ − 1)·3ᵐ⁺¹ + 2ᵐ, and a(n) is the coefficient of xⁿ⁻¹.
- `p` = 2ᵐ and `q` = 3ᵐ⁺¹, so `~-p*q+p` is the term.

**Notes**

- The whole b-file (100 terms) prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001240), CC BY-SA 4.0.
