# A001558

> Number of hill-free Dyck paths of semilength n+3 and having length of first descent equal to 1 (a hill in a Dyck path is a peak at level 1).
> — [OEIS A001558](https://oeis.org/A001558)

Offset 0: 1, 3, 10, 33, 111, 379, 1312, 4596, 16266, 58082, 209010, 757259, …

### Python 3 — 79 bytes

```python
a=0;p,q,r,k=1,2,5,3
while[print(a:=(r-q-p-a)//2)]:k+=1;p,q,r=q,r,r*(4*k-2)//-~k
```

**How it works**

- Let C(z) = Σ Cₙzⁿ be the Catalan generating function (C = 1 + zC²).
  A Dyck path is a sequence of primitive pieces U·P·D with P a Dyck path;
  a hill is a piece with P empty. So hill-free paths have generating
  function F = 1/(1 − z(C−1)) = 1/(1 − z²C²) = C/(1 + zC), the Fine
  numbers.
- First descent of length 1: the first descent of the whole path lies in
  its first piece U·P·D. If P is a pyramid UʲDʲ its descent runs on into
  the closing D (length ≥ 2); otherwise it is the first descent of P. So
  the first piece must have P ≠ UD with first descent of length 1.
  Writing P = UʲD·R, the rest R goes from height j−1 down to 0, i.e.
  R = C₀·D·C₁·…·D·C_{j−1} with Dyck paths Cᵢ, and the descent has length 1
  iff C₀ is non-empty or j = 1. That gives zC + z(C−1)² for such P; taking
  away UD (z) leaves z(C−1)·C = z²C³, and the piece U·P·D is z³C³.
  Followed by any hill-free path: z³C³F, so
  **a(n) = [zⁿ] C³·F**, the generating function given on the OEIS page.
- From F = C/(1 + zC) and C = 1 + zC²: (2 + z)·F = 1 + C, hence
  (2 + z)·C³F = C³ + C⁴. Multiplying C − 1 = zC² by C^(j−1) gives
  zC^(j+1) = C^j − C^(j−1), and with it [zⁿ](C³ + C⁴) =
  C_{n+3} − C_{n+2} − C_{n+1}. So
  **2a(n) + a(n−1) = C_{n+3} − C_{n+2} − C_{n+1}**, with a(−1) = 0.
  (Equivalently a(n) = A000957(n+4) − A000957(n+3) − A000957(n+2) in terms
  of the Fine numbers, as the OEIS page says.)
- `p,q,r` hold C_{n+1}, C_{n+2}, C_{n+3} and `k` = n+3; the next Catalan
  number is C_k = C_{k−1}·(4k−2)/(k+1), an exact division. The print sets
  `a` to (r − q − p − a)/2, exact as well.

**Notes**

- Carrying three Fine numbers instead (F_m = (C_m − F_{m−1})/2) is also
  80 bytes; the single-Catalan form C_{n+3}·(n+1)(11n+24)/(4(2n+3)(2n+5))
  for the right side is longer (95), and so is `math.comb`.
- Exact integer arithmetic, so the program is right for every n; the first
  term over the 4300-digit int-to-str limit is a(7151).
- The b-file has 1000 terms (n = 0 to 999); they all print in well under a
  second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001558), CC BY-SA 4.0.
