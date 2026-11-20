# A002043

> MacMahon's solid partitions of n in which 2 is the smallest summand.
> — [OEIS A002043](https://oeis.org/A002043)

Offset 2: 3, 0, 6, 18, 40, 81, 201, 414, 916, 1899, 3973, 8059, 16402, 32561, 64520, 125986, 244448, …

### Python 3 — 113 bytes

```python
R=[0]*4+[1,0];n=-2
while 1:n-=2;R+=sum(d*d*~-d*sum(R[d::d])for d in range(n,-1))//n,;print(3*(R[-3]-R[-5])+R[-7])
```

**How it works**

- These are MacMahon's counts, not the true solid partitions
  ([A000293](../../A000xxx/A000293/)): his tables come from his guessed
  generating function Π_{i≥1} (1 − xⁱ)^(−i(i+1)/2)
  ([A000294](../../A000xxx/A000294/)), which first goes wrong at n = 6
  (141 against 140). In that model a part i comes in C(i + 1, 2) kinds, so
  "smallest summand 2" means parts ≥ 2 with at least one 2: the g.f. is
  (Π_{i≥2} − Π_{i≥3}) (1 − xⁱ)^(−C(i+1,2)). That is the entry's formula
  (Radcliffe, via A000294) and reproduces every term: 3 = C(3, 2) kinds of
  a lone 2, and a(3) = 0.
- With P = Π_{i≥2} (1 − xⁱ)^(−C(i+1,2)), the second product is
  P·(1 − x²)³, so the g.f. is P·(1 − (1 − x²)³) = (3x² − 3x⁴ + x⁶)·P and
  **a(n) = 3(P(n − 2) − P(n − 4)) + P(n − 6)**.
- P comes from the [A000294](../../A000xxx/A000294/) program with parts
  i ≥ 2 only: its log-derivative recurrence
  2m·P(m) = Σ_{i≥2} i²(i + 1)·Σⱼ P(m − ji), with d = −i, `d*d*~-d` and
  `R[d::d]` read from the end and n = −2m; `range(n,-1)` stops at d = −2.
- `R` starts with four zeros, so `R[-7]` and the slices that reach back
  past P(0) read 0, then P(0) = 1, P(1) = 0 and n = −2: the first pass
  makes P(2) and prints a(2).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 999 terms (n = 2 to 1000); the bar is the whole b-file in
  60 s, which takes about a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 113 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002043), CC BY-SA 4.0.
