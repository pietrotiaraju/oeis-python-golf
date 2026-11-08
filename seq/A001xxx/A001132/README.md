# A001132

> Primes == +-1 (mod 8).
> — [OEIS A001132](https://oeis.org/A001132)

Offset 1: 7, 17, 23, 31, 41, 47, 71, 73, 79, 89, 97, 103, 113, 127, 137, 151, 167, 191, 193, 199, …

These are also the odd primes for which 2 is a quadratic residue (the second
supplement to quadratic reciprocity), and the primes p with ord_p(2) | (p − 1)/2;
the siblings [A001133](../A001133/)–[A001136](../A001136/) ask for
ord_p(2) = (p − 1)/k exactly.

### Python 3 — 46 bytes

```python
P=k=1
while[-P%k*k%8%6==1==print(k)]:P*=k;k+=1
```

**How it works**

- The Wilson loop of [A000040](../../A000xxx/A000040/): `P` is (k − 1)!, and
  `-P%k` is 1 when k is prime, 0 for k = 1 and every composite k > 4, and 2
  for k = 4 (3! = 6).
- So `-P%k*k` is k itself for a prime and 0 or 8 otherwise. Taking it mod 8
  and then mod 6 maps the residues 0, 1, …, 7 to 0, 1, 2, 3, 4, 5, 0, 1: the
  result is 1 exactly for residues 1 and 7. Non-primes give 0, and the prime
  2 gives 2, so `==1` keeps just the primes ≡ ±1 (mod 8).
- The chained comparison `…==1==print(k)` runs `print(k)` only when the
  first test holds; the list around it is never empty, so the loop never
  stops.

**Notes**

- Exact for every n; it rests only on Wilson's theorem. P = (k − 1)! has
  about k log₂ k bits, so step k costs about k log k: 6933 terms in 60 s on
  the PC it was written on. The b-file has 10 000 terms (up to 225 343); the
  bar is 4500 terms in 60 s.
- Near misses: `-P%k*k*k%16==1` (odd squares are 1 mod 16 exactly for
  k ≡ ±1 mod 8) is 1 byte longer; the squared factorial (`P%k*k%8%6==1`,
  `P*=k*k`) saves one byte in the test and spends two in the update;
  `-P%k==1>k+1&4==print(k)` (k + 1 has bit 2 clear) is as long but also lets
  the prime 2 through.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001132), CC BY-SA 4.0.
