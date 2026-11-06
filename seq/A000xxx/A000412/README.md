# A000412

> Number of bipartite partitions of n white objects and 3 black ones.
> — [OEIS A000412](https://oeis.org/A000412)

Offset 0: 3, 7, 16, 31, 57, 97, 162, 257, 401, 608, …

This is a multiset partition of n identical white objects and 3
identical black ones. A fixed black total reduces the two-variable
product to the ordinary partition series and a fixed collection of
rational filters, combined directly without a polynomial convolution.

### Python 3 — 152 bytes

```python
a=[1];n=b=c=0;Q=[0]*2,[0]*3
while 1:
 b+=a[-1];c+=b;t=b
 for L in Q:L+=[t:=t+L.pop(0)]
 print(b+c+t)
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
- The black partitions 3, 2+1 and 1+1+1 give
  **P(x)(1/D₁+1/D₁²+1/D₃)=H₁+H₁/(1−x)+H₃**.
- b is the coefficient stream H₁, updated by adding the next
  ordinary partition number. The accumulator c is H₁/(1−x).
  Starting from t=b, the two queues of lengths 2 and 3 produce
  H₃. Their sum `b+c+t` is the requested coefficient.
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
- The b-file has 10001 terms. The unchanged verification bar is
  the complete reference file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 275 | first entry |
| 2026-11-06 | Python 3 | 261 | use sumprod on padded coefficient history and combine queue updates |
| 2026-11-06 | Python 3 | 152 | sum the black-partition cases directly and use the divisor recurrence |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000412), CC BY-SA 4.0.
