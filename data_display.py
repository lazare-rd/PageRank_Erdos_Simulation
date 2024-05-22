import matplotlib.pyplot as plt
import json
from run_simul import *
NEW_NODE_RATE = [0.01, 0.005, 0.0005]
PROBA_BERNOUILLI = [0.1, 0.3, 0.5, 0.8]
ALPHA = [0.85, 0.7, 0.6, 0.5]

file = open("data.json", "r")
data_dico = json.loads(file.read())
file.close()

x = [i for i in range(1, 6)]

plt.plot(x, data_dico["new_node_rate"][0]["0.005"][0], 'b--', label='x_0 usuel')
plt.plot(x, data_dico["new_node_rate"][0]["0.005"][1], 'r--', label='x_0 mois t-1')
plt.xlabel('Mois')
plt.ylabel('nb_itérations')
plt.suptitle("new node rate = 0.005")
plt.legend()
plt.show()
