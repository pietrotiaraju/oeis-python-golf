# A001902

> Successive denominators of Wallis's approximation to Pi/2 (reduced).
> — [OEIS A001902](https://oeis.org/A001902)

Offset 0: 1, 1, 3, 9, 45, 75, 175, 1225, 11025, 19845, 43659, 160083, 693693, …

### Python 3 — 55 bytes

```python
A=B=n=1
while[print(B*(A&-A)//A)]:n+=1;A*=n&-2;B*=n-1|1
```

**How it works**

- **The product.** W(n) is Wallis's product (1/1)·(2/1)·(2/3)·(4/3)·(4/5)·(6/5)⋯
  cut after n + 1 factors, W(0) = 1: for k ≥ 1 the k-th factor is the even one
  of k, k + 1 over the odd one. Unreduced, W(n) = A(n)/B(n) with
  A(n) = 2·2·4·4·6⋯ = [A001900](../A001900/)(n) = 2ⁿ·⌈n/2⌉!·⌊n/2⌋! and
  B(n) = 1·1·3·3·5⋯ = (2⌈n/2⌉ − 1)!!·(2⌊n/2⌋ + 1)!!, which is odd.
- **What cancels.** The odd part of j! divides (2j − 1)!!: from
  (2j)! = 2ʲ·j!·(2j − 1)!!, the quotient is the odd part of C(2j, j). So the
  odd part of A(n) divides B(n), and since B(n) is odd,
  gcd(A(n), B(n)) is exactly the odd part of A(n). The reduced fraction is
  therefore 2ᵛ/(B(n)/odd(A(n))), where 2ᵛ is the largest power of 2 dividing
  A(n): the reduced numerators are powers of two.
- **The program.** A001901 shows the reduced denominator is
  B(n)/odd(A(n)) = B(n)·(A(n) & −A(n))/A(n). `A` and `B` hold the unreduced
  numerator and denominator; with `n` one ahead of the index k, the k-th factor
  is `n&-2` (2⌊(k + 1)/2⌋, the even one of k, k + 1) over `n-1|1` (k with its
  last bit set, the odd one). `B*(A&-A)//A` is exact because A & −A is the
  power-of-two part of A.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 25 terms (n = 0 to 24); the bar is the whole b-file in 60 s,
  which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001902), CC BY-SA 4.0.
