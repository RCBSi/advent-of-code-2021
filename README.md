# advent-of-code-2021

Day 19, Plan: 

    1. Identify stars by their local types, i.e., the distance
        and cosine to the nearest two other stars.
    Result: Success! 1a. Whenever two regions overlap, at least 
        one star and its two nearest neighbours are in the overlap, 
        and 1b. distance, distance, cosine is enough information for
        a hash: there are no false positives anywhere in space.
    
    2. For each pair of observers who can see a triple of stars,
        use that triple to translate observations 
        from one reference frame to another. 
        
    3. Make a "reduction plan" to transitively translate all 
        observations into a common reference frame. 
