# A001901

> Successive numerators of Wallis's approximation to Pi/2 (reduced).
> — [OEIS A001901](https://oeis.org/A001901)

Offset 0: 1, 2, 4, 16, 64, 128, 256, 2048, 16384, 32768, 65536, 262144, 1048576, …

### Python 3 — 37 bytes

```python
p=n=1
while[print(p&-p)]:n+=1;p*=n&-2
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
- **The program.** `p` is A(n), built as in A001900: `n` runs one ahead of the
  index, and `p*=n&-2` multiplies by n with its last bit cleared, the next
  factor 2, 2, 4, 4, 6, …. `p&-p` is the lowest set bit of p, the largest power
  of 2 dividing it, which is a(n).

**Notes**

- Equivalently a(n) = 2^(2n + 1 − s(n) − s(n + 1)), with s the binary digit
  sum (Legendre's formula for the power of 2 in n!·(n + 1)! = A(n)·B(n)).
- Exact integer arithmetic, so the program is right for every n; only the
  power of two is printed, so the int-to-str limit is far away.
- The b-file has 24 terms (n = 0 to 23); the bar is the whole b-file in 60 s,
  which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001901), CC BY-SA 4.0.
