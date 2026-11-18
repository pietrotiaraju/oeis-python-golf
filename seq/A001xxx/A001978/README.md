# A001978

> Number of partitions of 3n-1 into n nonnegative integers each no more than 6.
> — [OEIS A001978](https://oeis.org/A001978)

Offset 0: 0, 1, 3, 8, 16, 32, 55, 94, 147, 227, 332, 480, 668, 920, 1232, 1635, …

### Python 3 — 92 bytes

```python
n=0
while 1:Q=(n+2)**6;V=x=1;exec("x*=Q;V*=x*Q**n-1;V//=~-x;"*6);print(V*Q//Q**(3*n)%Q);n+=1
```

**How it works**

- **What is counted.** Unordered choices of n numbers from {0, …, 6} with sum 3n − 1
  are, after dropping the zeros, the partitions of 3n − 1 into at most
  n parts, each ≤ 6.
- **Partitions in a box.** The partitions of w that fit in an n × 6 box (at
  most n parts, each ≤ 6) have the Gaussian binomial coefficient
  G(q) = ∏ᵢ₌₁⁶ (1 − q^(n+i))/(1 − qⁱ) as generating function, so a(n) is
  the coefficient of q^w in G(q), with w = 3n − 1.
- **Evaluate, then read a digit.** The program computes V = G(Q) at the
  integer Q = (n + 2)⁶, one factor at a time: after factor i, V is the
  Gaussian binomial [n + i choose i] at Q, a polynomial with integer
  coefficients, so every step is exact. `x` is Qⁱ, `V*=x*Q**n-1` multiplies
  by Q^(n+i) − 1 and `V//=~-x` divides by Qⁱ − 1 (`~-x` is x − 1); `exec`
  repeats the step 6 times, shorter than a `for` loop inside the `while`
  line. The coefficients of G are ≥ 0 and add up to
  C(n + 6, 6) = ∏ᵢ (n + i)/i ≤ (n + 1)⁶ < Q, so each one is a base-Q
  digit of V, and a(n), the digit just below w, is ⌊V·Q/Q^w⌋ mod Q,
  `V*Q//Q**(3*n)%Q`; at n = 0 that is V·Q mod Q = 0, the right value
  for w = −1.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The slow
  part is the final division by Q^w, which grows faster than linearly with n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in 60 s,
  which takes about 13 reference seconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001978), CC BY-SA 4.0.
