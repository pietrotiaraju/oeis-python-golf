# A000465

> Number of bipartite partitions of n white objects and 4 black ones.
> — [OEIS A000465](https://oeis.org/A000465)

Offset 0: 5, 12, 29, 57, 109, 189, 323, 522, 831, 1279, …

This is a multiset partition of n identical white objects and 4
identical black ones. A fixed black total reduces the two-variable
product to the ordinary partition series and a fixed collection of
rational filters, combined directly without a polynomial convolution.

### Python 3 — 187 bytes

```python
a=[1];n=c=0;Q=[[0]*k for k in range(1,5)]
while t:=a[-1]:
 T=[L.append(t:=t+L.pop(0))or t for L in Q]
 print((c:=c+(b:=T[0]+T[1]))+b+t)
 n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- A part is a pair (i,j) of nonnegative white and black counts,
  not both zero. Since parts form a multiset, their bivariate
  generating function is ∏_((i,j)≠(0,0))(1−xⁱyʲ)⁻¹.
- Let P(x)=∏ᵢ≥₁(1−xⁱ)⁻¹ and D_r(x)=∏ᵢ₌₁ʳ(1−xⁱ).
  Euler's q-binomial identity shows that a partition of the fixed
  black total with m_j parts of size j contributes
  P(x)/∏ⱼD_(m_j)(x). Write H_r=P/D_r.
- The black partitions 4, 3+1, 2+2, 2+1+1 and 1+1+1+1 give
  **P(x)(1/D₁+1/D₁²+1/D₂+1/(D₁D₂)+1/D₄)**.
  Equivalently this is
  **H₁+H₂+H₄+(H₁+H₂)/(1−x)**.
- The four queues produce T=[h₁,h₂,h₃,h₄] for the current
  coefficient, with t=h₄ after the final queue. Set b=h₁+h₂
  and accumulate c+=b; this implements division of H₁+H₂ by
  1−x. The output is c+b+t.
- Each queue L of length r implements division by 1−xʳ:
  the current output is the input plus the output r steps earlier.
  `pop(0)` retrieves that earlier value, and the updated value is
  appended to the queue. All queues start with zeros.
- The ordinary partition numbers in a use the logarithmic derivative
  of P:

  **m·p(m)=Σₖ₌₁ᵐ k·Σⱼ₌₁^⌊m/k⌋ p(m−jk)**.

  Before the append, n=−m and d=−k; `a[d::d]` contains
  p(m−k),p(m−2k),… . The two minus signs cancel in the quotient.
  Starting from p(0)=1 generates the exact partition stream.

- The assignment expression in the while condition loads the next
  partition number into t. Partition numbers are positive, so this
  condition keeps running. `L.append(...)` returns None; `or t`
  records the queue's new integer output in T after saving it in L.

**Notes**

- Every step is an exact formal-series identity. The finite black
  cases above explain all constants and coefficients in the code.
- One growing list stores ordinary partition numbers; the rational
  filters need only queues of fixed lengths and cumulative totals.
  No history of the final filtered stream is stored.
- The divisor recurrence uses O(m log m) entries for coefficient m,
  plus large-integer arithmetic. The source is shorter, with more
  arithmetic per partition coefficient than the pentagonal recurrence.
- Python's integer-to-string conversion limit can eventually apply.
- The b-file has 5001 terms. The unchanged verification bar is
  the complete reference file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 284 | first entry |
| 2026-11-06 | Python 3 | 272 | use sumprod on padded coefficient history and combine queue updates |
| 2026-11-06 | Python 3 | 187 | accumulate the four black-partition filters directly |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000465), CC BY-SA 4.0.
