# advent-of-code-2021

Day 19, Plan: 

    1. Identify stars by their local types, i.e., the distance
        and cosine to the nearest two other stars.
    Result: 1a. These triples are seen often enough,
            1b. The "local type" hash has no false positive.
    
    2. For each pair of observers who can see a triple of stars,
        that triple specifies the change of basis to translate observations 
        from one reference frame to the neighbor.
        
    3. Walk through the graph of neighbours, translating to a common
        reference frame.

    1a. If we declare regions neighbours when at least 1 fingerprint matches, 
    the graph of neighbours has 28 nodes and 94 edges, with degrees between 2 and 11. 
    It's enough that the graph is connected.
        
    1b. After part 1, (len(fi(so1[plan[-1][1]])) == len(so1[plan[-1][1]])) == True ,
    i.e., no two stars had the same hash.




date, runtime, version

18,     1.5s,  "location-value-depth"

19,     1s,    "min-distance, 2nd-min-distance, cosine" hash for each star.
