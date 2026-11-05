# OEIS Python Golf

Shortest known Python programs that generate sequences from the
[OEIS](https://oeis.org/). Every record is run and checked against the
sequence's OEIS b-file, locally and in CI.

## Records

Size in bytes, shortest in bold. The last column is how many terms every
program for that sequence must reproduce within its time limit. Click a
sequence for the code and how it works.

<!-- records:start -->

| Sequence | Name | Python 3 | Terms checked |
|---|---|---|---|
| [A000001](seq/A000xxx/A000001/) | Number of groups of order n. | **255** | 6 |
| [A000002](seq/A000xxx/A000002/) | Kolakoski sequence: a(n) is length of n-th run; a(1) = 1; sequence… | **53** | 10502 |
| [A000003](seq/A000xxx/A000003/) | Number of classes of primitive positive definite binary quadratic… | **146** | 300 |
| [A000004](seq/A000xxx/A000004/) | The zero sequence. | **16** | 1001 |
| [A000005](seq/A000xxx/A000005/) | d(n) (also called tau(n) or sigma\_0(n)), the number of divisors of n. | **52** | 10000 |
| [A000006](seq/A000xxx/A000006/) | Integer part of square root of n-th prime. | **56** | 5000 |
| [A000007](seq/A000xxx/A000007/) | The characteristic function of {0}: a(n) = 0^n. | **23** | 1001 |
| [A000008](seq/A000xxx/A000008/) | Number of ways of making change for n cents using coins of 1, 2, 5,… | **67** | 10001 |
| [A000009](seq/A000xxx/A000009/) | Expansion of Product\_{m >= 1} (1 + x^m); number of partitions of n… | **68** | 500 |
| [A000010](seq/A000xxx/A000010/) | Euler totient function phi(n): count numbers <= n and prime to n. | **67** | 500 |
| [A000011](seq/A000xxx/A000011/) | Number of n-bead necklaces (turning over is allowed) where… | **110** | 3336 |
| [A000012](seq/A000xxx/A000012/) | The simplest sequence of positive numbers: the all 1's sequence. | **16** | 10001 |
| [A000013](seq/A000xxx/A000013/) | Definition (1): Number of n-bead binary necklaces with beads of 2… | **96** | 3335 |
| [A000014](seq/A000xxx/A000014/) | Number of series-reduced trees with n nodes. | **167** | 1001 |
| [A000015](seq/A000xxx/A000015/) | Smallest prime power >= n. | **82** | 10000 |
| [A000016](seq/A000xxx/A000016/) | a(n) is the number of distinct (infinite) output sequences from… | **96** | 3335 |
| [A000018](seq/A000xxx/A000018/) | Number of positive integers <= 2^n of form x^2 + 16\*y^2. | **92** | 24 |
| [A000019](seq/A000xxx/A000019/) | Number of primitive permutation groups of degree n. | **468** | 5 |
| [A000020](seq/A000xxx/A000020/) | Number of primitive polynomials of degree n over GF(2) (version 2). | **83** | 24 |
| [A000021](seq/A000xxx/A000021/) | Number of positive integers <= 2^n of form x^2 + 12 y^2. | **92** | 24 |
| [A000022](seq/A000xxx/A000022/) | Number of centered hydrocarbons with n atoms. | **247** | 40 |
| [A000023](seq/A000xxx/A000023/) | a(n) is the number of permutations on {1,2,...,n} with an even number… | **40** | 251 |
| [A000024](seq/A000xxx/A000024/) | Number of positive integers <= 2^n of form x^2 + 10 y^2. | **92** | 24 |
| [A000025](seq/A000xxx/A000025/) | Coefficients of the 3rd-order mock theta function f(q). | **118** | 400 |
| [A000026](seq/A000xxx/A000026/) | Mosaic numbers or multiplicative projection of n: if n = Product… | **95** | 10000 |
| [A000027](seq/A000xxx/A000027/) | The positive integers. Also called the natural numbers, the whole… | **24** | 500000 |
| [A000028](seq/A000xxx/A000028/) | Let k = p\_1^e\_1 p\_2^e\_2 p\_3^e\_3 ... be the prime factorization of n.… | **88** | 10000 |
| [A000029](seq/A000xxx/A000029/) | Number of necklaces with n beads of 2 colors, allowing turning over… | **98** | 301 |
| [A000030](seq/A000xxx/A000030/) | Initial digit of n. | **31** | 10001 |
| [A000031](seq/A000xxx/A000031/) | Number of n-bead necklaces with 2 colors when turning over is not… | **84** | 3334 |
| [A000032](seq/A000xxx/A000032/) | Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1)… | **33** | 4776 |
| [A000033](seq/A000xxx/A000033/) | a(n) = A058087(n,n-2). | **83** | 100 |
| [A000034](seq/A000xxx/A000034/) | Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2). | **21** | 10000 |
| [A000035](seq/A000xxx/A000035/) | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n. | **21** | 1001 |
| [A000036](seq/A000xxx/A000036/) | Let A(n) = #{(i,j): i^2 + j^2 <= n}, V(n) = Pi\*n, P(n) = A(n) - V(n);… | **205** | 50 |
| [A000037](seq/A000xxx/A000037/) | Numbers that are not squares (or, the nonsquares). | **39** | 10000 |
| [A000038](seq/A000xxx/A000038/) | Twice A000007. | **23** | 10001 |
| [A000039](seq/A000xxx/A000039/) | Coefficient of q^(2n) in the series expansion of Ramanujan's mock… | **96** | 200 |
| [A000040](seq/A000xxx/A000040/) | The prime numbers. | **40** | 10000 |
| [A000041](seq/A000xxx/A000041/) | a(n) is the number of partitions of n (the partition numbers). | **79** | 5000 |
| [A000042](seq/A000xxx/A000042/) | Unary representation of natural numbers. | **28** | 1000 |
| [A000043](seq/A000xxx/A000043/) | Mersenne exponents: primes p such that 2^p - 1 is prime. Then 2^p - 1… | **65** | 15 |
| [A000044](seq/A000xxx/A000044/) | Dying rabbits: a(0) = 1; for 1 <= n <= 12, a(n) = Fibonacci(n); for n… | **42** | 1001 |
| [A000045](seq/A000xxx/A000045/) | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1. | **33** | 2001 |
| [A000046](seq/A000xxx/A000046/) | Number of primitive n-bead necklaces (turning over is allowed) where… | **133** | 1001 |
| [A000047](seq/A000xxx/A000047/) | Number of integers <= 2^n of form x^2 - 2y^2. | **95** | 25 |
| [A000048](seq/A000xxx/A000048/) | Number of n-bead necklaces with beads of 2 colors and primitive… | **93** | 3321 |
| [A000049](seq/A000xxx/A000049/) | Number of positive integers <= 2^n of the form 3\*x^2 + 4\*y^2. | **93** | 24 |
| [A000050](seq/A000xxx/A000050/) | Number of positive integers <= 2^n of form x^2 + y^2. | **87** | 25 |
| [A000051](seq/A000xxx/A000051/) | a(n) = 2^n + 1. | **26** | 101 |
| [A000052](seq/A000xxx/A000052/) | 1-digit numbers arranged in alphabetical order, then the 2-digit… | **389** | 10000 |
| [A000055](seq/A000xxx/A000055/) | Number of trees with n unlabeled nodes. | **138** | 1001 |
| [A000056](seq/A000xxx/A000056/) | Order of the group SL(2,Z\_n). | **81** | 1000 |
| [A000057](seq/A000xxx/A000057/) | Primes that divide at least one term in every Fibonacci sequence. | **54** | 100 |
| [A000058](seq/A000xxx/A000058/) | Sylvester's sequence: a(n+1) = a(n)^2 - a(n) + 1, with a(0) = 2. | **28** | 13 |
| [A000059](seq/A000xxx/A000059/) | Numbers k such that (2k)^4 + 1 is prime. | **63** | 120 |
| [A000060](seq/A000xxx/A000060/) | Number of signed trees with n nodes. | **131** | 500 |
| [A000061](seq/A000xxx/A000061/) | Generalized tangent numbers d(n,1). | **158** | 1000 |
| [A000062](seq/A000xxx/A000062/) | A Beatty sequence: a(n) = floor(n/(e-2)). | **53** | 1000 |
| [A000063](seq/A000xxx/A000063/) | Symmetrical dissections of an n-gon. | **91** | 996 |
| [A000064](seq/A000xxx/A000064/) | Partial sums of (unordered) ways of making change for n cents using… | **69** | 1001 |
| [A000065](seq/A000xxx/A000065/) | -1 + number of partitions of n. | **81** | 1001 |
| [A000067](seq/A000xxx/A000067/) | Number of positive integers <= 2^n of form x^2 + 2 y^2. | **89** | 24 |
| [A000068](seq/A000xxx/A000068/) | Numbers k such that k^4 + 1 is prime. | **60** | 120 |
| [A000069](seq/A000xxx/A000069/) | Odious numbers: numbers with an odd number of 1's in their binary… | **41** | 10001 |
| [A000070](seq/A000xxx/A000070/) | a(n) = Sum\_{k=0..n} p(k) where p(k) = number of partitions of k… | **80** | 1001 |
| [A000071](seq/A000xxx/A000071/) | a(n) = Fibonacci(n) - 1. | **32** | 500 |
| [A000072](seq/A000xxx/A000072/) | Number of positive integers <= 2^n of form x^2 + 4 y^2. | **91** | 25 |
| [A000073](seq/A000xxx/A000073/) | Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) for n >= 3 with… | **41** | 3001 |
| [A000074](seq/A000xxx/A000074/) | Number of odd integers <= 2^n of form x^2 + y^2. | **90** | 25 |
| [A000075](seq/A000xxx/A000075/) | Number of positive integers <= 2^n of form 2\*x^2 + 3\*y^2. | **93** | 24 |
| [A000076](seq/A000xxx/A000076/) | Number of integers <= 2^n of form 4 x^2 + 4 x y + 5 y^2. | **97** | 24 |
| [A000077](seq/A000xxx/A000077/) | Number of positive integers <= 2^n of form x^2 + 6 y^2. | **91** | 24 |
| [A000078](seq/A000xxx/A000078/) | Tetranacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) for n >=… | **41** | 3506 |
| [A000079](seq/A000xxx/A000079/) | Powers of 2: a(n) = 2^n. | **24** | 1001 |
| [A000080](seq/A000xxx/A000080/) | Number of nonisomorphic minimal triangle graphs. | **339** | 6 |
| [A000081](seq/A000xxx/A000081/) | Number of unlabeled rooted trees with n nodes (or connected functions… | **87** | 1001 |
| [A000082](seq/A000xxx/A000082/) | a(n) = n^2\*Product\_{p\|n} (1 + 1/p). | **75** | 1000 |
| [A000083](seq/A000xxx/A000083/) | Number of mixed Husimi trees with n nodes; or polygonal cacti with… | **262** | 501 |
| [A000084](seq/A000xxx/A000084/) | Number of series-parallel networks with n unlabeled edges. Also… | **91** | 1001 |
| [A000085](seq/A000xxx/A000085/) | Number of self-inverse permutations on n letters, also known as… | **40** | 801 |
| [A000087](seq/A000xxx/A000087/) | Number of unrooted nonseparable planar maps with n edges and a… | **160** | 200 |
| [A000088](seq/A000xxx/A000088/) | Number of simple graphs on n unlabeled nodes. | **172** | 40 |
| [A000089](seq/A000xxx/A000089/) | Number of solutions to x^2 + 1 == 0 (mod n). | **54** | 10000 |
| [A000090](seq/A000xxx/A000090/) | Expansion of e.g.f. exp((-x^3)/3)/(1-x). | **58** | 101 |
| [A000091](seq/A000xxx/A000091/) | Multiplicative with a(2^e) = 2 for k >= 1; a(3) = 2, a(3^e) = 0 for k… | **88** | 2000 |
| [A000092](seq/A000xxx/A000092/) | Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)\*Pi\*n^(3/2),… | **284** | 30 |
| [A000093](seq/A000xxx/A000093/) | a(n) = floor(n^(3/2)). | **41** | 501 |
| [A000094](seq/A000xxx/A000094/) | Number of trees of diameter 4. | **86** | 500 |
| [A000095](seq/A000xxx/A000095/) | Number of fixed points of Gamma\_0 (n) of type i. | **57** | 10000 |
| [A000096](seq/A000xxx/A000096/) | a(n) = n\*(n+3)/2. | **31** | 10001 |
| [A000097](seq/A000xxx/A000097/) | Number of partitions of n if there are two kinds of 1's and two kinds… | **87** | 5000 |
| [A000098](seq/A000xxx/A000098/) | Number of partitions of n if there are two kinds of 1, two kinds of 2… | **87** | 1001 |
| [A000099](seq/A000xxx/A000099/) | Let A(n) = #{(i,j): i^2 + j^2 <= n}, V(n) = Pi\*n, P(n) = A(n) - V(n);… | **177** | 50 |
| [A000100](seq/A000xxx/A000100/) | a(n) is the number of compositions of n in which the maximal part is… | **57** | 201 |
| [A000101](seq/A000xxx/A000101/) | Record gaps between primes (upper end) (compare A002386, which gives… | **67** | 14 |
| [A000102](seq/A000xxx/A000102/) | a(n) = number of compositions of n in which the maximum part size is… | **63** | 201 |
| [A000103](seq/A000xxx/A000103/) | Number of n-node triangulations of sphere in which every node has… | **427** | 7 |
| [A000104](seq/A000xxx/A000104/) | Number of n-celled free polyominoes without holes. | **285** | 12 |
| [A000105](seq/A000xxx/A000105/) | Number of free polyominoes (or square animals) with n cells. | **209** | 13 |
| [A000106](seq/A000xxx/A000106/) | 2nd power of rooted tree enumerator; number of linear forests of 2… | **112** | 999 |
| [A000107](seq/A000xxx/A000107/) | Number of rooted trees with n nodes and a single labeled node;… | **121** | 1001 |
| [A000108](seq/A000xxx/A000108/) | Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!). | **39** | 1001 |
| [A000109](seq/A000xxx/A000109/) | Number of simplicial polyhedra with n vertices; simple planar graphs… | **415** | 8 |
| [A000110](seq/A000xxx/A000110/) | Bell or exponential numbers: number of ways to partition a set of n… | **48** | 501 |
| [A000111](seq/A000xxx/A000111/) | Euler or up/down numbers: e.g.f. sec(x) + tan(x). Also for n >= 2,… | **56** | 486 |
| [A000112](seq/A000xxx/A000112/) | Number of partially ordered sets ("posets") with n unlabeled elements. | **228** | 7 |
| [A000113](seq/A000xxx/A000113/) | Number of transformation groups of order n. | **116** | 10000 |
| [A000114](seq/A000xxx/A000114/) | Number of cusps of principal congruence subgroup Gamma^{hat}(n). | **86** | 9999 |
| [A000115](seq/A000xxx/A000115/) | Denumerants: Expansion of 1/((1-x)\*(1-x^2)\*(1-x^5)). | **34** | 10001 |
| [A000116](seq/A000xxx/A000116/) | Number of even sequences with period 2n (bisection of A000013). | **92** | 1001 |
| [A000117](seq/A000xxx/A000117/) | Number of even sequences with period 2n (bisection of A000011). | **107** | 501 |
| [A000118](seq/A000xxx/A000118/) | Number of ways of writing n as a sum of 4 squares; also theta series… | **67** | 10000 |
| [A000119](seq/A000xxx/A000119/) | Number of representations of n as a sum of distinct Fibonacci numbers. | **77** | 6766 |
| [A000120](seq/A000xxx/A000120/) | Ones-counting sequence: number of 1's in binary expansion of n (or… | **36** | 10001 |
| [A000121](seq/A000xxx/A000121/) | Number of representations of n as a sum of Fibonacci numbers (1 is… | **74** | 6766 |
| [A000122](seq/A000xxx/A000122/) | Expansion of Jacobi theta function theta\_3(x) = Sum\_{m =-oo..oo}… | **40** | 10001 |
| [A000123](seq/A000xxx/A000123/) | Number of binary partitions: number of partitions of 2n into powers… | **40** | 65537 |
| [A000124](seq/A000xxx/A000124/) | Central polygonal numbers (the Lazy Caterer's sequence): n(n+1)/2 +… | **31** | 1001 |
| [A000125](seq/A000xxx/A000125/) | Cake numbers: maximal number of pieces resulting from n planar cuts… | **37** | 1001 |
| [A000126](seq/A000xxx/A000126/) | A nonlinear binomial sum. | **40** | 201 |
| [A000127](seq/A000xxx/A000127/) | Maximal number of regions obtained by joining n points around a… | **41** | 1000 |
| [A000128](seq/A000xxx/A000128/) | A nonlinear binomial sum. | **47** | 201 |
| [A000129](seq/A000xxx/A000129/) | Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2\*a(n-1) + a(n-2). | **35** | 1001 |
| [A000130](seq/A000xxx/A000130/) | One-half the number of permutations of length n with exactly 1 rising… | **88** | 201 |
| [A000131](seq/A000xxx/A000131/) | Number of asymmetrical dissections of n-gon. | **117** | 994 |
| [A000132](seq/A000xxx/A000132/) | Number of ways of writing n as a sum of 5 squares. | **74** | 100 |
| [A000133](seq/A000xxx/A000133/) | Number of Boolean functions of n variables. | **41** | 11 |
| [A000134](seq/A000xxx/A000134/) | Positive zeros of Bessel function of order 0 rounded to nearest… | **93** | 200 |
| [A000136](seq/A000xxx/A000136/) | Number of ways of folding a strip of n labeled stamps. | **145** | 10 |
| [A000137](seq/A000xxx/A000137/) | Series-parallel numbers. | **133** | 1000 |
| [A000138](seq/A000xxx/A000138/) | Expansion of e.g.f. exp(-x^4/4)/(1-x). | **54** | 101 |
| [A000139](seq/A000xxx/A000139/) | a(n) = 2\*(3\*n)! / ((2\*n+1)!\*(n+1)!). | **55** | 201 |
| [A000140](seq/A000xxx/A000140/) | Kendall-Mann numbers: the most common number of inversions in a… | **78** | 400 |
| [A000141](seq/A000xxx/A000141/) | Number of ways of writing n as a sum of 6 squares. | **74** | 100 |
| [A000142](seq/A000xxx/A000142/) | Factorial numbers: n! = 1\*2\*3\*4\*...\*n (order of symmetric group S\_n,… | **31** | 101 |
| [A000143](seq/A000xxx/A000143/) | Number of ways of writing n as a sum of 8 squares. | **74** | 80 |
| [A000144](seq/A000xxx/A000144/) | Number of ways of writing n as a sum of 10 squares. | **76** | 75 |
| [A000145](seq/A000xxx/A000145/) | Number of ways of writing n as a sum of 12 squares. | **76** | 70 |
| [A000146](seq/A000xxx/A000146/) | From von Staudt-Clausen representation of Bernoulli numbers: a(n) =… | **101** | 150 |
| [A000147](seq/A000xxx/A000147/) | Number of trees of diameter 5. | **129** | 1000 |
| [A000148](seq/A000xxx/A000148/) | Number of partitions into non-integral powers. | **102** | 40 |
| [A000149](seq/A000xxx/A000149/) | a(n) = floor(e^n). | **76** | 301 |
| [A000150](seq/A000xxx/A000150/) | Number of dissections of an n-gon, rooted at an exterior edge,… | **61** | 201 |
| [A000151](seq/A000xxx/A000151/) | Number of oriented rooted trees with n nodes. Also rooted trees with… | **88** | 1300 |
| [A000152](seq/A000xxx/A000152/) | Number of ways of writing n as a sum of 16 squares. | **76** | 60 |
| [A000153](seq/A000xxx/A000153/) | a(n) = n\*a(n-1) + (n-2)\*a(n-2), with a(0) = 0, a(1) = 1. | **48** | 251 |
| [A000796](seq/A000xxx/A000796/) | Decimal expansion of Pi (or digits of Pi). | **85** | 20000 |
| [A139569](seq/A139xxx/A139569/) | A triangle of coefficients of a Chebyshev T(x,n) polynomials to make… | **86** | 66 |
| [A276805](seq/A276xxx/A276805/) | a(n) = numerator((n^2 + 3\*n + 2)/n^3). | **41** | 1000 |
| [A300000](seq/A300xxx/A300000/) | The sum of the first n terms of the sequence is the concatenation of… | **65** | 1001 |
| [A300001](seq/A300xxx/A300001/) | Side length of the smallest equilateral triangle that can be… | **71** | 100 |
| [A300002](seq/A300xxx/A300002/) | Lexicographically earliest sequence of positive integers such that no… | **209** | 10 |
| [A334244](seq/A334xxx/A334244/) | Decimal representation of n-th iteration of the one-dimensional… | **46** | 1000 |
| [A384128](seq/A384xxx/A384128/) | Number of iterations for the circular absolute first-difference on… | **118** | 106 |
| [A386929](seq/A386xxx/A386929/) | a(n) is the least base b in {2,...,10} such that the base-b expansion… | **131** | 200 |

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
