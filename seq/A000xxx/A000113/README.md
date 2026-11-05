# A000113

> Number of transformation groups of order n.
> — [OEIS A000113](https://oeis.org/A000113)

Offset 1: 1, 3, 4, 3, 6, 12, 8, 6, 4, 18, 12, 12, 14, 24, 24, 6, 18, 12, …

### Python 3 — 116 bytes

```python
A=[n:=1]*2
while p:=1:
 while p*p*n%576:p+=1
 print(A[n]*p//24);n+=1;p=2
 while n%p:p+=1
 A+=A[n//p]*(p+(n%p**2>0)),
```

**How it works**

- The OEIS formula: a(n) = ψ(n)/h, where ψ is Dedekind's psi function
  ([A001615](https://oeis.org/A001615)), ψ(n) = n·∏(1 + 1/p) over the primes
  p | n, and h = 2^i′·3^j′ with i′ = min(3, ⌊i/2⌋) and j′ = [j ≥ 2] for
  n = 2^i·3^j·k. Put another way, h is the largest divisor of 24 whose square
  divides n.
- The first inner loop finds the smallest k ≥ 1 with 576 | k²·n. At 2 this
  needs 2·v₂(k) + i ≥ 6, at 3 it needs 2·v₃(k) + j ≥ 2, and no other prime
  matters, so that k is 24/h. That makes a(n) = ψ(n)·k/24 exactly, which is
  `A[n]*p//24`.
- `A[m]` is ψ(m). For a new n, `while n%p:p+=1` finds its smallest prime
  factor p, and ψ(n) = ψ(n/p)·(p + 1) when p ∤ n/p and ψ(n/p)·p when it does
  divide. `n%p**2>0` is that test.
- Both loops have to start from scratch for every n, from 1 and from 2.
  `while p:=1:` makes the reset for the first one part of the loop
  condition, and `;p=2` handles the second.
- `A=[n:=1]*2` sets n = 1 and A = [1, 1], with ψ(1) = 1 at index 1.
  `A[0]` is never read, because n/p ≥ 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The prime-factor search costs up to n steps when n is prime, so the whole
  b-file (10000 terms) prints in about half a second and about 115 000 terms
  print in 60 s. The bar is the whole b-file in 60 s.
- Counting h directly as `sum(k*k*n%576<1for k in range(24))` (the k mod 24
  with 576 | k²n are the multiples of 24/h, so there are h of them) fits in a
  `while[print(…)]:` condition, but it comes to 120 bytes. Using
  `max(d for d in range(1,25)if 24%d<1>n%d**2)` for h is longer still.
- Searching for k from 2 in steps of 2, with 2304 in place of 576 and `//48`
  (which finds 2·24/h), lets one `k=p=2` reset both loops, but that is
  117 bytes.
- Without the list, ψ by trial division on every n (dividing each prime out
  of a copy of n) is 129 bytes, and keeping a list of primes is 123.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 116 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000113), CC BY-SA 4.0.
