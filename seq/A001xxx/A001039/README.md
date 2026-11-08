# A001039

> a(n) = (p^p-1)/(p-1) where p = prime(n).
> — [OEIS A001039](https://oeis.org/A001039)

Offset 1: 3, 13, 781, 137257, 28531167061, 25239592216021, 51702516367896047761, …

### Python 3 — 50 bytes

```python
P=k=1
while k:=k+1:~P%k or print(~-k**k//~-k);P*=k
```

**How it works**

- Primes by Wilson's theorem, as in [A000040](../../A000xxx/A000040/):
  P = (k−1)! and `~P%k` is 0 exactly when k divides (k−1)! + 1.
- `~-x` is x − 1, and `**` binds tighter than the unary operators, so
  `~-k**k//~-k` is (kᵏ − 1)//(k − 1) = 1 + k + … + kᵏ⁻¹, an exact
  division.

**Notes**

- Exact integer arithmetic.
- The b-file has 26 terms and prints at once; the bar is the whole b-file.
  Near p = 1400 the terms pass 4300 digits and Python's int-to-str limit
  stops the program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001039), CC BY-SA 4.0.
