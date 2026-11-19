# A001979

> Number of partitions of floor(7n/2) into n nonnegative integers each no more than 7.
> — [OEIS A001979](https://oeis.org/A001979)

Offset 0: 1, 1, 4, 10, 24, 49, 94, 169, 289, 468, 734, 1117, 1656, 2385, 3370, …

### Python 3 — 93 bytes

```python
n=0
while 1:Q=(n+2)**7;V=x=1;exec("x*=Q;V*=x*Q**n-1;V//=~-x;"*7);print(V//Q**(7*n//2)%Q);n+=1
```

**How it works**

- **What is counted.** Unordered choices of n numbers from {0, …, 7} with sum ⌊7n/2⌋
  are, after dropping the zeros, the partitions of ⌊7n/2⌋ into at most
  n parts, each ≤ 7.
- **Partitions in a box.** The partitions of w that fit in an n × 7 box (at
  most n parts, each ≤ 7) have the Gaussian binomial coefficient
  G(q) = ∏ᵢ₌₁⁷ (1 − q^(n+i))/(1 − qⁱ) as generating function, so a(n) is
  the coefficient of q^w in G(q), with w = ⌊7n/2⌋.
- **Evaluate, then read a digit.** The program computes V = G(Q) at the
  integer Q = (n + 2)⁷, one factor at a time: after factor i, V is the
  Gaussian binomial [n + i choose i] at Q, a polynomial with integer
  coefficients, so every step is exact. `x` is Qⁱ, `V*=x*Q**n-1` multiplies
  by Q^(n+i) − 1 and `V//=~-x` divides by Qⁱ − 1 (`~-x` is x − 1); `exec`
  repeats the step 7 times, shorter than a `for` loop inside the `while`
  line. The coefficients of G are ≥ 0 and add up to
  C(n + 7, 7) = ∏ᵢ (n + i)/i ≤ (n + 1)⁷ < Q, so each one is a base-Q
  digit of V, and a(n) = ⌊V/Q^w⌋ mod Q is `V//Q**(7*n//2)%Q`.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The slow
  part is the final division by Q^w, which grows faster than linearly with n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the first 800 terms in 60 s,
  reached in about 11 reference seconds; the whole b-file comes within the timeout.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001979), CC BY-SA 4.0.
