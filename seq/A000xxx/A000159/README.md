# A000159

> a(n) = A058087(n,n-3).
> — [OEIS A000159](https://oeis.org/A000159)

Offset 3: 2, 8, 20, 152, 994, 7888, 70152, 695760, 7603266, 90758872, …

### Python 3 — 77 bytes

```python
a=1;b=c=0;n=3
while[print(n*abs(2*(a+c)+~b)*2//3)]:a,b,c=b,c,~-n*(b-c)-a;n+=1
```

**How it works**

- Row n of A058087 lists the coefficients of the ménage hit polynomial
  U_n(t) = Σ_k (2n/(2n−k))·C(2n−k,k)·(n−k)!·(t−1)^k (Kaplansky and
  Riordan), highest power first, so a(n) is the coefficient of t³: the
  number of permutations π of 1..n with exactly three i such that
  π(i) ≡ i or i+1 (mod n).
- Two identities fold the factor 2n/(2n−k) and C(k,3) away (C(m,k)/m =
  C(m−1,k−1)/k with m = 2n−k, then C(k,3)/k = C(k−1,2)/3):
  a(n) = (2n/3)·e_2(n−1), where
  e_j(m) = Σ_k (−1)^(k−j)·C(k,j)·C(2m−k,k)·(m−k)! is the number of
  permutations of 1..m with exactly j i such that π(i) = i or i+1 (the
  straight-table hit numbers, [A058057](https://oeis.org/A058057)).
- e_2 = [A000222](../A000222/), and that page proves
  e_2(m) = 2W_m + W_{m−1} + 2W_{m−2} − (−1)^m with
  W_m = [A000271](https://oeis.org/A000271)(m) = e_0(m).
  So a(n) = (2n/3)·(2W_{n−1} + W_{n−2} + 2W_{n−3} + (−1)ⁿ).
- The program runs X_k = (−1)^k·W_k. W_{k+1} = k(W_k + W_{k−1}) + W_{k−2}
  (A000271, k ≥ 2) becomes X_{k+1} = k(X_{k−1} − X_k) − X_{k−2}, with plain
  copies. The state is (a,b,c) = (X_{n−3}, X_{n−2}, X_{n−1}), so the update
  multiplies by n−1 (`~-n`), and the seeds at n = 3 are X_0, X_1, X_2 = 1, 0, 0.
- In these variables the bracket is (−1)^(n−1)·(2X_{n−1} − X_{n−2} + 2X_{n−3} − 1)
  = (−1)^(n−1)·`(2*(a+c)+~b)` (`~b` is −b−1). The bracket is 3a(n)/(2n) ≥ 0,
  so `abs` takes the sign off, and `n*…*2//3` is exact because a(n) is an
  integer.

**Notes**

- Each term is a few big-integer operations. The whole b-file
  (248 terms) prints at once; the bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1558) (4299 digits). All printed terms agree with the hit-polynomial
  sum.
- The previous record (108 bytes) summed the folded formula term by term:
  `n*sum((-1)**j*j*~-j*comb(2*n-2-j,j)*perm(n+~j)for j in range(n))//3`.
- One byte longer: the plain basis W, with `n*(2*(a+c-n%2)-~b)*2//3`
  (−(−1)ⁿ = 2(n mod 2) − 1 in place of `abs`) and `~-n*(b+c)+a` in the update.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 108 | first entry |
| 2026-11-05 | Python 3 | 77 | 108 → 77: W-recurrence instead of the sum |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000159), CC BY-SA 4.0.
