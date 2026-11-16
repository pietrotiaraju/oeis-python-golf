# A001858

> Number of forests of trees on n labeled nodes.
> — [OEIS A001858](https://oeis.org/A001858)

Offset 0: 1, 1, 2, 7, 38, 291, 2932, 36961, 561948, 10026505, 205608536, 4767440679, …

### Python 3 — 106 bytes

```python
import math
a=[n:=1]
while[print(a[-1])]:a+=sum(math.comb(n,k)*k**~-k*a[-k]for k in range(1,n+1))//n,;n+=1
```

**How it works**

- **Forests.** A forest on n labeled nodes is a set of trees, and there are
  kᵏ⁻² trees on k labeled nodes (Cayley). Mark one node of the forest: its
  tree has some k nodes, chosen in C(n, k) ways, with kᵏ⁻² shapes and k
  places for the mark, and the other n − k nodes form any forest. So
  n·a(n) = Σₖ₌₁..ₙ C(n, k)·kᵏ⁻¹·a(n − k), which is Alois P. Heinz's
  recurrence on the OEIS page times n (the e.g.f. is
  exp(Σ kᵏ⁻²xᵏ/k!)).
- **The program.** The list `a` holds a(0), …, a(n − 1), so `a[-k]` is
  a(n − k). `k**~-k` is kᵏ⁻¹ (`~-k` = k − 1), an integer for k ≥ 1, and the
  sum is divisible by n, so `//n` is exact. `a=[n:=1]` starts the list with
  a(0) = 1 and the index at 1. `import math` with one `math.comb` is 1 byte
  under `from math import*`.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 1373.
- The b-file has 389 terms (n = 0 to 388); the bar is the whole b-file in
  60 s, which takes about a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 106 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001858), CC BY-SA 4.0.
