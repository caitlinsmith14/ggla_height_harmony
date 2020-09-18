# Alternatives

## The Soft Typology Tool

The simulations within alternative frameworks that are reported here were conducted using the [Soft Typology Tool](https://github.com/charlieohara/softtypologytool), a tool for examining the stability of phonological patterns over time within a generational MaxEnt Harmonic Grammar learning paradigm.

Basic details on the workings of the Soft Typology Tool can be found in section four of [O'Hara (to appear)](https://dornsifecms.usc.edu/assets/sites/837/docs/oharaNELS20.pdf).

## Generating Derivationally Opaque Stepwise and Saltatory Harmony with Constraints

Unlike in the Gestural Harmony Model, featural analyses of harmony assume that height harmony is the result of featural change; specifically, a target takes on one or more features of the harmony trigger. As a result, both stepwise and saltatory patterns are derivationally opaque within these frameworks.

Stepwise (chain-shifting) phonological patterns: /X/ → [Y], /Y/ → [Z]

Saltatory (derived-environment) phonological patterns: /X/ → [Z], /Y/ → [Y], where X is more similar to Y than it is to Z

 Such patterns are difficult, but not impossible, to generate within constraint-based phonological frameworks, including Optimality Theory and Harmonic Grammar. We examine two different constraint sets that are able to capture these derivationally opaque patterns: constraints on feature scales (Gnanadesikan 1997) and \*MAP constraints (Zuraw 2007, White 2013, Hayes & White 2015). In both approaches, capturing opaque harmony patterns require a set of harmony-driving markedness constraints M such that under some weighting, [X] is more marked than [Y], which is more marked than [Z], as well as one of two types of faithfulness constraints.

### Faithfulness Constraint Necessary for Stepwise Patterns

Generating stepwise harmony requires a faithfulness constraint C such that C(X,Z) \< C(X,Y) + C(Y,Z), where C is a function from a mapping (X → Z) to a negative integer or zero:

 |/X/ | C | M |
 |----|---|---|
 | Z  | -1|   |
 |→ Y |   | -1|
 | X  |   | -2|

 |/Y/ | C | M |
 |----|---|---|
 |→ Z |   |   |
 | Y  |   | -1|

Such a constraint is violated more by the /X/ → [Z] mapping than by the /X/ → [Y] or /Y/ → [Z] mappings put together. When it is weighted (significantly) higher than the relevant markedness constraints, it prevents /X/ from repairing all markedness violations (i.e., undergoing harmony) and surfacing as [Z]. However, it does not prevent /Y/ from surfacing as [Z].

#### Stepwise Patterns with Scalar Features

Gnanadesikan (1997) proposes such a constraint C in her theory of feature scales, in which vowel height is represented by a single scalar feature:

IDENT-ADJ[height]: Assign a violation mark for each output segment that has a height feature that differs from its corresponding input segment's height feature by more than one tier.

If IDENT-ADJ is weighted sufficiently above the relevant markedness constraint(s) driving harmony, and no other relevant faithfulness constraints are weighted  highly, stepwise harmony can be modeled.

 | /a/  | IDENT-ADJ | M |
 |------|-----------|---|
 | [i]  |     -1    |   |
 |→ [e] |           | -1|
 | [a]  |           | -2|

|  /e/ | IDENT-ADJ | M |
|------|-----------|---|
|→ [i] |           |   |
| [e]  |           | -1|

#### Stepwise Patterns with \*MAP constraints:

Another example of this type of constraint C comes from the family of \*MAP constraints (Zuraw 2007, White 2013, Hayes & White 2013).

\*MAP(X,Y): Assign a violation mark if a segment X in the input surfaces as Y in the output.

If \*MAP(a,i) is weighted above the relevant markedness constraints, and other relevant \*MAP constraints are weighted low, stepwise harmony is generated.

 | /a/  | \*MAP(a,i)| M |
 |------|-----------|---|
 | [i]  |     -1    |   |
 |→ [e] |           | -1|
 | [a]  |           | -2|

|  /e/ | \*MAP(a,i)| M |
|------|-----------|---|
|→ [i] |           |   |
| [e]  |           | -1|

Both IDENT-ADJ[height] and \*MAP(a,i) generate the stepwise pattern in functionally equivalent ways, as demonstrated by the similarity of the tableau illustrating the evaluations of both constraints.

### Faithfulness Constraint Necessary for Saltatory Patterns

 Generating saltatory harmony requires a faithfulness constraint D such that D(X,Z) \> D(X,Y) + D(Y,Z) and D(Y,Z) \< 0:

 |/X/ |  D | M |
 |----|-----|---|
 |→ Z |     |   |
 | Y  | (-1)| -1|
 | X  |     | -2|

 |/Y/ | D | M |
 |----|---|---|
 | Z  | -1|   |
 |→ Y |   | -1|

 There are two major approaches to generating saltation in a constraint-based framework.

### Overlapping Faithfulness (Scalar Features):

In what we call the overlapping faithfulness approach, there exists a constraint D such that all three mappings (/X/ → [Z], /Y/ → [Z], /X/ → [Y]) violate D. The scalar feature approach introduced above makes use of an overlapping faithfulness constraint that can be used to generate saltatory harmony.

IDENT[height]: Assign a violation mark for each output segment that has a corresponding input segment that has a different vowel height.

 |/a/    | IDENT[height] | M |       |
 |-------|---------------|---|-------|
 |weights|       4       | 3 |Harmony|
 |→ [i]  |       -1      |   |     -4|
 | [e]   |       -1      | -1|     -7|
 | [a]   |               | -2|     -6|

 |/a/   | IDENT[height] | M |  |
 |------|---------------|---|--|
 | [i]  |      -1       |   |-4|
 |→ [e] |               | -1|-3|


### Non-Overlapping Faithfulness (\*MAP Constraints):

In what we call the non-overlapping faithfulness approach, there exists a constraint D violated by either /Y/→[Z] or /X/→[Y], but not /X/→[Z]. The \*MAP constraints introduced above capture saltatory patterns using non-overlapping faithfulness constraints. In the case of saltatory harmony in a three-height vowel system, the relevant constraint is \*MAP(e,i). 

 |/a/| \*MAP(e,i) | M |
 |-----|----------|---|
 |→[i] |          |   |
 | [e] |          | -1|
 | [a] |          | -2|

 |/e/| \*MAP(e,i) | M |
 |----|-----------|---|
 | [i]|     -1    |   |
 |→[e]|           | -1|

\*MAP constraints are quite powerful, and can generate even extreme saltation patterns. In practice, however, this framework is usually assumed to be constrained by biases favoring certain constraint weightings over others. Specifically, \*MAP constraints are usually biased towards weightings consistent with the P-Map (Steriade 2000). For instance, if X is more similar to Y than it is to Z, \*MAP(X,Z) is biased to be higher weighted than \*MAP(X,Y). This bias makes saltatory patterns harder to learn than other patterns, but not impossible.

## Learning Simulations

In order to test the learnability of the stepwise and saltatory patterns within featural, constraint-based phonological frameworks, we ran simulations using the [`SoftTypologyTool`](https://github.com/charlieohara/softtypologytool). The `SoftTypologyTool` is a Python script developed by Charlie O'Hara that performs generational learning within a MaxEnt Harmonic Grammar framework. More information about this learning model and the `SoftTypologyTool` can be found in [O'Hara (to appear)](https://dornsifecms.usc.edu/assets/sites/837/docs/oharaNELS20.pdf).

All simulations were tested against the two opaque harmony patterns also used in our gestural learning simulations:
* Four-tier stepwise height harmony: /a/ → [ɛ], /ɛ/ → [e], /e/ → [i]
* Four-tier saltatory height harmony: /a/ → [e], /ɛ/ → [i], /e/ → [e]

### Overlapping Faithfulness
 
Overlapping faithfulness simulations were run using the following constraints: IDENT[height], IDENT-ADJ, IDENT-PARTIAL, ASSIM, ASSIM-ADJ, ASSIM-PARTIAL. Their violation profiles are as follows. (Note that Gnanadesikan assumes only ternary feature scales; the four-tier height scale requires the additional constraint IDENT-PARTIAL and ASSIM-PARTIAL).

These tableaux can be loaded into the `SoftTypologyTool` using the file `overlappingfaithfulness/overlappingfaithfulness.txt`. 

|/a-i/|IDENT[HEIGHT]|IDENT-ADJ|IDENT-PARTIAL|ASSIM|ASSIM-ADJ|ASSIM-PARTIAL|
|-----|-------------|---------|-------------|-----|---------|-------------|
|[a-i]|             |         |             | -1  |     -1  |      -1     |
|[ɛ-i]|      -1     |         |             | -1  |     -1  |             |
|[e-i]|      -1     |   -1    |             | -1  |         |             |
|[i-i]|      -1     |   -1    |     -1      |     |         |             |

|/ɛ-i/|IDENT[HEIGHT]|IDENT-ADJ|IDENT-PARTIAL|ASSIM|ASSIM-ADJ|ASSIM-PARTIAL|
|-----|-------------|---------|-------------|-----|---------|-------------|
|[a-i]|      -1     |         |             | -1  |     -1  |      -1     |
|[ɛ-i]|             |         |             | -1  |     -1  |             |
|[e-i]|      -1     |         |             | -1  |         |             |
|[i-i]|      -1     |   -1    |             |     |         |             |

|/e-i/|IDENT[HEIGHT]|IDENT-ADJ|IDENT-PARTIAL|ASSIM|ASSIM-ADJ|ASSIM-PARTIAL|
|-----|-------------|---------|-------------|-----|---------|-------------|
|[a-i]|      -1     |    -1   |             | -1  |     -1  |      -1     |
|[ɛ-i]|      -1     |         |             | -1  |     -1  |             |
|[e-i]|             |         |             | -1  |         |             |
|[i-i]|      -1     |         |             |     |         |             |

|/i-i/|IDENT[HEIGHT]|IDENT-ADJ|IDENT-PARTIAL|ASSIM|ASSIM-ADJ|ASSIM-PARTIAL|
|-----|-------------|---------|-------------|-----|---------|-------------|
|[a-i]|           -1|       -1|           -1|   -1|       -1|           -1|
|[ɛ-i]|           -1|       -1|             |   -1|       -1|             |
|[e-i]|           -1|         |             |   -1|         |             |
|[i-i]|             |         |             |     |         |             |

Learners are initialized with harmony-driving markedness constraints (the ASSIM family) weighted at 50 and faithfulness (the IDENT family) at 1. Each learner is exposed to 2000 iterations from the learner, after which that learner is used to train the next generation. After twenty generations, the learned pattern is compared to the target pattern: if the weights are consistent (in HG) with the target pattern, the run is considered stable.

These numbers of iterations and generations were selected so that a) target patterns were learned accurately at the first generation, and b) the difference in learnability between saltatory and stepwise height harmony patterns was not flattened by floor or ceiling effects. Increasing the number of iterations per generation increases stability across the board, while increasing number of generations decreases stability.

Logs of sample simulations (stable and unstable runs for stepwise and saltatory patterns) are available in the `/overlappingfaithfulness` directory above. These include:

* Probability of each target mapping at the end of each generation (in `/overlappingfaithfulness/generation`)
* Probability of each target mapping, within each generation, per iteration (in `/overlappingfaithfulness/iteration`)
* Weight assigned to each constraint, on each iteration (in `/overlappingfaithfulness/weight`)

### Non-Overlapping Faithfulness

Non-overlapping faithfulness simulations were run using the following constraints: \*MAP(a,i), \*MAP(a,e), \*MAP(a,ɛ), \*MAP(e,ɛ), \*MAP(e, i), ASSIM, ASSIM-ADJ, ASSIM-PARTIAL. Their violation profiles are as follows:

|/a-i/|\*MAP(a,i)|\*MAP(a,e)|\*MAP(a,ɛ)|ASSIM|ASSIM-ADJ|ASSIM-PARTIAL|
|-----|----------|----------|----------|-----|---------|-------------|
|[a-i]|          |          |          |   -1|       -1|           -1|
|[ɛ-i]|          |          |        -1|   -1|       -1|             |
|[e-i]|          |        -1|          |   -1|         |             |
|[i-i]|        -1|          |          |     |         |             |

|/ɛ-i/|\*MAP(ɛ,e)|\*MAP(ɛ,i)|\*MAP(a,ɛ)|ASSIM|ASSIM-ADJ|ASSIM-PARTIAL|
|-----|----------|----------|----------|-----|---------|-------------|
|[a-i]|          |          |        -1|   -1|       -1|           -1|
|[ɛ-i]|          |          |          |   -1|       -1|             |
|[e-i]|        -1|          |          |   -1|         |             |
|[i-i]|          |        -1|          |     |         |             |

|/e-i/|\*MAP(e,i)|\*MAP(a,e)|\*MAP(ɛ,e)|ASSIM|ASSIM-ADJ|ASSIM-PARTIAL|
|-----|----------|----------|----------|-----|---------|-------------|
|[a-i]|          |        -1|          |   -1|       -1|           -1|
|[ɛ-i]|          |          |        -1|   -1|       -1|             |
|[e-i]|          |          |          |   -1|         |             |
|[i-i]|        -1|          |          |     |         |             |

|/i-i/|IDENT[HEIGHT]|IDENT-ADJ|IDENT-PARTIAL|ASSIM|ASSIM-ADJ|ASSIM-PARTIAL|
|-----|-------------|---------|-------------|-----|---------|-------------|
|[a-i]|           -1|       -1|           -1|   -1|       -1|           -1|
|[ɛ-i]|           -1|       -1|             |   -1|       -1|             |
|[e-i]|           -1|         |             |   -1|         |             |
|[i-i]|             |         |             |     |         |             |

To approximate the P-Map bias usually assumed when working with these constraints, we initially weighted \*MAP constraints between less similar segments higher than more similar segments. This differs from the model proposed by White (2013), which uses a persistent L2 prior in a batch learner. An L2 prior in a batch learner differs in some ways from a bias via initial weights in an online learner; for further discussion, see [O'Hara (2020)](https://dornsife.usc.edu/assets/sites/837/docs/scilposter20hand.pdf).

We tested two sets of initial constraint weights:

 #### Markedness High: Markedness constraints weighted above all \*MAP constraints

|Constraint    |\*MAP(a,i)|\*MAP(a,e)|\*MAP(a,ɛ)|\*MAP(ɛ,i)|\*MAP(ɛ,e)|\*MAP(e,i)|ASSIM|ASSIM-ADJ|ASSIM-PARTIAL|
|--------------|----------|----------|----------|----------|----------|----------|-----|---------|-------------|
|Initial Weight|        15|        10|         5|        10|         5|         5|   50|       50|           50|
 
These tableaux and initial weights can be loaded into the `SoftTypologyTool` using the file `nonoverlappingfaithfulness/markednesshigh/markednesshigh.txt`.

#### \*MAP High: \*MAP constraints weighted above markedness constraints

|Constraint    |\*MAP(a,i)|\*MAP(a,e)|\*MAP(a,ɛ)|\*MAP(ɛ,i)|\*MAP(ɛ,e)|\*MAP(e,i)|ASSIM|ASSIM-ADJ|ASSIM-PARTIAL|
|--------------|----------|----------|----------|----------|----------|----------|-----|---------|-------------|
|Initial Weight|        30|        20|        10|        20|        10|        10|   10|       10|           10|

These tableaux and initial weights can be loaded into the `SoftTypologyTool` using the file `nonoverlappingfaithfulness/maphigh/maphigh.txt`. 

Simulations with the Markedness High weightings were run for 20 generations of 3600 iterations. Simulations with the \*MAP High weightings were run for 10 generations of 500 iterations.

Logs of sample simulations (stable and unstable runs for stepwise and saltatory patterns with different initial conditions) are available in the `/nonoverlappingfaithfulness` directory above. These include:

* Simulations with the Markedness High weighings (in `/nonoverlappingfaithfulness/markhigh`)
* Simulations with the \*MAP High weightings (in `/nonoverlappingfaithfulness/maphigh`)
* Probability of each target mapping at the end of each generation
* Probability of each target mapping, within each generation, per iteration
* Weight assigned to each constraint, on each iteration

### Results

 In all three test conditions (constraint set plus initial weighting condition), the saltatory harmony pattern was more stable across generations than the stepwise harmony pattern. The following table reports the percentages of learning runs in which a given pattern was stable for a given test condition.

|Test Condition   |Stepwise|Saltation|
|-----------------|--------|---------|
|Overlapping Faith|      0%|      34%|
|Markedness High  |     28%|     100%|
|\*MAP High       |     11%|      40%|

We interpret this result as predicting that saltatory harmony should be more easily learnable and therefore more robustly attested than stepwise harmony, contra the typological facts and the results of the Gestural Gradual Learning Algorithm.

Future work will seek to characterize why these featural, constraint-based approaches learn unattested saltatory height harmonies more easily than attested stepwise harmonies.

## External References
- Gnanadesikian, Amalia (1997). *Phonology with Ternary Scales*. PhD Dissertation, University of Massachusetts, Amherst. 
- Hayes, Bruce and White, James (2015). Saltation and the P-map. *Phonology* 32 267-302.
- White, James (2013). *Bias in phonological learning: evidence from saltation*. PhD Dissertation, University of California, Los Angeles.
- Zuraw, Kie (2007). The role of phonetic knowledge in phonological patterning: corpus and survey evidence from Tagalog infixation. *Language* 83. 277-316.
