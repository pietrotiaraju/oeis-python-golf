# A001981

> Restricted partitions.
> — [OEIS A001981](https://oeis.org/A001981)

Offset 0: 1, 1, 5, 13, 33, 73, 151, 289, 526, 910, 1514, 2430, 3788, 5744, 8512, …

### Python 3 — 90 bytes

```python
n=0
while 1:Q=(n+2)**8;V=x=1;exec("x*=Q;V*=x*Q**n-1;V//=~-x;"*8);print(V//Q**(4*n)%Q);n+=1
```

**How it works**

- **What is counted.** The name says only "restricted partitions". The entry's comment and its
  formula a(n) = A067059(n, 8) make it the number of partitions of 4n into
  at most n parts, each ≤ 8 (equivalently: at most 8 parts, each ≤ n), and
  all 1001 terms of the b-file agree with that; this page uses that
  definition.
- **Partitions in a box.** The partitions of w that fit in an n × 8 box (at
  most n parts, each ≤ 8) have the Gaussian binomial coefficient
  G(q) = ∏ᵢ₌₁⁸ (1 − q^(n+i))/(1 − qⁱ) as generating function, so a(n) is
  the coefficient of q^w in G(q), with w = 4n.
- **Evaluate, then read a digit.** The program computes V = G(Q) at the
  integer Q = (n + 2)⁸, one factor at a time: after factor i, V is the
  Gaussian binomial [n + i choose i] at Q, a polynomial with integer
  coefficients, so every step is exact. `x` is Qⁱ, `V*=x*Q**n-1` multiplies
  by Q^(n+i) − 1 and `V//=~-x` divides by Qⁱ − 1 (`~-x` is x − 1); `exec`
  repeats the step 8 times, shorter than a `for` loop inside the `while`
  line. The coefficients of G are ≥ 0 and add up to
  C(n + 8, 8) = ∏ᵢ (n + i)/i ≤ (n + 1)⁸ < Q, so each one is a base-Q
  digit of V, and a(n) = ⌊V/Q^w⌋ mod Q is `V//Q**(4*n)%Q`.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The slow
  part is the final division by Q^w, which grows faster than linearly with n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the first 760 terms in 60 s,
  reached in about 14 reference seconds; the whole b-file comes within the timeout.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 90 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001981), CC BY-SA 4.0.
