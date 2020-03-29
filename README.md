# MapCrypto
A re-authentication technique over comprised channels

# Scenario: Re-Authentication

- Authentication : Verifying if someone is who they claim in the **1st** communication with them
- Re-authentication : Verifying if someone is who they claim in communications **after the 1st** communication.

# Sample Usage Scenario

Let us say `user1` wants to re-authenticate `user2`.

Vice-versa can also be achieved using similar steps.

1. `user1` and `user2` make a secure communication.
 2. `user1` and `user2` agree on a random `map.txt` file. This file is generate by `python3 create_map.py`
 3. `user1` and `user2` both have this shared file in their individual PC's.
 4. `user1` and `user2` communicate happily, and close the connection.
 5. `user2` wants to contact `user1`.
 6. `user1`: `python3 generate_random_sequence.py`. Sends this output to `user2`
 7. `user2`: `python3 compute_sequence_answer.py | INPUT_FROM_user1`
 
Sends this output to `user1`

8. `user1`: 
Calculates
- `LocalOutput` = `python3 compute_sequence_answer.py | THE_SEQUENCE_SENT_TO_user2`
- `ForeignOutput` = `INPUT_FROM_user1`
```
if(LocalOutput == ForeignOutput):
        user1 verifies that user2 is who they claim to be
        user1 proceeds to communicate with user2
```

# Implementation [1/3]: Graphs Aspect
`map.txt` contains a "map". The "map" is just bunch of coordinates.

Think of every coordinate as a node. The graph formed using these coordinates is the complete graph with `V` vertices/nodes. Every vertex has an edge with every other node of the graph (no self-edges). The edges are weighted, with each edge's weight being the Euclidean distance between 2 nodes.

# Implementation [2/3]: Computing a Sequence
What happens when you run `$ python3 compute_sequence_answer.py` ?

Eg. `1 6 3 9 13` is our input. 1,6,3,9,13 refer to `point1`, `point6`, `point3`, `point9` & `point13`

`Output` = `dist(1,6) + dist(6,3) + dist(3,9) + dist(9,13)`

 where `dist(a,b)` is the Euclidean distance between the points `a` and `b`

This is basically saying what is the total distance travelled if you move in from `1 -> 6 -> 3 -> 9 -> 13`

# Implementation [3/3]: Idea & Resistance to Attacks

The idea is that we are reducing a long path to a single float number. So, it would be very difficult to reverse engineer it. So, the only way you would be able to compute the correct answer is if you had the correct `map.txt` file. We estimate that the attacker would need around `O(V!)` queries to be able to make up the map themselves. `V` is generally set to 1000. 1000! is an unthinkable number! So, our technique should be resistant to brute force attack.



# Did I Just Invent the Next Big Thing in Cryptography?

Obviously, this is just for fun. This would not make sense in a real-world scenario because:
- AES has no known vulnerability for repeated key use. The secret key in the 1st communication can be used for subsequent communications as well.
- `MapCrypto` is very memory-intensive. A `map.txt` file with 1000 coordinates measures to around `40KB`. For a single pair of users. Compare this with techniques like AES which measure to `256 bytes` at most!

> "Anyone, from the most clueless amateur to the best cryptographer, can create an algorithm that he himself can't break. It's not even hard. What is hard is creating an algorithm that no one else can break, even after years of analysis.
~ Bruce Schneier, 1998
