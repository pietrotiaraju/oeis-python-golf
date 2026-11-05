# A000082

> a(n) = n^2*Product_{p|n} (1 + 1/p).
> — [OEIS A000082](https://oeis.org/A000082)

Offset 1: 1, 6, 12, 24, 30, 72, 56, 96, 108, 180, 132, 288, …

### Python 3 — 75 bytes

```python
k=1
while 1:a=n=k;P=k=1;exec("P*=k*k;k+=1;a+=(P%k>n%k)*a//k;"*n);print(a*n)
```

**How it works**

- a(n) = n·ψ(n), where ψ(n) = n·∏(1 + 1/p) is the Dedekind psi function
  (A001615). `a` starts at n, gets one factor 1 + 1/p for each prime p
  dividing n, and is printed times n.
- The `exec` string runs n times and tries k = 2, 3, …, n+1. `P` is
  ((k−1)!)², kept up to date by `P*=k*k` before `k+=1`. By Wilson's theorem
  (k−1)! ≡ −1 (mod k) for a prime k, so `P%k` is 1. For a composite k,
  (k−1)! is divisible by k, except for k = 4, where 3! = 6 is not but
  3!² = 36 is. So `P%k` is 0, and squaring is what deals with k = 4.
- So `P%k>n%k` holds exactly when k is prime and n%k is 0: k is a prime
  divisor of n. Then `a+=a//k` multiplies `a` by 1 + 1/k. The division is
  exact: at that point `a` is n·∏(q+1)/q over the primes q < k that divide n,
  and k still divides it. Otherwise the product is 0 and `a` stays the same.
- The last try, k = n+1, never counts: n%(n+1) is n ≥ 1 and `P%k` is at most
  1. Running the string n times instead of n−1 avoids `*~-n`.
- After the `exec`, k is n+1, so `a=n=k` steps n for the next term without
  an `n+=1`. Starting `a` at n and printing `a*n` is two bytes shorter than
  `n=k;a=n*n` and `print(a)`.

**Notes**

- Exact integer arithmetic and Wilson's theorem, so the program is right for
  every n. ψ(n) ≤ σ(n) < n², so a(n) < n³, far from the int-to-str limit.
- The same program with `n=0` and `n+=1;a=n*n;…;print(a)` is 78 bytes, an
  inner `while k<=n:` loop instead of `exec` is 79, and trial division that
  divides each prime out of a copy of n is 97.
- `P*=k` with the test `P*P%k>n%k` is also 31 bytes inside the string.
  Without the square, `(k-1)!%4` is 2, and k = 4 would count as a prime
  divisor of every multiple of 4.
- Each term costs about n big-integer steps plus compiling a string of 31·n
  characters, so the whole b-file (1000 terms) takes about 12 s. The bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000082), CC BY-SA 4.0.
