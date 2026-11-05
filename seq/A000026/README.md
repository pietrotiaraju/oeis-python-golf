# A000026

> Mosaic numbers or multiplicative projection of n: if n = Product (p_j^k_j)
> then a(n) = Product (p_j * k_j).
> — [OEIS A000026](https://oeis.org/A000026)

Offset 1: 1, 2, 3, 4, 5, 6, 7, 6, 6, 10, 11, 12, 13, 14, 15, 8, 17, 12, 19, 20, …

### Python 3 — 95 bytes

```python
n=a=1
while[print(a)]:
 m=n=n+1;a=p=1
 while~-m:
  p+=1;e=1
  while m%p<1:m//=p;e+=p-e%p
  a*=e
```

**How it works**

- Plain trial division: m starts as n, and each p = 2, 3, … is divided out
  of m as often as it goes. A composite p never divides m, because its prime
  factors were removed before p is reached, so every p that divides is a
  prime pᵉ ∥ n. The loop stops when m = 1 (`while~-m:`, since `~-m` is
  m − 1), that is at the largest prime factor of n.
- The factor p·e is built in `e`, which starts at 1 for each p. On the first
  division `e%p` is 1 (p ≥ 2), so `e+=p-e%p` turns 1 into p; after that `e`
  is a multiple of p, `e%p` is 0, and each division adds p. After e
  divisions `e` is p·e. When p does not divide m, `e` stays 1 and `a*=e`
  changes nothing.
- Starting `e` at 0 with `e+=p` needs `a*=e or 1` for the primes that do not
  divide, which is one byte more (96).
- `m=n=n+1` steps n and copies it into m in one statement.
- `while[print(a)]:` prints in the loop condition: `[None]` is a non-empty
  list, so it is true. `n=a=1` makes the first line a(1) = 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n. Since
  p·e ≤ pᵉ, a(n) ≤ n, and the terms never get near the int-to-str limit.
- Each term costs at most as many steps as the largest prime factor of n:
  the whole b-file (10 000 terms) prints in about 2 s. The bar is the whole
  b-file in 60 s.
- A single loop with `if m%p:a*=e;e=1;p+=1` / `else:m//=p;e+=p-e%p` needs
  `p=2` and a last `a*e` outside the loop and came out at 99 bytes, as did
  moving `a*=e` into the loop condition as `while~-m*(a:=a*e):`.

### Python 3 + sympy — 80 bytes

```python
from sympy import*
n=1
while[print(prod(f:=factorint(n))*prod(f.values()))]:n+=1
```

- `factorint(n)` is the dict {p: e}. `prod` (from the star import)
  multiplies the keys, which gives the radical p₁p₂⋯, and then the values,
  which gives the exponents' product e₁e₂⋯: a(n) = rad(n)·Πe, the formula
  A007947(n)·A005361(n) on the OEIS page. For n = 1 the dict is empty and
  both products are 1.
- The walrus is allowed as a call argument but not as the iterable of a
  comprehension, so `prod(p*f[p]for p in(f:=factorint(n)))` is a
  SyntaxError. `prod(p*e for p,e in factorint(n).items())` is 83 bytes.
- The whole b-file prints in about 1 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 95 | first entry |
| 2026-11-05 | Python 3 + sympy | 80 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000026), CC BY-SA 4.0.
