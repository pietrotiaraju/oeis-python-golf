# A000491

> Number of bipartite partitions of n white objects and 5 black ones.
> — [OEIS A000491](https://oeis.org/A000491)

Offset 0: 7, 19, 47, 97, 189, 339, 589, 975, 1576, 2472, …

This is a multiset partition of n identical white objects and 5
identical black ones. A fixed black total reduces the two-variable
product to the ordinary partition series and a fixed collection of
rational filters, combined directly without a polynomial convolution.

### Python 3 — 193 bytes

```python
a=[1];n=c=0;Q=[[0]*k for k in range(1,6)]
while t:=a[-1]:
 T=[L.append(t:=t+L.pop(0))or t for L in Q]
 print(T[0]+(c:=c+2*sum(T[:2])+T[2])+t)
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
- The seven black partitions are 5, 4+1, 3+2, 3+1+1,
  2+2+1, 2+1+1+1 and 1+1+1+1+1. They give
  **P(x)(1/D₁+2/D₁²+2/(D₁D₂)+1/(D₁D₃)+1/D₅)**,
  equivalently
  **H₁+H₅+(2H₁+2H₂+H₃)/(1−x)**.
- The five queues produce T=[h₁,h₂,h₃,h₄,h₅], with t=h₅.
  Accumulate c+=2h₁+2h₂+h₃, which divides that stream by
  1−x. The output h₁+c+h₅ is therefore the required count.
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
- The b-file has 1001 terms. The unchanged verification bar is
  the complete reference file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 296 | first entry |
| 2026-11-06 | Python 3 | 284 | use sumprod on padded coefficient history and combine queue updates |
| 2026-11-06 | Python 3 | 193 | accumulate the five black-partition filters directly |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000491), CC BY-SA 4.0.
