# A000114

> Number of cusps of principal congruence subgroup Gamma^{hat}(n).
> — [OEIS A000114](https://oeis.org/A000114)

Offset 2: 3, 4, 6, 12, 12, 24, 24, 36, 36, 60, 48, 84, 72, 96, 96, …

### Python 3 — 86 bytes

```python
J=[0,n:=1]
while 1:n+=1;J+=n*n-sum(J[d>>n%d*n]for d in range(1,n)),;print(J[n]>>(n>2))
```

**How it works**

- The cusps of Γ(n) correspond to the pairs ±(x, y) mod n with
  gcd(x, y, n) = 1. There are J₂(n) such pairs (Jordan's totient, A007434),
  and for n ≥ 3 a pair and its negative are always different, so
  a(n) = J₂(n)/2. For n = 2 every pair is its own negative, so
  a(2) = J₂(2) = 3. `>>(n>2)` halves the count only from n = 3 on.
- J₂ comes from the identity Σ_{d|n} J₂(d) = n²: every pair (x, y) mod n
  has a gcd g with n, and dividing by g gives a primitive pair mod n/g.
  So J₂(n) = n² − Σ J₂(d) over the divisors d < n, and the list `J`
  keeps every value found so far.
- `J[d>>n%d*n]` reads J[d] when d divides n (the shift is 0). Otherwise
  the shift is at least n, more than the number of bits of d, so it reads
  `J[0]`, which is 0. That is 1 byte shorter than `J[d]for … if n%d<1`.
- `J=[0,n:=1]` holds the zero slot and J₂(1) = 1, and starts n at 1.

**Notes**

- A recursive lambda ties at 86 bytes but takes about 8 s for the
  b-file instead of 5:

  ```python
  f=lambda n:n*n-sum(f(d)for d in range(1,n)if n%d<1)
  n=2
  while[print(f(n)>>(n>2))]:n+=1
  ```

- Changing the base to `n*n+~n%2*4` (adding 4 at every even n, which
  only moves J₂(2) from 3 to 7) lets the print be `J[n]>>1` for every n,
  but costs 3 bytes more. OEIS's n²/2·∏(1 − 1/p²) needs the prime factors
  of n, and counting the pairs directly with `math.gcd(x,y,n)` takes
  n² steps a term, too slow for the bar and longer anyway.
- Exact integer arithmetic, so the program is right for every n. Each
  term costs n steps, so the time grows with the square of the number of
  terms. The values stay below n²/2, far from the int-to-str limit.
- The b-file has 9999 terms (n = 2 to 10000); they print in about 5 s.
  The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000114), CC BY-SA 4.0.
