# A000331

> Related to zeros of Bessel function.
> — [OEIS A000331](https://oeis.org/A000331)

Offset 4: 5, 14, 1026, 4324, 311387, 6425694, 579783114, 4028104212, …

### Python 3 — 151 bytes

```python
K=8**5;a=[0,1<<K];n=1
while[n<4or print(a[n]%2**K)]:n+=1;a+=sum([w:=a[k]*a[-k]>>K,*[w:=w*r+(w>>K)for r in range(1,n)if k%r>n%r]][-1]for k in range(n)),
```

**How it works**

- The OEIS comment: a(n) is the coefficient of ν in the Rayleigh
  polynomial of index 2n. The Rayleigh function σ_n(ν) = Σ_k j_(ν,k)^(−2n),
  over the positive zeros of J_ν, is P_n(ν)/(4ⁿ·Q_n(ν)) with
  Q_n(ν) = ∏_{r≤n} (ν + r)^⌊n/r⌋, and P_n is the Rayleigh polynomial; for
  example σ₄ = (5ν + 11)/(256(ν+1)⁴(ν+2)²(ν+3)(ν+4)), so a(4) = 5. The
  constant terms P_n(0) are [A000175](../A000175/).
- J_(ν+1)/J_ν = 2Σσ_n x^(2n−1) satisfies a Riccati equation that gives
  σ₁ = 1/(4(ν+1)) and (ν + n)·σ_n = Σ_{k=1}^{n−1} σ_k σ_(n−k) (Kishore's
  recurrence). Exactly as on the A000175 page, the exponent of ν + r in
  Q_n/(Q_k·Q_(n−k)) is 1 when k mod r > n mod r (a carry in base r) and 0
  otherwise, and for r = n it cancels the factor ν + n, so
  P_n = Σ_k P_k·P_(n−k)·∏_{r<n, k mod r > n mod r} (ν + r), P₁ = 1, with
  nonnegative integer coefficients.
- Only P_n mod ν² is needed, a pair (c, l) = (P_n(0), a(n)) that multiplies
  like a dual number. The program packs it into one integer c·2^K + l with
  K = 8⁵ = 32768:
  - `a[k]*a[-k]>>K` is the product of two pairs: the l·l′ term falls below
    2^K and the shift drops it;
  - multiplying by ν + r maps (c, l) to (c·r, l·r + c), which on the packed
    integer is `w*r+(w>>K)`;
  - sums of pairs are sums of integers, and `a[n]%2**K` reads l back.
  All of this is exact as long as every l stays below 2^K and every product
  l·l′ of two earlier terms too; the c parts may be as large as they like.
- The comprehension keeps the running product in the walrus `w` (the inner
  list may be empty, so `[…][-1]` takes the last value instead of `max`),
  and `a[0] = 0` lets k run over `range(n)`, with `a[-k]` = P_(n−k) while
  `a` holds P_0 … P_(n−1). Terms are printed from n = 4; before that the ν
  coefficient is 0.

**Notes**

- Exactness, checked by computation: an exact program that keeps (c, l) as
  two separate integers (172 bytes, below) shows that a(n) < 10^4300 for
  n < 567, that a(567) has 14311 bits (more than 4300 digits), and that no earlier
  term has more than 14266 bits. So for n ≤ 567 every l and every product
  l·l′ is below 2^28532 < 2^K, the packed arithmetic is exact, and the
  program prints a(4) … a(566) correctly; at a(567) it stops on the
  4300-digit int-to-str limit of Python 3.11+, before 2^K could ever be
  reached.
- The exact two-integer version:
  `a=[0,n:=1];b=[0,0]` / `while 1:` / ` n+=1;c=l=0` /
  ` for k in range(n):p=a[-k];q=2*b[k]*p;p*=a[k];[(q:=q*r+p,p:=p*r)for r in range(1,n)if k%r>n%r];c+=p;l+=q` /
  ` a+=c,;b+=l,;n<4or print(l)`. It uses the symmetry k ↔ n − k of the
  carry condition to start each pair at (c_k·c_(n−k), 2·l_k·c_(n−k)).
- `M=2**8**5` with `//M` and `%M` is 4 bytes shorter but CPython divides
  by a 32768-bit number much more slowly than it shifts, and it falls
  below the b-file in 60 s.
- The whole b-file (192 terms) prints in about 5 s; about 360 terms come
  out in 60 s. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 151 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000331), CC BY-SA 4.0.
