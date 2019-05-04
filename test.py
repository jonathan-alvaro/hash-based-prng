from main import *
import matplotlib.pyplot as plt
import seaborn as sns
import sys

nums = run_hash_algorithm(hashlib.sha512, num_iters=int(sys.argv[1]))

plt.show(sns.distplot(nums))