"topdown" is a software library for the Python 2.7 language.
Its copyright belongs to me, Aaron Mansheim (http://github.com/minopret).
I have not decided upon a free or open-source license for this software.

"topdown" provides a top-down parser for natural language,
as explained by James F. Allen in the book Natural Language Understanding.
Using the Earley algorithm, it guesses the phrasing
and the grammar symbol and features for each word and each phrase.
The parse produces every guess that is permitted by a
given grammar. A sentence that permits multiple guesses
is an ambiguous sentence. There is no attempt to notice or
eliminate improbable guesses.

Running the file SampleParser.py as "python SampleParser.py" prints
the log shown below for a parse of the phrase "the dog".

An "arc" is a partial match between a grammar rule and a hypothesized
sequence of grammar symbols that match the words observed so far.
Abbreviations used in the particular grammar include "noun
phrase" (NP), "article" (ART), "noun" (N), and the feature for noun
or verb "agreement" in person and number (AGR) whose values include
third-person singular (3s) and third-person plural (3p).

    Introducing symbol NP['AGR: ?x']
        Using the top-down rule,  new active arcs are added for NP['AGR: ?x']
        An arc can be extended NP['AGR: ?a'] -> o ART['AGR: ?a'] N['AGR: ?a'] from 0 to 0
    Introducing symbol ART['AGR: ?a']
    Entering ART["ROOT: ['the']", "AGR: ['3s', '3p']"] from 0 to 1
        An arc can be extended NP["AGR: ['3s', '3p']"] -> ART["AGR: ['3s', '3p']"] o N["AGR: ['3s', '3p']"] from 0 to 1
    Introducing symbol N["AGR: ['3s', '3p']"]
    Entering N["ROOT: ['DOG1']", "AGR: ['3s']"] from 1 to 2
        An arc can be extended NP["AGR: ['3s']"] -> ART["AGR: ['3s']"] N["AGR: ['3s']"] o from 0 to 2
    Entering NP["AGR: ['3s']"] from 0 to 2
