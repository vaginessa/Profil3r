import re
from collections import OrderedDict
import math
import sys
import math

# To compute the probability that a string of characters is an username, 
# we use the transition matrix associated to the Markov chain of usernames
# For example: 

# With this Markov Chain:

#           ┌────────┐
#     ┌─────┤ Start  ├────┐
#  0.4│     └────────┘    │ 0.6
#     │                   │
#     ▼                   ▼
# ┌────────────┐     ┌─────────┐
# │ Uppercase  │ 0.3 │         │
# │ Alphabetic ├────►│ Number  │
# │ Sequence   │     │         │
# └─────┬──────┘     └┬──────┬─┘
#       │0.7          │      │
#       │          0.3│      │ 0.7
#       ▼             │      │
# ┌────────────┐      │      ▼
# │ Underscore │ ◄────┘   ┌─────┐
# └────────────┘          │ End │
#                         └─────┘

# The transition matrix will be:

# [ 0,   0.4, 0.6, 0,   0  ]
# [ 0,   0,   0.3, 0.7, 0  ]
# [ 0,   0,   0,   0.3, 0.7]
# [ 0,   0,   0,   0,   0  ]
# [ 0,   0,   0,   0,   0  ]

usernames_transition_matrix = [
                                [0.0, 0.0725, 0.8491, 0.0247, 0.0263, 0.0023, 0.0175, 0.0067, 0.0006, 0.0002, 0.0, 0.0001, 0.0],
                                [0.0, 0.1718, 0.0, 0.0441, 0.0, 0.0458, 0.1607, 0.0648, 0.0486, 0.0174, 0.021, 0.0013, 0.4245],
                                [0.0, 0.0027, 0.0, 0.0019, 0.0, 0.0019, 0.2159, 0.0717, 0.0813, 0.0406, 0.0597, 0.0004, 0.5239],
                                [0.0, 0.0, 0.1522, 0.0, 0.1076, 0.0, 0.1584, 0.092, 0.0226, 0.0112, 0.0097, 0.001, 0.4452],
                                [0.0, 0.0421, 0.0, 0.0309, 0.0, 0.0259, 0.1238, 0.2008, 0.0693, 0.0485, 0.1294, 0.0009, 0.3284],
                                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1378, 0.2862, 0.0328, 0.0161, 0.0344, 0.0037, 0.4891],
                                [0.0, 0.002, 0.0627, 0.003, 0.0295, 0.0029, 0.0, 0.0, 0.0122, 0.006, 0.0055, 0.0002, 0.876],
                                [0.0, 0.0182, 0.244, 0.0194, 0.1431, 0.0193, 0.0, 0.0, 0.0127, 0.0042, 0.0046, 0.0004, 0.5341],
                                [0.0, 0.0271, 0.6293, 0.0148, 0.0758, 0.0079, 0.1817, 0.0357, 0.0089, 0.0012, 0.0005, 0.0, 0.0171],
                                [0.0, 0.0149, 0.7095, 0.0049, 0.0778, 0.0025, 0.1435, 0.0274, 0.0022, 0.0073, 0.0007, 0.0001, 0.0092],
                                [0.0, 0.014, 0.7805, 0.005, 0.0883, 0.0034, 0.0899, 0.0121, 0.001, 0.001, 0.0019, 0.0, 0.0029],
                                [0.0, 0.0589, 0.2674, 0.0271, 0.1116, 0.0236, 0.0508, 0.1704, 0.003, 0.0029, 0.0005, 0.1169, 0.1669],
                                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                              ]

tokens = OrderedDict()
tokens['CAPITAL_ALPHABETIC_SEQUENCE'] = r'[A-Z][a-z]+'
tokens['LOWERCASE_ALPHABETIC_SEQUENCE'] = r'[a-z]{2,}'
tokens['UPPERCASE_ALPHABETIC_SEQUENCE'] = r'[A-Z]{2,}'
tokens['LOWERCASE_LETTER'] = r'[a-z]'
tokens['UPPERCASE_LETTER'] = r'[A-Z]'
tokens['NUMBER_SEQUENCE'] = r'[0-9]{2,}'
tokens['NUMBER'] = r'[0-9]'
tokens['UNDERSCORE'] = r'[_]'
tokens['HYPHEN'] = r'[-]'
tokens['DOT'] = r'[.]'
tokens['UNUSUAL_SEPARATOR'] = r'.'

def filter(self):
    probabilities = {}

    usernames = self.permutations_list

    for username in usernames:
        username_tmp = username

        # We convert each username into a list of tokens
        # e.g. RandomUsername_82 -> ["START", "CAPITAL_ALPHABETIC_SEQUENCE", "CAPITAL_ALPHABETIC_SEQUENCE", "UNDERSCORE", "END"]
        chain = ["START"]
        while username_tmp != "":   
            for token, regexp in tokens.items():
                match = re.findall(regexp, username_tmp)
                if match:
                    if username_tmp.find(match[0]) == 0:
                        chain.append(token)
                        username_tmp = username_tmp[len(match[0]):]
                        break
        chain.append("END")

        # Permutations with only one element are not taken into account
        # e.g ["john", "doe", "52"] -> "john"
        if len(chain) == 3:
            probability = 0
        else:
            probability = 1

        # We calculate the probability of each permutation using the transition matrix.
        probability *= usernames_transition_matrix[0][list(tokens.keys()).index(chain[1]) + 1]
        for i in range(2, len(chain)-1):
            start_token = list(tokens.keys()).index(chain[i - 1]) + 1
            end_token = list(tokens.keys()).index(chain[i]) + 1
            probability *= usernames_transition_matrix[start_token][end_token]
        probability *= usernames_transition_matrix[list(tokens.keys()).index(chain[-2])][-1] * math.exp(len(chain))

        probabilities[username] = probability

    # We sort by probability
    probabilities = list({k: v for k, v in sorted(probabilities.items(), key=lambda item: item[1])}.keys())

    # Number of probables usernames : min { 10, log(number of permutations^2) }
    number_of_probables_usernames = max(6, min(10, round(math.log(len(probabilities)**2))))

    probables_usernames = probabilities[-1 * number_of_probables_usernames:]
    self.permutations_list = probables_usernames