# A000696

> Numbers k such that (1,k) is "good".
> — [OEIS A000696](https://oeis.org/A000696)

Offset 1: 1, 7, 31, 37, 109, 121, 127, 133, 151, 157, 403, 421, 511, …

### Python 3 — 79 bytes

```python
k=1
while X:=range(k):exec('X={m%2*k+m>>2for m in X};'*k);X-{0}or print(k);k+=2
```

**How it works**

- S is the set of numbers whose base-4 digits are 0 or 1
  ([A000695](../A000695/)). In the form Eigen, Ito and Prasad
  (*Universally bad integers and the 2-adics*, 2004) give de Bruijn's 1964
  question, a pair of positive odd numbers (a, b) is good when
  ℤ = aS ⊕ (−2b)S: every integer is
  a·s₁ − 2b·s₂ with s₁, s₂ in S in exactly one way. (The OEIS comment
  writes this loosely; this reading gives exactly the 44 terms of the
  b-file.) So k is a term when every integer n is uniquely s₁ − 2k·s₂.
- k must be odd, otherwise s₁ − 2k·s₂ misses the residues 2 and 3 mod 4. For
  odd k the last base-4 digits a, b ∈ {0, 1} of s₁, s₂ are forced by
  n ≡ a − 2kb (mod 4), since the four choices give the four residues. So the
  representation is unique if it exists, and it exists exactly when the map
  T(n) = (n − a + 2kb)/4 leads n to 0.
- With m = ⌊n/2⌋ one step of T followed by halving is
  U(m) = (m + k·(m mod 2))/4 rounded down, which is `m%2*k+m>>2`; n reaches
  0 exactly when m does (n ∈ {0, 1} gives T(n) = 0). Negative n climb to
  n ≥ 0, and every m ≥ 0 ends up in [0, k), which U maps into itself. So k
  is good exactly when every m in `range(k)` reaches 0.
- The program applies U to the whole set k times. The sets shrink
  (U(X) ⊆ X once U([0,k)) ⊆ [0,k)), so they are stable after at most k
  steps, and the stable set is the union of the cycles of U. It is {0} (0 is
  always fixed) exactly when k is good, which `X-{0}or print(k)` tests.

**Notes**

- Exact integer arithmetic, so the program is right for every k.
- `exec` of the k-fold string is 3 bytes shorter than
  `for _ in X:X={m%2*k+m>>2for m in X}` on its own line, but compiling that
  string makes it slower: 18 terms (k = 679) take about 10 s and the 19th,
  1579, about 54 s. The loop version prints 37 terms in 13 s, and
  `while X!=(X:={…}):0` (85 bytes) all 44 in 8 s. The bar is 17 terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000696), CC BY-SA 4.0.
