# A001112

> A continued fraction.
> — [OEIS A001112](https://oeis.org/A001112)

Offset 0: 0, 1, 1, 3, 4, 11, 136, 283, 419, 1121, 1540, 38081, …

### Python 3 — 63 bytes

```python
p=n=0;q=1
while[print(p)]:p,q=q,b'1212<2121H'[n%10]%48*q+p;n+=1
```

**How it works**

- √162 = 12.727… has the continued fraction [12; 1, 2, 1, 2, 12, 2, 1, 2,
  1, 24] with period 10 (the usual m, d, a recurrence for a quadratic surd,
  m → d·a − m, d → (162 − m²)/d, a → ⌊(12 + m)/d⌋, comes back to its start
  after 10 steps). The convergent denominators are q_k = a_k·q_{k−1} +
  q_{k−2} with q_{−1} = 0, q_0 = 1, and the sequence is q_{−1}, q_0, q_1, …
  (the OEIS a(0) = 0 is q_{−1}).
- `p, q` hold q_{k−1}, q_k; each step prints p and moves on with the next
  partial quotient a_{k+1}.
- The ten quotients sit in a bytes literal: `b'1212<2121H'[n%10]` reads 49,
  50, 49, 50, 60 (`<`), …, 72 (`H`), and `%48` turns them into 1, 2, 12, 24.
  `%48*q` needs no parentheses: `%` and `*` group left to right.

**Notes**

- Computing the quotients with the m, d, a recurrence
  (`m=d*a-m;d=(162-m*m)//d;a=(12+m)//d`) is 77 bytes.
- The whole b-file (201 terms) prints instantly; the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001112), CC BY-SA 4.0.
