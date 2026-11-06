# A000440

> Number of permutations of an n-sequence discordant with three given permutations (see reference) in n-4 places.
> — [OEIS A000440](https://oeis.org/A000440)

Offset 4: 9, 30, 180, 980, 8326, 70272, 695690, 7518720, 89193276, 1148241458, …

### Python 3 — 240 bytes

```python
from math import*
n=4
while 1:
 B=(4*n)**n;z=B*B;w=z*z;a=b=c=0;d=1
 for v in([0,-2*z,-2*z*(1+B),3*w]+[0]*n)[:n]:a,b,c,d=b,c,d,(1+3*B)*d-2*z*c-z*(1+B)*b+w*a+v
 print(sum((-1)**(k-4)*comb(k,4)*perm(n-k)*(d//B**k%B)for k in range(4,n+1)));n+=1
```

**How it works**

- Let R_q(t)=Σₖ σ_(q,k)tᵏ be the rook polynomials in
  Margolius's bivariate generating function on the OEIS page.
  The requested answer is the coefficient of y^4 in
  Σₖ σ_(n,k)(n−k)!(y−1)ᵏ, converting rook placements into
  the hit count for the three specified permutations.
- Multiplying the generating function's denominator gives

  R_q=(1+3t)R_(q−1)−2t²R_(q−2)
  −(t²+t³)R_(q−3)+t⁴R_(q−4)+v_q,

  with R_0=1 and earlier values zero. Its numerator supplies
  v_1=0, v_2=−2t², v_3=−2t²(1+t), v_4=3t⁴,
  and v_q=0 afterwards.
- Evaluate the polynomials at t=B, using z=B² and w=B⁴.
  The scalar states a,b,c,d hold four consecutive evaluations,
  initially R_(−3),R_(−2),R_(−1),R_0. Each simultaneous
  assignment shifts them and appends R_q(B), preserving all old
  values for the recurrence.
- The list of v values supplies the four numerator corrections,
  followed by zeros; slicing to n entries performs exactly n
  updates. Thus d=R_n(B) when the final print is evaluated.
- For the current n≥4, every rook coefficient obeys
  0≤σ_(n,k)≤C(n,k)²k!≤4ⁿn!<(4n)ⁿ=B.
  The first bound chooses rows, columns and a bijection between
  them, before restricting to the allowed board. Hence the
  base-B digits of d are the coefficients with no carries:
  `d//B**k%B` retrieves σ_(n,k) exactly.
- The coefficient of y^4 in (y−1)ᵏ is
  (−1)^(k−4)C(k,4), zero for k<4. The final
  sum multiplies this by σ_(n,k) and (n−k)!;
  `perm(n-k)` is that factorial with one argument.
- The counter starts at n=4, the OEIS offset, and increases
  after each output. A new base and a fresh polynomial evaluation
  are used each time, so no previously packed digits need to be
  reinterpreted when the required base grows.

**Notes**

- Exact integer polynomial evaluation and coefficient extraction.
  Negative terms in the hit sum implement inclusion-exclusion;
  they cancel before printing the nonnegative count.
- The only stored constants are the generating function's recurrence
  and numerator coefficients. The program computes each rook
  polynomial and does not store an answer table.
- This is the same construction as
  [A000470](../A000470/),
  with a different hit coefficient.
  The coefficient index is 4, with the offset shown above.
- Each output uses n recurrence steps and at most n hit summands,
  but the packed integer has O(n² log n) bits. Those large
  integer products, powers and divisions dominate at larger n.
  Output eventually meets Python 3.11+'s default 4300-digit
  integer conversion limit, an interpreter limit.
- The b-file has 19 terms (indices 4 through 22). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 240 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000440), CC BY-SA 4.0.
