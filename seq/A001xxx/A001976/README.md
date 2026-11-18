# A001976

> Number of partitions of floor(5n/2)-1 into n nonnegative integers each no more than 5.
> — [OEIS A001976](https://oeis.org/A001976)

Offset 0: 0, 1, 3, 6, 11, 19, 32, 48, 71, 101, 141, 188, 249, 322, 414, 518, 645, …

### Python 3 — 95 bytes

```python
n=0
while 1:Q=(n+2)**5;V=x=1;exec("x*=Q;V*=x*Q**n-1;V//=~-x;"*5);print(V*Q//Q**(5*n//2)%Q);n+=1
```

**How it works**

- **What is counted.** Unordered choices of n numbers from {0, …, 5} with sum ⌊5n/2⌋ − 1
  are, after dropping the zeros, the partitions of ⌊5n/2⌋ − 1 into at most
  n parts, each ≤ 5.
- **Partitions in a box.** The partitions of w that fit in an n × 5 box (at
  most n parts, each ≤ 5) have the Gaussian binomial coefficient
  G(q) = ∏ᵢ₌₁⁵ (1 − q^(n+i))/(1 − qⁱ) as generating function, so a(n) is
  the coefficient of q^w in G(q), with w = ⌊5n/2⌋ − 1.
- **Evaluate, then read a digit.** The program computes V = G(Q) at the
  integer Q = (n + 2)⁵, one factor at a time: after factor i, V is the
  Gaussian binomial [n + i choose i] at Q, a polynomial with integer
  coefficients, so every step is exact. `x` is Qⁱ, `V*=x*Q**n-1` multiplies
  by Q^(n+i) − 1 and `V//=~-x` divides by Qⁱ − 1 (`~-x` is x − 1); `exec`
  repeats the step 5 times, shorter than a `for` loop inside the `while`
  line. The coefficients of G are ≥ 0 and add up to
  C(n + 5, 5) = ∏ᵢ (n + i)/i ≤ (n + 1)⁵ < Q, so each one is a base-Q
  digit of V, and a(n), the digit just below w, is ⌊V·Q/Q^w⌋ mod Q,
  `V*Q//Q**(5*n//2)%Q`; at n = 0 that is V·Q mod Q = 0, the right value
  for w = −1.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The slow
  part is the final division by Q^w, which grows faster than linearly with n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in 60 s,
  which takes about 10 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 95 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001976), CC BY-SA 4.0.
