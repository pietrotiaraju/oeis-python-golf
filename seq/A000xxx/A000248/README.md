# A000248

> Expansion of e.g.f. exp(x*exp(x)).
> — [OEIS A000248](https://oeis.org/A000248)

Offset 0: 1, 1, 3, 10, 41, 196, 1057, 6322, 41393, 293608, 2237921, 18210094, …

### Python 3 — 73 bytes

```python
r=[0]
for n in r:r+=n+1,;B=3*n**n;print(sum((B+k)**n//B**k%B for k in r))
```

**How it works**

- a(n) counts the idempotent maps f on an n-element set (f∘f = f): pick the
  k fixed points, then send each of the other n − k points to one of them.
  So a(n) = Σₖ C(n,k)·k^(n−k).
- By the binomial theorem (B+k)ⁿ = Σᵢ C(n,i)·k^(n−i)·Bⁱ, so the term
  C(n,k)·k^(n−k) is digit k of (B+k)ⁿ in base B. `(B+k)**n//B**k%B` reads
  it with B = 3nⁿ, so the program needs no binomial and no import.
- `r` is the list 0, 1, …, n + 1. The `for` loop walks it while `r+=n+1,`
  keeps appending, so it never ends, and the inner sum runs over the same
  list. Its last element k = n + 1 adds 0 (see below).

**Why the digits never carry**

- k = 0: Bⁿ has a single nonzero digit.
- 1 ≤ k ≤ n: the digits C(n,i)·k^(n−i) are all positive and add up to
  (k+1)ⁿ, so each is at most (k+1)ⁿ − 1 < (n+1)ⁿ = nⁿ(1 + 1/n)ⁿ < e·nⁿ < B.
- k = n + 1: n(n+1) ≤ 3nⁿ = B for every n ≥ 1, so
  (1 + (n+1)/B)ⁿ ≤ (1 + 1/n)ⁿ < e < B, which gives
  (B+n+1)ⁿ < B^(n+1). The quotient by B^(n+1) is 0.
- n = 0: every power is 1 and B = 3, so the sum is 1 + 0.

**Notes**

- (B+k)ⁿ has about n²·log₂ n bits and each term needs n + 2 of them, so the
  program slows down quickly: 100 terms in about 3 s and 160 in a minute on
  a desktop PC. The bar is 125 terms in 60 s; the b-file has 542
  (n = 0 to 541).
- `math.comb` costs 82 bytes and prints the whole b-file in under 2 s:
  `import math` / `n=0` /
  `while[print(sum(math.comb(n,k)*k**(n-k)for k in range(n+1)))]:n+=1`.
  A running binomial without the import is also 82:
  `n=0` / `while[print((c:=1)+sum((c:=c*(n-j)//-~j)*(n+~j)**-~j for j in range(n)))]:n+=1`.
- The `while` form of the digit trick is 74 bytes:
  `n=0` / `while[B:=3*n**n,print(sum((B+k)**n//B**k%B for k in range(n+1)))]:n+=1`.
  The growing list costs as much as `n=0` + `range(n+1)` + `n+=1`, and
  `B=3*n**n;` is a byte under the walrus in the list.
- B must also be at least 2 at n = 0, which rules out bases like 4^(n²)
  that are 1 there.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000248), CC BY-SA 4.0.
