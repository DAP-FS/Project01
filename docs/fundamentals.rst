Fundamentals
============

This section covers the core mathematical and computational concepts that form the 
foundation of theory of computation.

Mathematical Prerequisites
-------------------------

Set Theory
~~~~~~~~~~~

Understanding of basic set operations is essential:

* Union, intersection, and complement
* Cartesian products
* Relations and functions
* Equivalence relations

Logic
~~~~~

Propositional and predicate logic concepts:

* Boolean algebra
* Logical connectives
* Quantifiers
* Proof techniques

Formal Language Definitions
---------------------------

Alphabet
~~~~~~~~

An alphabet Σ is a finite, non-empty set of symbols.

Example: Σ = {0, 1} for binary strings

String
~~~~~~

A string (or word) over an alphabet Σ is a finite sequence of symbols from Σ.

* Empty string: ε (epsilon)
* Length of string w: |w| (number of symbols)
* Concatenation: w₁w₂

Language
~~~~~~~~

A language L over alphabet Σ is a set of strings over Σ.

Examples:

* L₁ = {ε} (language containing only the empty string)
* L₂ = {0, 1, 00, 11, 000, 111, ...} (all strings of 0s and 1s)
* L₃ = ∅ (empty language)

Operations on Languages
~~~~~~~~~~~~~~~~~~~~~~~

* Union: L₁ ∪ L₂
* Intersection: L₁ ∩ L₂
* Concatenation: L₁ · L₂ = {xy | x ∈ L₁, y ∈ L₂}
* Kleene star: L* = L⁰ ∪ L¹ ∪ L² ∪ ...

Grammar Basics
--------------

A formal grammar G = (V, Σ, R, S) where:

* V: finite set of variables (non-terminals)
* Σ: finite set of terminals (alphabet)
* R: finite set of production rules
* S: start variable

The Chomsky Hierarchy
~~~~~~~~~~~~~~~~~~~~

1. **Type 0** (Unrestricted): No restrictions on production rules
2. **Type 1** (Context-sensitive): alpha → beta where |alpha| ≤ |beta|
3. **Type 2** (Context-free): A → alpha where A is a variable
4. **Type 3** (Regular): A → aB or A → a where A, B are variables, a is terminal