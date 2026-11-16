# A001860

> Number of series-reduced planted trees with n+9 nodes and 4 internal nodes.
> — [OEIS A001860](https://oeis.org/A001860)

Offset 0: 0, 3, 12, 29, 57, 99, 157, 234, 333, 456, 606, 786, 998, 1245, 1530, …

### Python 3 — 42 bytes

```python
n=1
while[print(n*(n*(8*n+3)-9)//18)]:n+=1
```

**How it works**

- **The trees.** A planted tree hangs from a root of degree 1; series-reduced
  means no node of degree 2. Cut off the root: what is left is a rooted tree
  whose 4 internal nodes each have at least two children, with n + 4 leaves
  (n + 8 nodes).
- **Skeletons.** The internal nodes form a rooted tree on 4 nodes, one of
  four shapes; then each internal node gets enough leaves to reach two
  children. With f = x²/(1 − x) (two or more leaves), the leaf generating
  functions are
  - path r–a–b–c: x·x·x·f/(1 − x)³ = x⁵/(1 − x)⁴;
  - r with children a, b and a with child c: x⁵/(1 − x)⁴;
  - r with child a, a with children b, c (swappable):
    x/(1 − x)² · (f(x)² + f(x²))/2;
  - r with three children (any permutation): (f(x)³ + 3f(x)f(x²) +
    2f(x³))/6/(1 − x).

  Their sum is x⁴·x(3 + 3x + 2x²)/((1 − x)³(1 − x³)), the OEIS generating
  function in x^(n+4): two rational functions of small degree that agree on
  their first 60 coefficients are equal. A brute-force enumeration of the
  trees agrees for n ≤ 21.
- **Closed form.** The coefficients are a cubic on each residue class
  mod 3. With m = n + 1, m(m(8m + 3) − 9) = 8n³ + 27n² + 21n + 2, and
  8n³ + 27n² + 21n + 2 − 18·a(n) is again a cubic on each class; it equals
  2, 4, 0 at four values of each class (n ≡ 0, 1, 2), so it is that
  constant everywhere and a(n) = ⌊m(m(8m + 3) − 9)/18⌋.
- **Golf.** Counting with m = n + 1 instead of n turns the OEIS numerator
  8n³ + 27n² + 21n + 9 into 8m³ + 3m² − 9m + 7, whose floor does not change
  when the 7 is dropped; then it factors as m(m(8m + 3) − 9): 42 bytes
  against 50.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001860), CC BY-SA 4.0.
