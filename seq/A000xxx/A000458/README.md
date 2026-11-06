# A000458

> a(0) = a(1) = 1; thereafter a(n) = sigma(a(n-1)) + sigma(a(n-2)).
> — [OEIS A000458](https://oeis.org/A000458)

Offset 0: 1, 1, 2, 4, 10, 25, 49, 88, 237, 500, …

### Python 3 — 137 bytes

```python
def s(n):
 p=2;t=1
 while p*p<=n:
  a=1
  while n%p<1:n//=p;a=a*p+1
  t*=a;p+=1
 return t*(n+(n>1))
a=b=1
while[print(a)]:a,b=b,s(a)+s(b)
```

**How it works**

- σ(m) is the sum of all positive divisors of m, including 1
  and m itself. If m=∏pᵉ, unique prime factorization gives
  σ(m)=∏(1+p+…+pᵉ); the function s computes this product.
- Trial division removes every copy of the current p. Starting
  with a=1, `a=a*p+1` gives 1+p after one copy, 1+p+p²
  after two, and so on. Multiply that factor into t only after
  all copies of p have been removed.
- The bound `p*p<=n` uses the remaining cofactor n, which shrinks
  during factorization. Once the bound fails, the cofactor is either
  1 or a prime of exponent 1, whose divisor sum is n+1.
  This explains the conditional final multiplication.
- For m=1 the loop is empty and s returns 1, the correct σ(1).
  Composite trial values of p extract nothing after all their
  smaller prime factors have already been removed.
- At the print, a and b are consecutive sequence values, initially
  a(0)=a(1)=1. The simultaneous assignment
  `a,b=b,s(a)+s(b)` advances to the next pair while both
  function calls still read the old values.
- For example a(2)=1+1=2, a(3)=σ(1)+σ(2)=1+3=4,
  and a(4)=σ(2)+σ(4)=3+7=10. Both initial ones are printed.

- After trial division, the remaining n is 1 or a prime. The
  factor `n+(n>1)` is respectively 1 or n+1, combining the
  exhausted-factor case and the final prime's divisor sum.

**Notes**

- Exact integer factorization and the multiplicative divisor-sum
  identity prove every recurrence update. No approximate prime
  test, fixed-width arithmetic or precomputed answer table is used.
- The variable a inside s is local to that function; it does not
  overwrite the outer sequence state with the same name.
- Only the consecutive pair and temporary factorization state are
  stored. Trial division can require O(√m) steps on a large prime
  input m, so later terms become expensive even while their decimal
  representations remain manageable.
- The next iteration recomputes the divisor sum of the value just
  shifted into a. Caching it could save work, at the cost of more
  state and code; the present program favors the shorter recurrence.
- The b-file has 101 terms (indices 0 through 100). The bar is the
  first 40 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 146 | first entry |
| 2026-11-06 | Python 3 | 137 | combine the remaining-prime and exhausted-factor cases |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000458), CC BY-SA 4.0.
