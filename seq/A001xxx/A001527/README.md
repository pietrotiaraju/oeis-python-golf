# A001527

> a(n) = 2 * Sum_{i=0..n} C(2^n-1, i).
> — [OEIS A001527](https://oeis.org/A001527)

Offset 0: 2, 4, 14, 128, 3882, 412736, 151223522, 189581406208, …

### Python 3 — 61 bytes

```python
n=0
while[print(pow((B:=4<<n*n)+1,2**n-1,B**-~n)%~-B*2)]:n+=1
```

**How it works**

- Write m = 2ⁿ − 1. By the binomial theorem, (1 + B)ᵐ = Σ C(m, i)·Bⁱ;
  reducing it mod B^(n+1) keeps the terms i ≤ n, and since each
  C(m, i) ≤ mⁱ < B they do not carry into each other:
  `pow(B+1,2**n-1,B**-~n)` = Σ_{i≤n} C(m, i)·Bⁱ, the wanted binomials as
  base-B digits. Three-argument `pow` gets there in about n squarings mod
  B^(n+1), never forming (1 + B)ᵐ itself (m is about a billion at n = 30).
- B ≡ 1 (mod B − 1), so that number is ≡ the sum of its digits
  Σ_{i≤n} C(m, i) mod B − 1, and `%~-B` (`~-B` = B − 1) returns the sum
  itself as long as it is below B − 1. Then `*2`.
- B = `4<<n*n` = 2^(n²+2) is big enough: for n ≥ 2,
  Σ_{i≤n} C(m, i) ≤ Σ_{i≤n} mⁱ ≤ 2mⁿ < 2^(n²+1) < B − 1, and also
  C(m, i) ≤ mⁱ < 2^(n²) < B; for n = 0, 1 the sums are 1 and 2, below
  B − 1 = 3 and 7. The walrus names B inside the `pow` call.

**Notes**

- The plain sum, `from math import*` / `n=0` /
  `while[print(2*sum(comb(2**n-1,i)for i in range(n+1)))]:n+=1`, is
  81 bytes.
- Exact integer arithmetic, so the program is right for every n. The
  modulus has about n³ bits, which is small for every n the 4300-digit
  int-to-str limit allows (a(123) has more than 4300 digits).
- The b-file has 31 terms (n = 0 to 30); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001527), CC BY-SA 4.0.
