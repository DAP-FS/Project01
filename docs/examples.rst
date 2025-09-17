Examples
========

This section provides practical examples and case studies demonstrating key concepts 
in theory of computation.

Regular Languages
-----------------

Example 1: Binary Numbers Divisible by 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Design a finite automaton that accepts binary strings representing 
numbers divisible by 3.

**Solution**: We need to track the remainder when dividing by 3.

States:
* q₀: remainder 0 (accepting state)
* q₁: remainder 1  
* q₂: remainder 2

Transitions (reading bit b):
* From qᵢ reading b: go to state (2i + b) mod 3

**Implementation tip**: Use modular arithmetic to determine state transitions.

Example 2: Balanced Parentheses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Determine if a string of parentheses is balanced.

**Note**: This is NOT a regular language! It requires a context-free grammar.

Context-Free Languages
----------------------

Example 3: Arithmetic Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Grammar for simple arithmetic**::

    E → E + T | E - T | T
    T → T * F | T / F | F  
    F → (E) | id | num

**Best practice**: Left-factorize to avoid ambiguity in parsing.

**Improved grammar**::

    E → T E'
    E' → + T E' | - T E' | ε
    T → F T'
    T' → * F T' | / F T' | ε
    F → (E) | id | num

Complexity Analysis Examples
---------------------------

Example 4: Matrix Multiplication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Standard algorithm**: O(n³)

.. code-block:: python

    def matrix_multiply(A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C

**Strassen's algorithm**: O(n^log₂7) ≈ O(n^2.807)

**Key insight**: Reduce 8 multiplications to 7 through clever recombination.

Example 5: Graph Algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Depth-First Search**:

Time complexity: O(V + E)
Space complexity: O(V) for recursion stack

.. code-block:: python

    def dfs(graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)
        
        return visited

Undecidability Examples
----------------------

Example 6: The Halting Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Theorem**: There is no algorithm that can determine whether an arbitrary program 
will halt on a given input.

**Proof sketch by contradiction**:

1. Assume such an algorithm H exists
2. Construct a program P that calls H on itself
3. If H says P halts, make P loop forever
4. If H says P doesn't halt, make P halt immediately
5. This creates a contradiction

**Practical implication**: Static analysis tools cannot be complete for all programs.

Real-World Applications
----------------------

Example 7: Regular Expressions in Text Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Email validation regex** (simplified)::

    [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

**Best practice**: Use specialized libraries for complex validation rather than 
trying to capture all edge cases in a single regex.

Example 8: Compiler Design
~~~~~~~~~~~~~~~~~~~~~~~~~

**Lexical analysis**: Use finite automata to tokenize source code
**Parsing**: Use pushdown automata for syntax analysis
**Optimization**: Apply complexity theory to choose efficient algorithms

**Key insight**: Different phases of compilation use different computational models 
appropriate to their complexity requirements.