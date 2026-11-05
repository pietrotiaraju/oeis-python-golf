# OEIS Python Golf

Shortest known Python programs that generate sequences from the
[OEIS](https://oeis.org/). Every record is run and checked against the
sequence's OEIS b-file, locally and in CI.

## Records

Size in bytes, shortest in bold. The last column is how many terms every
program for that sequence must reproduce within its time limit. Click a
sequence for the code and how it works.

<!-- records:start -->
| Sequence | Name | Python 3 | Python 3 + sympy | Terms checked |
|---|---|---|---|---|
| [A000001](seq/A000001/) | Number of groups of order n. | **256** | — | 6 |
| [A000002](seq/A000002/) | Kolakoski sequence: a(n) is length of n-th run; a(1) = 1; sequence… | **53** | — | 10502 |
| [A000003](seq/A000003/) | Number of classes of primitive positive definite binary quadratic… | **147** | — | 300 |
| [A000004](seq/A000004/) | The zero sequence. | **16** | — | 1001 |
| [A000005](seq/A000005/) | d(n) (also called tau(n) or sigma_0(n)), the number of divisors of n. | **52** | — | 10000 |
| [A000006](seq/A000006/) | Integer part of square root of n-th prime. | **56** | — | 5000 |
| [A000007](seq/A000007/) | The characteristic function of {0}: a(n) = 0^n. | **23** | — | 1001 |
| [A000008](seq/A000008/) | Number of ways of making change for n cents using coins of 1, 2, 5,… | **73** | — | 10001 |
| [A000009](seq/A000009/) | Expansion of Product_{m >= 1} (1 + x^m); number of partitions of n… | **68** | — | 500 |
| [A000010](seq/A000010/) | Euler totient function phi(n): count numbers <= n and prime to n. | 67 | **52** | 500 |
| [A000011](seq/A000011/) | Number of n-bead necklaces (turning over is allowed) where… | **112** | — | 3336 |
| [A000012](seq/A000012/) | The simplest sequence of positive numbers: the all 1's sequence. | **16** | — | 10001 |
| [A000013](seq/A000013/) | Definition (1): Number of n-bead binary necklaces with beads of 2… | **98** | — | 3335 |
| [A000014](seq/A000014/) | Number of series-reduced trees with n nodes. | **167** | — | 1001 |
| [A000015](seq/A000015/) | Smallest prime power >= n. | **83** | — | 10000 |
| [A000016](seq/A000016/) | a(n) is the number of distinct (infinite) output sequences from… | **97** | — | 3335 |
| [A000018](seq/A000018/) | Number of positive integers <= 2^n of form x^2 + 16*y^2. | **101** | — | 24 |
| [A000019](seq/A000019/) | Number of primitive permutation groups of degree n. | **469** | — | 5 |
| [A000020](seq/A000020/) | Number of primitive polynomials of degree n over GF(2) (version 2). | 83 | **66** | 24 |
| [A000021](seq/A000021/) | Number of positive integers <= 2^n of form x^2 + 12 y^2. | **101** | — | 24 |
| [A000022](seq/A000022/) | Number of centered hydrocarbons with n atoms. | **247** | — | 40 |
| [A000023](seq/A000023/) | a(n) is the number of permutations on {1,2,...,n} with an even number… | **40** | — | 251 |
| [A000024](seq/A000024/) | Number of positive integers <= 2^n of form x^2 + 10 y^2. | **101** | — | 24 |
| [A000025](seq/A000025/) | Coefficients of the 3rd-order mock theta function f(q). | **119** | — | 400 |
| [A276805](seq/A276805/) | a(n) = numerator((n^2 + 3*n + 2)/n^3). | **41** | — | 1000 |
| [A300000](seq/A300000/) | The sum of the first n terms of the sequence is the concatenation of… | **65** | — | 1001 |
| [A300001](seq/A300001/) | Side length of the smallest equilateral triangle that can be… | **71** | — | 100 |
| [A300002](seq/A300002/) | Lexicographically earliest sequence of positive integers such that no… | 209 | **152** | 10 |
| [A384128](seq/A384128/) | Number of iterations for the circular absolute first-difference on… | **118** | — | 106 |
| [A386929](seq/A386929/) | a(n) is the least base b in {2,...,10} such that the base-b expansion… | 131 | **124** | 200 |
<!-- records:end -->

## Rules in short

- Print the sequence from its OEIS offset, one term per line, forever.
- CPython 3.12, no flags, no input. Size = file bytes, trailing newline free.
- Plain Python 3 and each "Python 3 + library" are separate categories.
- Correct for every n, with exact arithmetic; hard-coding only with a proof on
  the page.

Full rules and how to send a record: [CONTRIBUTING.md](CONTRIBUTING.md).

## Verify locally

```bash
pip install -r requirements.txt
python tools/verify.py
```

## Why "shortest known"

No record here is proved minimal, and in general none can be:

- A function that returns the length of the shortest program for any output
  cannot exist (the Berry paradox argument behind Kolmogorov complexity).
- Even deciding whether a given program prints a given infinite sequence is
  undecidable (Rice's theorem): a program that prints the sequence but switches
  to 0 once some machine halts prints it exactly when that machine never halts.
- For one specific record of, say, 66 bytes, ruling out every shorter program
  means about 96⁶⁵ ≈ 10¹²⁸ candidates, each needing a proof about its infinite
  output.

So a record stands until someone finds a shorter program.

## Related

- [LODA](https://loda-lang.org/) mines programs for OEIS sequences in its own
  assembly-like language, at a much larger scale and without byte golfing.
- The `%o` lines of each OEIS entry hold readable reference programs.

## License

Programs and tools: [MIT](LICENSE). Sequence names, b-files and other data
come from [The On-Line Encyclopedia of Integer Sequences](https://oeis.org/)
under [CC BY-SA 4.0](https://oeis.org/LICENSE); the pages that quote them are
under CC BY-SA 4.0 too.
