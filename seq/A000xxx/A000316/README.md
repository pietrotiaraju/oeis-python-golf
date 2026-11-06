# A000316

> Two decks each have n kinds of cards, 2 of each kind. The first deck is laid out in order. The second deck is shuffled and laid out next to the first. A match occurs if a card from the second deck is next to a card of the same kind from the first deck. a(n) is the number of ways of achieving no matches.
> — [OEIS A000316](https://oeis.org/A000316)

Offset 0: 1, 0, 4, 80, 4752, 440192, 59245120, 10930514688, …

### Python 3 — 56 bytes

```python
a=d=n=0
while[print(a:=2**n+n*(d-2*a))]:d=4*n*(a+d);n+=1
```

**How it works**

- The forbidden positions form n disjoint 2×2 blocks, each with rook
  polynomial 1 + 4x + 2x², so by inclusion–exclusion
  a(n) = Σ_k (−1)ᵏ·r_k·(2n−k)! with Σ r_k xᵏ = (1 + 4x + 2x²)ⁿ.
  Writing (2n−k)! = ∫₀^∞ e^(−x) x^(2n−k) dx turns this into
  a(n) = L(qⁿ) with q = x² − 4x + 2 and L(f) = ∫₀^∞ e^(−x) f(x) dx
  (P. Bala's formula in the entry).
- Integration by parts gives L(f) = f(0) + L(f′). With q(0) = 2,
  q′ = 2(x−2) and x(x−2) = q + 2x − 2, the values A_n = L(qⁿ) and
  D_n = 2·L((x−1)qⁿ) satisfy
  A_n = 2ⁿ + n·(D_{n−1} − 2A_{n−1}) and D_n = 4n·(A_n + D_{n−1}),
  with A_0 = 1, D_0 = 0.
- The update of a sits inside `print` as a walrus and reads the old a
  and d. At n = 0 it gives 2⁰ = 1 whatever a and d hold, and then
  d = 4·0·(…) = 0 = D_0, so `a=d=n=0` needs no real seeds.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (101 terms, n = 0 to 100) prints at once; the program stops after
  a(779), when the next term passes the 4300-digit int-to-str limit of
  Python 3.11+. The bar is the whole b-file in 60 s.
- With C_n = L((x−1)qⁿ) itself the second update is `c=2*n*(a+2*c)`,
  2 bytes longer. Using L((x−2)qⁿ) instead couples three consecutive
  values of A, and the order-3 recurrence of V. Kotesovec in the entry
  has far longer coefficients.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000316), CC BY-SA 4.0.
