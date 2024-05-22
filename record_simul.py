import json

NEW_NODE_RATE_FIXE = 0.01
PROBA_BERNOUILLI_FIXE = 0.3
ALPHA_FIXE = 0.85

file = open("data.json", "w")
dico = {
        "new_node_rate" : ({1 : [(1,2), (2,3), (3,4)],
                            2 : [(1,2), (2,3), (3,4)]}, 
                            (PROBA_BERNOUILLI_FIXE, ALPHA_FIXE)),
        "proba_bernouilli" : ({1 : [(1,2), (2,3), (3,4)],
                            2 : [(1,2), (2,3), (3,4)]}, (NEW_NODE_RATE_FIXE, ALPHA_FIXE)),
        "alpha" : ({1 : [(1,2), (2,3), (3,4)],
                    2 : [(1,2), (2,3), (3,4)]}, (NEW_NODE_RATE_FIXE, PROBA_BERNOUILLI_FIXE))
        }
dico_json = json.dumps(dico, indent=2)
file.write(dico_json)
file.close()