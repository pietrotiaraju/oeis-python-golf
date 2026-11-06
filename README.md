# OEIS Python Golf

Shortest known Python programs that generate sequences from the
[OEIS](https://oeis.org/). Every record is run and checked against the
sequence's OEIS b-file, locally and in CI.

New to golfing these? The [golf tricks](TRICKS.md) page collects the
techniques that come up again and again across the sequence pages, each with a
short example and links to the sequences that use it.

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
| [A000014](seq/A000xxx/A000014/) | Number of series-reduced trees with n nodes. | **165** | 1001 |
| [A000015](seq/A000xxx/A000015/) | Smallest prime power >= n. | **82** | 10000 |
| [A000016](seq/A000xxx/A000016/) | a(n) is the number of distinct (infinite) output sequences from… | **96** | 3335 |
| [A000018](seq/A000xxx/A000018/) | Number of positive integers <= 2^n of form x^2 + 16\*y^2. | **92** | 24 |
| [A000019](seq/A000xxx/A000019/) | Number of primitive permutation groups of degree n. | **468** | 5 |
| [A000020](seq/A000xxx/A000020/) | Number of primitive polynomials of degree n over GF(2) (version 2). | **83** | 24 |
| [A000021](seq/A000xxx/A000021/) | Number of positive integers <= 2^n of form x^2 + 12 y^2. | **92** | 24 |
| [A000022](seq/A000xxx/A000022/) | Number of centered hydrocarbons with n atoms. | **200** | 40 |
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
| [A000036](seq/A000xxx/A000036/) | Let A(n) = #{(i,j): i^2 + j^2 <= n}, V(n) = Pi\*n, P(n) = A(n) - V(n);… | **204** | 50 |
| [A000037](seq/A000xxx/A000037/) | Numbers that are not squares (or, the nonsquares). | **39** | 10000 |
| [A000038](seq/A000xxx/A000038/) | Twice A000007. | **23** | 10001 |
| [A000039](seq/A000xxx/A000039/) | Coefficient of q^(2n) in the series expansion of Ramanujan's mock… | **96** | 200 |
| [A000040](seq/A000xxx/A000040/) | The prime numbers. | **40** | 10000 |
| [A000041](seq/A000xxx/A000041/) | a(n) is the number of partitions of n (the partition numbers). | **79** | 5000 |
| [A000042](seq/A000xxx/A000042/) | Unary representation of natural numbers. | **28** | 1000 |
| [A000043](seq/A000xxx/A000043/) | Mersenne exponents: primes p such that 2^p - 1 is prime. Then 2^p - 1… | **65** | 15 |
| [A000044](seq/A000xxx/A000044/) | Dying rabbits: a(0) = 1; for 1 <= n <= 12, a(n) = Fibonacci(n); for n… | **42** | 1001 |
| [A000045](seq/A000xxx/A000045/) | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1. | **31** | 2001 |
| [A000046](seq/A000xxx/A000046/) | Number of primitive n-bead necklaces (turning over is allowed) where… | **132** | 1001 |
| [A000047](seq/A000xxx/A000047/) | Number of integers <= 2^n of form x^2 - 2y^2. | **95** | 25 |
| [A000048](seq/A000xxx/A000048/) | Number of n-bead necklaces with beads of 2 colors and primitive… | **92** | 3321 |
| [A000049](seq/A000xxx/A000049/) | Number of positive integers <= 2^n of the form 3\*x^2 + 4\*y^2. | **93** | 24 |
| [A000050](seq/A000xxx/A000050/) | Number of positive integers <= 2^n of form x^2 + y^2. | **87** | 25 |
| [A000051](seq/A000xxx/A000051/) | a(n) = 2^n + 1. | **26** | 101 |
| [A000052](seq/A000xxx/A000052/) | 1-digit numbers arranged in alphabetical order, then the 2-digit… | **389** | 10000 |
| [A000053](seq/A000xxx/A000053/) | Local stops on New York City 1 Train (Broadway-7 Avenue Local) subway. | **62** | 29 |
| [A000054](seq/A000xxx/A000054/) | Local stops on New York City A line subway. | **58** | 25 |
| [A000055](seq/A000xxx/A000055/) | Number of trees with n unlabeled nodes. | **137** | 1001 |
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
| [A000066](seq/A000xxx/A000066/) | Smallest number of vertices in trivalent graph with girth (shortest… | **225** | 6 |
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
| [A000083](seq/A000xxx/A000083/) | Number of mixed Husimi trees with n nodes; or polygonal cacti with… | **260** | 501 |
| [A000084](seq/A000xxx/A000084/) | Number of series-parallel networks with n unlabeled edges. Also… | **91** | 1001 |
| [A000085](seq/A000xxx/A000085/) | Number of self-inverse permutations on n letters, also known as… | **40** | 801 |
| [A000086](seq/A000xxx/A000086/) | Number of solutions to x^2 - x + 1 == 0 (mod n). | **56** | 2000 |
| [A000087](seq/A000xxx/A000087/) | Number of unrooted nonseparable planar maps with n edges and a… | **160** | 200 |
| [A000088](seq/A000xxx/A000088/) | Number of simple graphs on n unlabeled nodes. | **169** | 40 |
| [A000089](seq/A000xxx/A000089/) | Number of solutions to x^2 + 1 == 0 (mod n). | **54** | 10000 |
| [A000090](seq/A000xxx/A000090/) | Expansion of e.g.f. exp((-x^3)/3)/(1-x). | **58** | 101 |
| [A000091](seq/A000xxx/A000091/) | Multiplicative with a(2^e) = 2 for k >= 1; a(3) = 2, a(3^e) = 0 for k… | **88** | 2000 |
| [A000092](seq/A000xxx/A000092/) | Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)\*Pi\*n^(3/2),… | **271** | 30 |
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
| [A000103](seq/A000xxx/A000103/) | Number of n-node triangulations of sphere in which every node has… | **425** | 7 |
| [A000104](seq/A000xxx/A000104/) | Number of n-celled free polyominoes without holes. | **285** | 12 |
| [A000105](seq/A000xxx/A000105/) | Number of free polyominoes (or square animals) with n cells. | **209** | 13 |
| [A000106](seq/A000xxx/A000106/) | 2nd power of rooted tree enumerator; number of linear forests of 2… | **111** | 999 |
| [A000107](seq/A000xxx/A000107/) | Number of rooted trees with n nodes and a single labeled node;… | **120** | 1001 |
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
| [A000119](seq/A000xxx/A000119/) | Number of representations of n as a sum of distinct Fibonacci numbers. | **75** | 6766 |
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
| [A000134](seq/A000xxx/A000134/) | Positive zeros of Bessel function of order 0 rounded to nearest… | **92** | 200 |
| [A000135](seq/A000xxx/A000135/) | Number of partitions into non-integral powers. | **211** | 38 |
| [A000136](seq/A000xxx/A000136/) | Number of ways of folding a strip of n labeled stamps. | **145** | 10 |
| [A000137](seq/A000xxx/A000137/) | Series-parallel numbers. | **132** | 1000 |
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
| [A000153](seq/A000xxx/A000153/) | a(n) = n\*a(n-1) + (n-2)\*a(n-2), with a(0) = 0, a(1) = 1. | **46** | 251 |
| [A000155](seq/A000xxx/A000155/) | Nearest integer to modified Bessel function K\_n(1). | **50** | 201 |
| [A000156](seq/A000xxx/A000156/) | Number of ways of writing n as a sum of 24 squares. | **76** | 45 |
| [A000157](seq/A000xxx/A000157/) | Number of Boolean functions of n variables. | **239** | 6 |
| [A000158](seq/A000xxx/A000158/) | Number of partitions into non-integral powers. | **172** | 35 |
| [A000159](seq/A000xxx/A000159/) | a(n) = A058087(n,n-3). | **77** | 248 |
| [A000160](seq/A000xxx/A000160/) | Number of partitions into non-integral powers. | **188** | 38 |
| [A000161](seq/A000xxx/A000161/) | Number of partitions of n into 2 squares. | **63** | 8000 |
| [A000162](seq/A000xxx/A000162/) | Number of 3-dimensional polyominoes (or polycubes) with n cells. | **273** | 7 |
| [A000163](seq/A000xxx/A000163/) | Series-parallel numbers. | **160** | 160 |
| [A000164](seq/A000xxx/A000164/) | Number of partitions of n into 3 squares (allowing part zero). | **79** | 800 |
| [A000165](seq/A000xxx/A000165/) | Double factorial of even numbers: (2n)!! = 2^n\*n!. | **33** | 404 |
| [A000166](seq/A000xxx/A000166/) | Subfactorial or rencontres numbers, or derangements: number of… | **33** | 451 |
| [A000167](seq/A000xxx/A000167/) | Nearest integer to modified Bessel function K\_n(2). | **69** | 201 |
| [A000168](seq/A000xxx/A000168/) | a(n) = 2\*3^n\*(2\*n)!/(n!\*(n+2)!). | **43** | 926 |
| [A000169](seq/A000xxx/A000169/) | Number of labeled rooted trees with n nodes: n^(n-1). | **29** | 100 |
| [A000170](seq/A000xxx/A000170/) | Number of ways of placing n nonattacking queens on an n X n board. | **122** | 13 |
| [A000171](seq/A000xxx/A000171/) | Number of self-complementary graphs with n nodes. | **146** | 65 |
| [A000172](seq/A000xxx/A000172/) | The Franel number a(n) = Sum\_{k = 0..n} binomial(n,k)^3. | **68** | 1001 |
| [A000173](seq/A000xxx/A000173/) | Unitary-sociable numbers (smallest member of each cycle). | **135** | 3 |
| [A000174](seq/A000xxx/A000174/) | Number of partitions of n into 5 squares. | **89** | 1000 |
| [A000175](seq/A000xxx/A000175/) | Related to zeros of Bessel function. | **119** | 100 |
| [A000176](seq/A000xxx/A000176/) | Generalized tangent numbers d\_(n,2). | **126** | 4500 |
| [A000177](seq/A000xxx/A000177/) | Number of partitions of n into 6 squares. | **94** | 200 |
| [A000178](seq/A000xxx/A000178/) | Superfactorials: product of first n factorials. | **38** | 47 |
| [A000179](seq/A000xxx/A000179/) | Ménage numbers: a(0) = 1, a(1) = -1, and for n >= 2, a(n) = number of… | **60** | 451 |
| [A000180](seq/A000xxx/A000180/) | Expansion of E.g.f. exp(-x)/(1-3x). | **33** | 101 |
| [A000181](seq/A000xxx/A000181/) | a(n) = A058087(n,n-4). | **89** | 247 |
| [A000182](seq/A000xxx/A000182/) | Tangent (or "Zag") numbers: e.g.f. tan(x), also (up to signs) e.g.f.… | **66** | 243 |
| [A000183](seq/A000xxx/A000183/) | Number of discordant permutations of length n. | **98** | 11 |
| [A000184](seq/A000xxx/A000184/) | Number of genus 0 rooted maps with 3 faces with n vertices. | **48** | 499 |
| [A000185](seq/A000xxx/A000185/) | a(n) = A058087(n,n-5). | **90** | 246 |
| [A000186](seq/A000xxx/A000186/) | Number of 3 X n Latin rectangles in which the first row is in order. | **77** | 208 |
| [A000187](seq/A000xxx/A000187/) | Generalized Euler numbers, c(5,n). | **87** | 251 |
| [A000188](seq/A000xxx/A000188/) | (1) Number of solutions to x^2 == 0 (mod n). (2) Also square root of… | **52** | 10000 |
| [A000189](seq/A000xxx/A000189/) | Number of solutions to x^3 == 0 (mod n). | **53** | 10000 |
| [A000190](seq/A000xxx/A000190/) | Number of solutions to x^4 == 0 (mod n). | **53** | 10000 |
| [A000191](seq/A000xxx/A000191/) | Generalized tangent numbers d(3, n). | **79** | 251 |
| [A000192](seq/A000xxx/A000192/) | Generalized Euler numbers c(6,n). | **88** | 251 |
| [A000193](seq/A000xxx/A000193/) | Nearest integer to log n. | **97** | 10000 |
| [A000194](seq/A000xxx/A000194/) | n appears 2n times, for n >= 1; also nearest integer to square root… | **37** | 1001 |
| [A000195](seq/A000xxx/A000195/) | a(n) = floor(log(n)). | **63** | 1200 |
| [A000196](seq/A000xxx/A000196/) | Integer part of square root of n. Or, number of positive squares <=… | **38** | 10001 |
| [A000197](seq/A000xxx/A000197/) | a(n) = (n!)!. | **54** | 6 |
| [A000198](seq/A000xxx/A000198/) | Largest order of automorphism group of a tournament with n nodes. | **84** | 1000 |
| [A000199](seq/A000xxx/A000199/) | Coefficient of q^(2n-1) in the series expansion of Ramanujan's mock… | **106** | 500 |
| [A000200](seq/A000xxx/A000200/) | Number of bicentered hydrocarbons with n atoms. | **163** | 50 |
| [A000201](seq/A000xxx/A000201/) | Lower Wythoff sequence (a Beatty sequence): a(n) = floor(n\*phi),… | **42** | 10000 |
| [A000202](seq/A000xxx/A000202/) | a(8i+j) = 13i + a(j), where 1<=j<=8. | **29** | 10000 |
| [A000203](seq/A000xxx/A000203/) | a(n) = sigma(n), the sum of the divisors of n. Also called sigma\_1(n). | **56** | 15000 |
| [A000204](seq/A000xxx/A000204/) | Lucas numbers (beginning with 1): L(n) = L(n-1) + L(n-2) with L(1) =… | **33** | 4780 |
| [A000205](seq/A000xxx/A000205/) | Number of positive integers <= 2^n of form x^2 + 3 y^2. | **91** | 24 |
| [A000206](seq/A000xxx/A000206/) | Even sequences with period 2n. | **122** | 1001 |
| [A000207](seq/A000xxx/A000207/) | Number of inequivalent ways of dissecting a regular (n+2)-gon into n… | **94** | 200 |
| [A000208](seq/A000xxx/A000208/) | Number of even sequences with period 2n. | **107** | 1001 |
| [A000209](seq/A000xxx/A000209/) | Nearest integer to tan n. | **125** | 900 |
| [A000210](seq/A000xxx/A000210/) | A Beatty sequence: floor(n\*(e-1)). | **44** | 1000 |
| [A000211](seq/A000xxx/A000211/) | a(n) = a(n-1) + a(n-2) - 2, a(0) = 4, a(1) = 3. | **35** | 501 |
| [A000212](seq/A000xxx/A000212/) | a(n) = floor(n^2/3). | **29** | 5001 |
| [A000213](seq/A000xxx/A000213/) | Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) with… | **39** | 3773 |
| [A000214](seq/A000xxx/A000214/) | Number of equivalence classes of Boolean functions of n variables… | **197** | 4 |
| [A000215](seq/A000xxx/A000215/) | Fermat numbers: a(n) = 2^(2^n) + 1. | **26** | 12 |
| [A000216](seq/A000xxx/A000216/) | Take sum of squares of digits of previous term, starting with 2. | **44** | 100 |
| [A000217](seq/A000xxx/A000217/) | Triangular numbers: a(n) = binomial(n+1,2) = n\*(n+1)/2 = 0 + 1 + 2 +… | **29** | 30001 |
| [A000218](seq/A000xxx/A000218/) | Take sum of squares of digits of previous term; start with 3. | **49** | 100 |
| [A000219](seq/A000xxx/A000219/) | Number of plane partitions (or planar partitions) of n. | **82** | 6501 |
| [A000220](seq/A000xxx/A000220/) | Number of asymmetric trees with n nodes (also called identity trees). | **143** | 1000 |
| [A000221](seq/A000xxx/A000221/) | Take sum of squares of digits of previous term; start with 5. | **49** | 100 |
| [A000222](seq/A000xxx/A000222/) | a(n) = A058057(n,n-2). | **66** | 151 |
| [A000223](seq/A000xxx/A000223/) | Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)Pi\*n^(3/2),… | **293** | 20 |
| [A000224](seq/A000xxx/A000224/) | Number of squares mod n. | **53** | 10000 |
| [A000225](seq/A000xxx/A000225/) | a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that… | **25** | 1001 |
| [A000226](seq/A000xxx/A000226/) | Number of n-node unlabeled connected graphs with one cycle of length… | **167** | 500 |
| [A000227](seq/A000xxx/A000227/) | Nearest integer to e^n. | **71** | 15 |
| [A000228](seq/A000xxx/A000228/) | Number of hexagonal polyominoes (or hexagonal polyforms, or planar… | **229** | 10 |
| [A000229](seq/A000xxx/A000229/) | a(n) is the least number m such that the n-th prime is the least… | **133** | 15 |
| [A000230](seq/A000xxx/A000230/) | a(0)=2; for n>=1, a(n) = smallest prime p such that there is a gap of… | **71** | 24 |
| [A000231](seq/A000xxx/A000231/) | Number of inequivalent Boolean functions of n variables under action… | **42** | 12 |
| [A000232](seq/A000xxx/A000232/) | Construct a triangle as in A036262. Sequence is one less than the… | **110** | 50 |
| [A000233](seq/A000xxx/A000233/) | Generalized class numbers c\_(n,1). | **115** | 6500 |
| [A000234](seq/A000xxx/A000234/) | Partitions into non-integral powers (see Comments for precise… | **157** | 26 |
| [A000235](seq/A000xxx/A000235/) | Number of n-node rooted trees of height 3. | **113** | 200 |
| [A000236](seq/A000xxx/A000236/) | Maximum m such that there are no two adjacent elements belonging to… | **216** | 4 |
| [A000237](seq/A000xxx/A000237/) | Number of mixed Husimi trees with n nodes; or rooted polygonal cacti… | **165** | 501 |
| [A000238](seq/A000xxx/A000238/) | Number of oriented trees with n nodes. | **119** | 1000 |
| [A000239](seq/A000xxx/A000239/) | One-half of number of permutations of [n] with exactly one run of… | **100** | 40 |
| [A000240](seq/A000xxx/A000240/) | Rencontres numbers: number of permutations of [n] with exactly one… | **36** | 100 |
| [A000241](seq/A000xxx/A000241/) | Crossing number of complete graph with n nodes. | **39** | 15 |
| [A000242](seq/A000xxx/A000242/) | 3rd power of rooted tree enumerator; number of linear forests of 3… | **107** | 198 |
| [A000243](seq/A000xxx/A000243/) | Number of trees with n nodes, 2 of which are labeled. | **124** | 199 |
| [A000244](seq/A000xxx/A000244/) | Powers of 3: a(n) = 3^n. | **24** | 201 |
| [A000245](seq/A000xxx/A000245/) | a(n) = 3\*(2\*n)!/((n+2)!\*(n-1)!). | **45** | 101 |
| [A000246](seq/A000xxx/A000246/) | Number of permutations in the symmetric group S\_n that have odd order. | **35** | 451 |
| [A000247](seq/A000xxx/A000247/) | a(n) = 2^n - n - 2. | **31** | 299 |
| [A000248](seq/A000xxx/A000248/) | Expansion of e.g.f. exp(x\*exp(x)). | **73** | 125 |
| [A000249](seq/A000xxx/A000249/) | Nearest integer to modified Bessel function K\_n(5). | **239** | 300 |
| [A000250](seq/A000xxx/A000250/) | Number of symmetric reflexive relations on n nodes: (1/2)\*A000666. | **137** | 18 |
| [A000251](seq/A000xxx/A000251/) | Number of trees of diameter 6. | **127** | 70 |
| [A000252](seq/A000xxx/A000252/) | Number of invertible 2 X 2 matrices mod n. | **95** | 1000 |
| [A000253](seq/A000xxx/A000253/) | a(n) = 2\*a(n-1) - a(n-2) + a(n-3) + 2^(n-1). | **49** | 1001 |
| [A000254](seq/A000xxx/A000254/) | Unsigned Stirling numbers of first kind, s(n+1,2): a(n+1) =… | **43** | 450 |
| [A000255](seq/A000xxx/A000255/) | a(n) = n\*a(n-1) + (n-1)\*a(n-2), a(0) = 1, a(1) = 1. | **39** | 101 |
| [A000256](seq/A000xxx/A000256/) | Number of simple triangulations of the plane with n nodes. | **92** | 198 |
| [A000257](seq/A000xxx/A000257/) | Number of rooted bicubic maps: a(n) = (8\*n-4)\*a(n-1)/(n+2) for n >=… | **41** | 201 |
| [A000258](seq/A000xxx/A000258/) | Expansion of e.g.f. exp(exp(exp(x)-1)-1). | **84** | 476 |
| [A000259](seq/A000xxx/A000259/) | Number of certain rooted planar maps. | **67** | 350 |
| [A000260](seq/A000xxx/A000260/) | Number of rooted simplicial 3-polytopes with n+3 nodes; or rooted… | **62** | 201 |
| [A000261](seq/A000xxx/A000261/) | a(n) = n\*a(n-1) + (n-3)\*a(n-2), with a(1) = 0, a(2) = 1. | **46** | 102 |
| [A000262](seq/A000xxx/A000262/) | Number of "sets of lists": number of partitions of {1,...,n} into any… | **46** | 445 |
| [A000263](seq/A000xxx/A000263/) | Number of partitions into non-integral powers. | **60** | 36 |
| [A000264](seq/A000xxx/A000264/) | Number of 3-edge-connected rooted cubic maps with 2n nodes and a… | **132** | 120 |
| [A000265](seq/A000xxx/A000265/) | Remove all factors of 2 from n; or largest odd divisor of n; or odd… | **32** | 100000 |
| [A000266](seq/A000xxx/A000266/) | Expansion of e.g.f. exp(-x^2/2) / (1-x). | **48** | 451 |
| [A000267](seq/A000xxx/A000267/) | Integer part of square root of 4n+1. | **37** | 10001 |
| [A000268](seq/A000xxx/A000268/) | E.g.f.: -log(1+log(1+log(1-x))). | **85** | 400 |
| [A000269](seq/A000xxx/A000269/) | Number of trees with n nodes, 3 of which are labeled. | **147** | 198 |
| [A000270](seq/A000xxx/A000270/) | For n >= 2, a(n) = b(n+1)+b(n)+b(n-1), where the b(i) are the ménage… | **58** | 176 |
| [A000271](seq/A000xxx/A000271/) | Sums of ménage numbers. | **53** | 451 |
| [A000272](seq/A000xxx/A000272/) | Number of trees on n labeled nodes: n^(n-2) with a(0)=1. | **36** | 389 |
| [A000273](seq/A000xxx/A000273/) | Number of unlabeled simple digraphs with n nodes. | **133** | 20 |
| [A000274](seq/A000xxx/A000274/) | Number of permutations of length n with 2 consecutive ascending pairs. | **40** | 150 |
| [A000275](seq/A000xxx/A000275/) | Coefficients of a Bessel function (reciprocal of J\_0(z)); also pairs… | **94** | 262 |
| [A000276](seq/A000xxx/A000276/) | Associated Stirling numbers. | **47** | 447 |
| [A000277](seq/A000xxx/A000277/) | 3\*n - 2\*floor(sqrt(4\*n+5)) + 5. | **46** | 1001 |
| [A000278](seq/A000xxx/A000278/) | a(n) = a(n-1) + a(n-2)^2 for n >= 2 with a(0) = 0 and a(1) = 1. | **35** | 26 |
| [A000279](seq/A000xxx/A000279/) | Card matching: coefficients B[n,1] of t in the reduced hit polynomial… | **74** | 300 |
| [A000280](seq/A000xxx/A000280/) | a(n) = a(n-1) + a(n-2)^3. | **36** | 18 |
| [A000281](seq/A000xxx/A000281/) | Expansion of cos(x)/cos(2x). | **75** | 216 |
| [A000282](seq/A000xxx/A000282/) | Finite automata. | **271** | 16 |
| [A000283](seq/A000xxx/A000283/) | a(n) = a(n-1)^2 + a(n-2)^2 for n >= 2 with a(0) = 0 and a(1) = 1. | **35** | 15 |
| [A000284](seq/A000xxx/A000284/) | a(n) = a(n-1)^3 + a(n-2) with a(0)=0, a(1)=1. | **36** | 11 |
| [A000285](seq/A000xxx/A000285/) | a(0) = 1, a(1) = 4, and a(n) = a(n-1) + a(n-2) for n >= 2. | **33** | 501 |
| [A000286](seq/A000xxx/A000286/) | Number of positive integers <= 2^n of form 2 x^2 + 5 y^2. | **80** | 12 |
| [A000287](seq/A000xxx/A000287/) | Number of rooted polyhedral graphs with n edges. | **77** | 995 |
| [A000288](seq/A000xxx/A000288/) | Tetranacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) with… | **39** | 3504 |
| [A000289](seq/A000xxx/A000289/) | A nonlinear recurrence: a(n) = a(n-1)^2 - 3\*a(n-1) + 3 (for n>1). | **32** | 13 |
| [A000290](seq/A000xxx/A000290/) | The squares: a(n) = n^2. | **26** | 10001 |
| [A000291](seq/A000xxx/A000291/) | Number of bipartite partitions of n white objects and 2 black ones. | **99** | 5000 |
| [A000292](seq/A000xxx/A000292/) | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) =… | **34** | 10001 |
| [A000293](seq/A000xxx/A000293/) | a(n) = number of solid (i.e., three-dimensional) partitions of n. | **145** | 16 |
| [A000294](seq/A000xxx/A000294/) | Expansion of g.f. Product\_{k >= 1} (1 - x^k)^(-k\*(k+1)/2). | **85** | 1001 |
| [A000295](seq/A000xxx/A000295/) | Eulerian numbers (Euler's triangle: column k=2 of A008292, column k=1… | **30** | 501 |
| [A000296](seq/A000xxx/A000296/) | Set partitions without singletons: number of partitions of an n-set… | **56** | 576 |
| [A000297](seq/A000xxx/A000297/) | a(n) = (n+1)\*(n+3)\*(n+8)/6. | **39** | 1002 |
| [A000298](seq/A000xxx/A000298/) | Number of partitions into non-integral powers. | **177** | 22 |
| [A000299](seq/A000xxx/A000299/) | Number of n-node rooted trees of height 4. | **121** | 1000 |
| [A000300](seq/A000xxx/A000300/) | 4th power of rooted tree enumerator: linear forests of 4 rooted trees. | **107** | 497 |
| [A000301](seq/A000xxx/A000301/) | a(n) = a(n-1)\*a(n-2) with a(0) = 1, a(1) = 2; also a(n) =… | **32** | 19 |
| [A000302](seq/A000xxx/A000302/) | Powers of 4: a(n) = 4^n. | **24** | 101 |
| [A000303](seq/A000xxx/A000303/) | Number of permutations of [n] in which the longest increasing run has… | **81** | 464 |
| [A000304](seq/A000xxx/A000304/) | a(n) = a(n-1)\*a(n-2). | **33** | 17 |
| [A000305](seq/A000xxx/A000305/) | Number of certain rooted planar maps. | **91** | 200 |
| [A000306](seq/A000xxx/A000306/) | Number of trees of diameter 8. | **178** | 2500 |
| [A000307](seq/A000xxx/A000307/) | Number of 4-level labeled rooted trees with n leaves. | **85** | 441 |
| [A000308](seq/A000xxx/A000308/) | a(n) = a(n-1)\*a(n-2)\*a(n-3) with a(1)=1, a(2)=2 and a(3)=3. | **43** | 15 |
| [A000309](seq/A000xxx/A000309/) | Number of rooted planar bridgeless cubic maps with 2n nodes. | **55** | 101 |
| [A000310](seq/A000xxx/A000310/) | Coefficients of iterated exponentials. | **85** | 100 |
| [A000311](seq/A000xxx/A000311/) | Schroeder's fourth problem; also series-reduced rooted trees with n… | **81** | 376 |
| [A000312](seq/A000xxx/A000312/) | a(n) = n^n; number of labeled mappings from n points to themselves… | **27** | 386 |
| [A000313](seq/A000xxx/A000313/) | Number of permutations of length n with 3 consecutive ascending pairs. | **43** | 450 |
| [A000314](seq/A000xxx/A000314/) | Number of mixed Husimi trees with n nodes; or labeled polygonal cacti… | **107** | 101 |
| [A000315](seq/A000xxx/A000315/) | Number of reduced Latin squares of order n; also number of labeled… | **140** | 6 |
| [A000316](seq/A000xxx/A000316/) | Two decks each have n kinds of cards, 2 of each kind. The first deck… | **56** | 101 |
| [A000317](seq/A000xxx/A000317/) | a(n+1) = a(n)^2 - a(n)\*a(n-1) + a(n-1)^2. | **41** | 14 |
| [A000318](seq/A000xxx/A000318/) | Generalized tangent numbers d(4,n). | **73** | 100 |
| [A000319](seq/A000xxx/A000319/) | a(n) = floor(b(n)), where b(n) = tan(b(n-1)), b(0)=1. | **254** | 10001 |
| [A000320](seq/A000xxx/A000320/) | Generalized tangent numbers d(5,n). | **89** | 189 |
| [A000321](seq/A000xxx/A000321/) | H\_n(-1/2), where H\_n(x) is Hermite polynomial of degree n. | **43** | 733 |
| [A000322](seq/A000xxx/A000322/) | Pentanacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) + a(n-5)… | **39** | 3403 |
| [A000323](seq/A000xxx/A000323/) | Let A(n) = #{(i,j): i^2 + j^2 <= n}, V(n) = Pi\*n, P(n) = A(n) - V(n);… | **177** | 45 |
| [A000324](seq/A000xxx/A000324/) | A nonlinear recurrence: a(0) = 1, a(1) = 5, a(n) = a(n-1)^2 -… | **32** | 13 |
| [A000325](seq/A000xxx/A000325/) | a(n) = 2^n - n. | **29** | 201 |
| [A000326](seq/A000xxx/A000326/) | Pentagonal numbers: a(n) = n\*(3\*n-1)/2. | **30** | 10001 |
| [A000327](seq/A000xxx/A000327/) | Number of partitions into non-integral powers. | **101** | 40 |
| [A000328](seq/A000xxx/A000328/) | Number of points of norm <= n^2 in square lattice. | **77** | 400 |
| [A000329](seq/A000xxx/A000329/) | Nearest integer to b(n), where b(n) = tan(b(n-1)), b(0) = 1. | **267** | 10001 |
| [A000330](seq/A000xxx/A000330/) | Square pyramidal numbers: a(n) = 0^2 + 1^2 + 2^2 + ... + n^2 =… | **33** | 10001 |
| [A000331](seq/A000xxx/A000331/) | Related to zeros of Bessel function. | **151** | 192 |
| [A000332](seq/A000xxx/A000332/) | Binomial coefficient binomial(n,4) = n\*(n-1)\*(n-2)\*(n-3)/24. | **38** | 1003 |
| [A000333](seq/A000xxx/A000333/) | Number of partitions into non-integral powers. | **154** | 15 |
| [A000334](seq/A000xxx/A000334/) | Number of 4-dimensional partitions of n. | **158** | 11 |
| [A000335](seq/A000xxx/A000335/) | Euler transform of A000292. | **96** | 500 |
| [A000336](seq/A000xxx/A000336/) | a(n) = a(n-1)\*a(n-2)\*a(n-3)\*a(n-4); for n < 5, a(n) = n. | **53** | 15 |
| [A000337](seq/A000xxx/A000337/) | a(n) = (n-1)\*2^n + 1. | **33** | 1001 |
| [A000338](seq/A000xxx/A000338/) | Expansion of x^3\*(5-2\*x)\*(1-x^3)/(1-x)^4. | **38** | 998 |
| [A000339](seq/A000xxx/A000339/) | Number of partitions into non-integral powers. | **62** | 560 |
| [A000340](seq/A000xxx/A000340/) | a(0)=1, a(n) = 3\*a(n-1) + n + 1. | **34** | 1001 |
| [A000341](seq/A000xxx/A000341/) | Number of ways to pair up {1..2n} so sum of each pair is prime. | **144** | 11 |
| [A000342](seq/A000xxx/A000342/) | Number of n-node rooted trees of height 5. | **122** | 200 |
| [A000343](seq/A000xxx/A000343/) | 5th power of rooted tree enumerator; number of linear forests of 5… | **107** | 746 |
| [A000344](seq/A000xxx/A000344/) | a(n) = 5\*binomial(2n, n-2)/(n+3). | **52** | 299 |
| [A000345](seq/A000xxx/A000345/) | Number of partitions into non-integral powers. | **141** | 15 |
| [A000346](seq/A000xxx/A000346/) | a(n) = 2^(2\*n+1) - binomial(2\*n+1, n+1). | **49** | 501 |
| [A000347](seq/A000xxx/A000347/) | Number of partitions into non-integral powers. | **166** | 17 |
| [A000348](seq/A000xxx/A000348/) | Number of ways to pair up {1^2, 2^2, ..., (2n)^2 } so sum of each… | **157** | 12 |
| [A000349](seq/A000xxx/A000349/) | One-half the number of permutations of length n with exactly 2 rising… | **129** | 201 |
| [A000350](seq/A000xxx/A000350/) | Numbers m such that Fibonacci(m) ends with m. | **62** | 370 |
| [A000351](seq/A000xxx/A000351/) | Powers of 5: a(n) = 5^n. | **24** | 101 |
| [A000352](seq/A000xxx/A000352/) | One half of the number of permutations of [n] such that the… | **42** | 397 |
| [A000353](seq/A000xxx/A000353/) | Primes p == 7, 19, 23 (mod 40) such that (p-1)/2 is also prime. | **74** | 230 |
| [A000354](seq/A000xxx/A000354/) | Expansion of e.g.f. exp(-x)/(1-2\*x). | **36** | 101 |
| [A000355](seq/A000xxx/A000355/) | Primes p == 3, 9, 11 (mod 20) such that 2p+1 is also prime. | **77** | 230 |
| [A000356](seq/A000xxx/A000356/) | Number of rooted cubic maps with 2n nodes and a distinguished… | **53** | 800 |
| [A000357](seq/A000xxx/A000357/) | Number of 5-level labeled rooted trees with n leaves. | **85** | 401 |
| [A000358](seq/A000xxx/A000358/) | Number of binary necklaces of length n with no subsequence 00,… | **99** | 1000 |
| [A000359](seq/A000xxx/A000359/) | Coefficients of iterated exponentials. | **85** | 100 |
| [A000360](seq/A000xxx/A000360/) | Distribution of nonempty triangles inside a fractal rep-4-tile. | **47** | 10001 |
| [A000361](seq/A000xxx/A000361/) | Binary encodings of the successive columns of the Gosper-Lafitte… | **81** | 10000 |
| [A000362](seq/A000xxx/A000362/) | Generalized class numbers c\_(n,2). | **129** | 4700 |
| [A000363](seq/A000xxx/A000363/) | Number of permutations of [n] with exactly 2 increasing runs of… | **49** | 997 |
| [A000364](seq/A000xxx/A000364/) | Euler (or secant or "Zig") numbers: e.g.f. (even powers only) sec(x)… | **65** | 243 |
| [A000365](seq/A000xxx/A000365/) | Number of genus 0 rooted planar maps with 4 faces and n vertices. | **78** | 198 |
| [A000366](seq/A000xxx/A000366/) | Genocchi numbers of second kind (A005439) divided by 2^(n-1). | **81** | 100 |
| [A000367](seq/A000xxx/A000367/) | Numerators of Bernoulli numbers B\_2n. | **138** | 250 |
| [A000368](seq/A000xxx/A000368/) | Number of connected graphs with one cycle of length 4. | **169** | 1997 |
| [A000369](seq/A000xxx/A000369/) | Triangle of numbers related to triangle A049213; generalization of… | **76** | 1275 |
| [A000370](seq/A000xxx/A000370/) | Number of NPN-equivalence classes of Boolean functions of n or fewer… | **235** | 7 |
| [A000371](seq/A000xxx/A000371/) | a(n) = Sum\_{k=0..n} (-1)^(n-k)\*binomial(n,k)\*2^(2^k). | **59** | 9 |
| [A000372](seq/A000xxx/A000372/) | Dedekind numbers or Dedekind's problem: number of monotone Boolean… | **72** | 7 |
| [A000373](seq/A000xxx/A000373/) | Conjectured dimension of a module associated with the free… | **182** | 200 |
| [A000374](seq/A000xxx/A000374/) | Number of cycles (mod n) under doubling map. | **75** | 480 |
| [A000375](seq/A000xxx/A000375/) | Topswops (1): start by shuffling n cards labeled 1..n. If top card is… | **125** | 10 |
| [A000376](seq/A000xxx/A000376/) | Topswops (2): start by shuffling n cards labeled 1..n. If the top… | **101** | 12 |
| [A000377](seq/A000xxx/A000377/) | Expansion of f(-q^3) \* f(-q^8) \* chi(-q^12) / chi(-q) in powers of q… | **73** | 10001 |
| [A000378](seq/A000xxx/A000378/) | Sums of three squares: numbers of the form x^2 + y^2 + z^2. | **52** | 10000 |
| [A000379](seq/A000xxx/A000379/) | Numbers where total number of 1-bits in the exponents of their prime… | **88** | 8000 |
| [A000380](seq/A000xxx/A000380/) | Number of permutations of an n-sequence discordant with three given… | **116** | 6 |
| [A000382](seq/A000xxx/A000382/) | Restricted permutations. | **49** | 997 |
| [A000383](seq/A000xxx/A000383/) | Hexanacci numbers with a(0) = ... = a(5) = 1. | **39** | 3359 |
| [A000384](seq/A000xxx/A000384/) | Hexagonal numbers: a(n) = n\*(2\*n-1). | **29** | 10001 |
| [A000385](seq/A000xxx/A000385/) | Convolution of A000203 with itself. | **75** | 10000 |
| [A000386](seq/A000xxx/A000386/) | a(n) = A058057(n,n-3). | **107** | 451 |
| [A000387](seq/A000xxx/A000387/) | Rencontres numbers: number of permutations of [n] with exactly two… | **41** | 201 |
| [A000388](seq/A000xxx/A000388/) | Number of permutations of an n-sequence discordant with three given… | **116** | 5 |
| [A000389](seq/A000xxx/A000389/) | Binomial coefficients C(n,5). | **44** | 1001 |
| [A000390](seq/A000xxx/A000390/) | Number of 5-dimensional partitions of n. | **161** | 10 |
| [A000391](seq/A000xxx/A000391/) | Euler transform of A000332. | **103** | 500 |
| [A000392](seq/A000xxx/A000392/) | Stirling numbers of second kind S(n,3). | **40** | 201 |
| [A000393](seq/A000xxx/A000393/) | Number of n-node rooted trees of height 6. | **124** | 200 |
| [A000394](seq/A000xxx/A000394/) | Numbers of form x^2 + y^2 + 7z^2. | **75** | 60 |
| [A000395](seq/A000xxx/A000395/) | 6th power of rooted tree enumerator; number of linear forests of 6… | **107** | 995 |
| [A000396](seq/A000xxx/A000396/) | Perfect numbers k: k is equal to the sum of the proper divisors of k. | **62** | 4 |
| [A000397](seq/A000xxx/A000397/) | Number of partitions into non-integral powers. | **137** | 13 |
| [A000398](seq/A000xxx/A000398/) | Numbers of form x^2 + 2y^2 + 2yz + 4z^2. | **79** | 450 |
| [A000399](seq/A000xxx/A000399/) | Unsigned Stirling numbers of first kind s(n,3). | **54** | 410 |
| [A000400](seq/A000xxx/A000400/) | Powers of 6: a(n) = 6^n. | **24** | 101 |
| [A000401](seq/A000xxx/A000401/) | Numbers of form x^2 + y^2 + 2\*z^2. | **61** | 1000 |
| [A000402](seq/A000xxx/A000402/) | Number of permutations of [n] in which the longest increasing run has… | **166** | 452 |
| [A000404](seq/A000xxx/A000404/) | Numbers that are the sum of 2 nonzero squares. | **91** | 10000 |
| [A000405](seq/A000xxx/A000405/) | Number of 6-level labeled rooted trees with n leaves. | **85** | 151 |
| [A000406](seq/A000xxx/A000406/) | Coefficients of iterated exponentials. | **85** | 100 |
| [A000407](seq/A000xxx/A000407/) | a(n) = (2\*n+1)! / n!. | **33** | 101 |
| [A000408](seq/A000xxx/A000408/) | Numbers that are the sum of three nonzero squares. | **117** | 10000 |
| [A000409](seq/A000xxx/A000409/) | Singular n X n (0,1)-matrices: the number of n X n (0,1)-matrices… | **144** | 14 |
| [A000414](seq/A000xxx/A000414/) | Numbers that are the sum of 4 nonzero squares. | **143** | 10000 |
| [A000415](seq/A000xxx/A000415/) | Numbers that are the sum of 2 but no fewer nonzero squares. | **106** | 10000 |
| [A000419](seq/A000xxx/A000419/) | Numbers that are the sum of 3 but no fewer nonzero squares. | **147** | 10000 |
| [A000420](seq/A000xxx/A000420/) | Powers of 7: a(n) = 7^n. | **24** | 101 |
| [A000422](seq/A000xxx/A000422/) | Concatenation of numbers from n down to 1. | **40** | 150 |
| [A000423](seq/A000xxx/A000423/) | a(n) is smallest number > a(n-1) of form a(i)\*a(j), i < j < n. | **79** | 49 |
| [A000430](seq/A000xxx/A000430/) | Primes and squares of primes. | **74** | 1000 |
| [A000431](seq/A000xxx/A000431/) | Expansion of 2\*x^3/((1-2\*x)^2\*(1-4\*x)). | **42** | 201 |
| [A000433](seq/A000xxx/A000433/) | n written in base where place values are positive cubes. | **114** | 10001 |
| [A000434](seq/A000xxx/A000434/) | Number of permutations of [n] in which the longest increasing run has… | **166** | 450 |
| [A000435](seq/A000xxx/A000435/) | Normalized total height of all nodes in all rooted trees with n… | **75** | 1000 |
| [A000441](seq/A000xxx/A000441/) | a(n) = Sum\_{k=1..n-1} k\*sigma(k)\*sigma(n-k). | **82** | 1000 |
| [A000442](seq/A000xxx/A000442/) | a(n) = (n!)^3. | **36** | 101 |
| [A000443](seq/A000xxx/A000443/) | Numbers that are the sum of 2 squares in exactly 3 ways. | **118** | 10000 |
| [A000447](seq/A000xxx/A000447/) | a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2\*n-1)^2 = n\*(4\*n^2 - 1)/3. | **35** | 1001 |
| [A000449](seq/A000xxx/A000449/) | Rencontres numbers: number of permutations of [n] with exactly 3… | **59** | 98 |
| [A000450](seq/A000xxx/A000450/) | a(n) = A058057(n,n-4). | **114** | 447 |
| [A000453](seq/A000xxx/A000453/) | Stirling numbers of the second kind, S(n,4). | **50** | 197 |
| [A000454](seq/A000xxx/A000454/) | Unsigned Stirling numbers of first kind s(n,4). | **68** | 97 |
| [A000455](seq/A000xxx/A000455/) | Digits of powers of 2. | **39** | 10000 |
| [A000456](seq/A000xxx/A000456/) | Number of permutations of [n] in which the longest increasing run has… | **166** | 450 |
| [A000459](seq/A000xxx/A000459/) | Number of multiset permutations of {1, 1, 2, 2, ..., n, n} with no… | **66** | 101 |
| [A000460](seq/A000xxx/A000460/) | Eulerian numbers (Euler's triangle: column k=3 of A008292, column k=2… | **50** | 998 |
| [A000461](seq/A000xxx/A000461/) | Concatenate n n times. | **32** | 333 |
| [A000463](seq/A000xxx/A000463/) | n followed by n^2. | **35** | 10000 |
| [A000466](seq/A000xxx/A000466/) | a(n) = 4\*n^2 - 1. | **31** | 901 |
| [A000468](seq/A000xxx/A000468/) | Powers of ten written in base 8. | **30** | 101 |
| [A000472](seq/A000xxx/A000472/) | a(n) = a(n-1)^2 + (a(n-2) + 1)\*(a(n-1) - a(n-2)^2). | **41** | 14 |
| [A000475](seq/A000xxx/A000475/) | Rencontres numbers: number of permutations of [n] with exactly 4… | **69** | 97 |
| [A000477](seq/A000xxx/A000477/) | a(n) = Sum\_{k=1..n-1} k^2\*sigma(k)\*sigma(n-k). | **82** | 10000 |
| [A000478](seq/A000xxx/A000478/) | Number of ways of placing n labeled balls into 3 indistinguishable… | **61** | 195 |
| [A000481](seq/A000xxx/A000481/) | Stirling numbers of the second kind, S(n,5). | **57** | 196 |
| [A000497](seq/A000xxx/A000497/) | S2(j,2j+2) where S2(n,k) is a 2-associated Stirling number of the… | **64** | 100 |
| [A000796](seq/A000xxx/A000796/) | Decimal expansion of Pi (or digits of Pi). | **85** | 20000 |
| [A005150](seq/A005xxx/A005150/) | Look and Say sequence: describe the previous term! (method A -… | **82** | 25 |
| [A034851](seq/A034xxx/A034851/) | Rows of Losanitsch's triangle T(n, k), n >= 0, 0 <= k <= n. | **92** | 5050 |
| [A035513](seq/A035xxx/A035513/) | Wythoff array read by falling antidiagonals. | **89** | 5151 |
| [A139569](seq/A139xxx/A139569/) | A triangle of coefficients of a Chebyshev T(x,n) polynomials to make… | **86** | 66 |
| [A276805](seq/A276xxx/A276805/) | a(n) = numerator((n^2 + 3\*n + 2)/n^3). | **41** | 1000 |
| [A300000](seq/A300xxx/A300000/) | The sum of the first n terms of the sequence is the concatenation of… | **65** | 1001 |
| [A300001](seq/A300xxx/A300001/) | Side length of the smallest equilateral triangle that can be… | **71** | 100 |
| [A300002](seq/A300xxx/A300002/) | Lexicographically earliest sequence of positive integers such that no… | **208** | 10 |
| [A334244](seq/A334xxx/A334244/) | Decimal representation of n-th iteration of the one-dimensional… | **46** | 1000 |
| [A335332](seq/A335xxx/A335332/) | Decimal representation of n-th iteration of the one-dimensional… | **42** | 22 |
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
