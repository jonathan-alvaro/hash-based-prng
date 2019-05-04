import random
import time
import seaborn as sns
import matplotlib.pyplot as plt

nums = []
start_time = time.time()
for _ in range(8000000):
    nums.append(random.randint(0, 9))
end_time = time.time()

fig = plt.figure()
new_axes = sns.distplot(nums, kde=False)
new_axes.set_title("Randint")
fig.add_axes(new_axes)
plt.show(fig)