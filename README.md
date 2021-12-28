# advent-of-code-2021

Day 19:

    left_observer ---------------- key-star ------------ right_observer 

the key-star has two neighbours nearby and both observers can see them. Each observer makes a matrix:

    key-star
    bestis, the nearest neighbour
    nextis, the next-nearest neighbour

Each observer subtracts the key-star to move these three stars into the keystar-centered reference frame:

    0,0,0,
    keystar_to_bestis
    keystar_to_nextis

Now, these are in fact the same stars, so there is a rotation U_right; when you have it on the right, u right:

    what_left_sees == what_right_sees * U_right

What's true for 2 stars is true for all stars:

    0,0,0
    bestis minus keystar
    nextis minus keystar
    star_0 minus keystar
    star_1 minus keystar
    star_2 minus keystar
    ...
    star29 minus keystar

If U_right rotates, acting on the columns of this matrix, and translates the first two rows of this matrix 
from reference frame right_observer to reference frame left_observer, then likewise for all the other stars
in this matrix.


    1. Identify stars by their local types, i.e., the distance
        and cosine to the nearest two other stars.
    Result: 1a. These triples are seen often enough,
            1b. The "local type" hash has no false positive.
    
    2. For each pair of observers who can see a triple of stars,
        that triple specifies the change of basis to translate observations 
        from one reference frame to the neighbor.
        
    3. Walk through the graph of observers who are neighbours, translating to a 
        common reference frame.

    1a. If we declare regions neighbours when at least 1 fingerprint matches, 
    the graph of neighbours has 28 nodes and 94 edges, with degrees between 2 and 11. 
    It's enough that the graph is connected.
        
    1b. After part 1, (len(fi(so1[plan[-1][1]])) == len(so1[plan[-1][1]])) == True ,
    i.e., no two stars had the same hash.





day, runtime, version

17,     0.03s  low + slow * patient.

18,     1.5s,  "location-value-depth"

19,     0.4s,  "min-distance, 2nd-min-distance, cosine" hash for each star.

21,     77s,   recursion, ct = [1, 3, 6, 7, 6, 3, 1]

22,     many minutes.

23,     94s,    list all paths of all depths, including 146 that end at the goal state. len({x for x in sl}) = 78067 states; len(seen) = 57650 non-final states.
