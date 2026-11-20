# A002098

> G.f.: 1/Product_{k>=1} (1-prime(k)*x^prime(k)).
> — [OEIS A002098](https://oeis.org/A002098)

Offset 0: 1, 0, 2, 3, 4, 11, 17, 29, 49, 85, 144, 226, 404, 603, 1025, 1679, …

### Python 3 — 119 bytes

```python
a=[1];*P,F,n=1,1
while[print(a[-1])]:P+=F%n*[n];F*=n*n;a+=sum(x*(q:=q*p)for p in P if(q:=p)for x in a[-p::-p])//n,;n+=1
```

**How it works**

- The generating function is ∏ 1/(1 − p·x^p) over the primes p, so a(n) is
  the sum, over the partitions of n into primes, of the product of the parts
  (equivalently, as the entry notes, the sum of all k whose prime factors,
  counted with repetition, add up to n).
- Logarithmic derivative: x·d/dx log 1/(1 − p·x^p) = Σ_{k ≥ 1} p^(k+1)·x^(kp), so
  n·a(n) = Σ_{p ≤ n} Σ_{k ≥ 1} p^(k+1)·a(n − kp).
- `a[-p::-p]` lists a(n − p), a(n − 2p), … from the list a(0), …, a(n − 1).
  The weight `q` runs through p², p³, …: the filter `if(q:=p)` (a prime, so
  always true) resets q = p at each prime, and `q:=q*p` multiplies before
  each use. The sum is n·a(n), and `//n` divides it exactly.
- Primes come from Wilson's theorem, as in the [A000607](../../A000xxx/A000607/)
  record: F = ((m − 1)!)², so F mod m is 1 when m is prime and 0 otherwise
  (also for m = 1, and for m = 4, where F = 36); `F*=n*n` then moves F on
  to (m!)².
- The starred assignment sets P = [], F = 1, n = 1 (a(0) = 1 is printed
  first).

**Notes**

- a(n) grows like 3^(n/3) (the factor 1/(1 − 3x³) has the smallest
  singularity), about 0.16·n digits.
- The b-file has 6275 terms (n = 0 to 6274). The program printed 5573 of
  them in 60 s here (4000 in about 20 s); the bar is 4200 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 119 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002098), CC BY-SA 4.0.
