# A000433

> n written in base where place values are positive cubes.
> — [OEIS A000433](https://oeis.org/A000433)

Offset 0: 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, …

The k-th digit from the right is the number of times the greedy algorithm
subtracts k³ from n (Joerg Arndt's comment): a(26) = 32 because
26 = 3·2³ + 2·1³, and a(27) = 100.

### Python 3 — 69 bytes

```python
a=[k:=0]
while[print(a[-1])]:k+=(k+1)**3<=len(a);a+=a[-k**3]+10**~-k,
```

**How it works**

- Let k be the largest integer with k³ ≤ n. The greedy algorithm first
  subtracts k³ as often as it can, then works on the rest with smaller cubes.
  Subtracting just one k³ leaves a number whose greedy representation is the
  same with the k-th digit lowered by one (if n − k³ ≥ k³ the largest cube is
  still k³; otherwise n − k³ < k³ is exactly the rest). So
  a(n) = a(n − k³) + 10^(k−1). The k-th digit of a(n − k³) is at most 6, since
  before the k³ place the remainder is below (k+1)³ ≤ 8k³, so no decimal
  carry occurs.
- The list a holds a(0), …, a(n−1) when a(n) is built, so `len(a)` is n and
  `a[-k**3]` is a(n − k³). n grows by one per pass, so k needs at most one
  step: `k+=(k+1)**3<=len(a)`. `10**~-k` is 10^(k−1).
- `a=[k:=0]` stores a(0) = 0 and sets k; `while[print(a[-1])]:` prints the
  newest term before the next one is appended.

**Notes**

- The greedy division from the top, with a string of digits per n: 114
  bytes. Taking the whole top digit at once,
  `n=len(a);k+=(k+1)**3<=n;a+=n//k**3*10**~-k+a[n%k**3],`: 82.
- Exact integer arithmetic, so the program is right for every n.
- The 10001 terms of the b-file print in a quarter of a second here; the list
  keeps every term.
- a(n) has ⌊n^(1/3)⌋ digits, so the 4300-digit int-to-str limit is not
  reached in practice.
- The b-file has 10001 terms (up to a(10000)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 114 | first entry |
| 2026-11-07 | Python 3 | 69 | a(n) = a(n − k³) + 10^(k−1) from the list of earlier terms |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000433), CC BY-SA 4.0.
