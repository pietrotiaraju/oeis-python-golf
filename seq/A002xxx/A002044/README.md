# A002044

> MacMahon's solid partitions of n in which 3 is the smallest summand.
> — [OEIS A002044](https://oeis.org/A002044)

Offset 3: 6, 0, 0, 21, 60, 90, 182, 378, 861, 1737, 3458, 6717, 13377, 25877, 49949, 95085, 180254, …

### Python 3 — 125 bytes

```python
L=[1,1,0,0,0,0];n=-6
while 1:
 for K in-2,-3:L+=sum(d*d*~-d*sum(L[2*d::2*d])for d in range(n,K))//n,
 print(L[-2]-L[-1]);n-=2
```

**How it works**

- These are MacMahon's counts, not the true solid partitions
  ([A000293](../../A000xxx/A000293/)): his tables come from his guessed
  generating function Π_{i≥1} (1 − xⁱ)^(−i(i+1)/2)
  ([A000294](../../A000xxx/A000294/)), which first goes wrong at n = 6.
  In that model a part i comes in C(i + 1, 2) kinds, so "smallest summand
  3" means parts ≥ 3 with at least one 3: the g.f. is
  (Π_{i≥3} − Π_{i≥4}) (1 − xⁱ)^(−C(i+1,2)), the entry's formula
  (Rascoe). It reproduces every term: 6 = C(4, 2) kinds of a lone 3, then
  0, 0 for n = 4, 5.
- The program builds both products, A = Π_{i≥3} and B = Π_{i≥4}, with the
  [A000294](../../A000xxx/A000294/) recurrence
  2m·A(m) = Σ_{i≥3} i²(i + 1)·Σⱼ A(m − ji) (n = −2m, d = −i,
  `d*d*~-d`), and prints A(m) − B(m). `range(n,K)` with K = −2 or −3
  stops at d = −3 or −4.
- One list holds both, interleaved: A(0), B(0), A(1), B(1), …. With two
  entries per m, A(m − i) sits 2i places from the end while A(m) is being
  computed, and so does B(m − i) once A(m) has been appended, so the same
  slice `L[2*d::2*d]` serves both passes of `for K in-2,-3`.
- `L` starts with A and B for m = 0, 1, 2 (1, 0, 0 each) and n = −6, so
  the first pass makes m = 3 and prints a(3).

**Notes**

- Writing the second product as A·(1 − x³)⁶ and printing
  A(m) − Σⱼ (−1)ʲC(6, j)·A(m − 3j) takes more bytes than the second list;
  for [A002043](../A002043/) (three terms) it is the other way round.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 34 terms (n = 3 to 36); the bar is the whole b-file in
  60 s, which takes a fraction of a second. The program prints a thousand
  terms in about 1.5 s, and its terms up to n = 150 agree with a direct
  expansion of the two products.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 125 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002044), CC BY-SA 4.0.
