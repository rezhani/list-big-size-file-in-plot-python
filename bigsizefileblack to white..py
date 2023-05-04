import os
import matplotlib.pyplot as plt

# Get file sizes and names
file_sizes = []
file_names = []
for root, dirs, files in os.walk('C:/'):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.isfile(file_path):
            file_sizes.append(os.path.getsize(file_path))
            file_names.append(file)

# Sort file sizes and names
file_sizes, file_names = zip(*sorted(zip(file_sizes, file_names), reverse=True))

# Plot the 10 biggest files
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('equal')

total_size = sum(file_sizes)
sizes = [size/total_size for size in file_sizes][:10]
colors = [(i/n, i/n, i/n) for i in range(n)] #putih ke hitam
#colors = [((n - i) / n, (n - i) / n, (n - i) / n) for i in range(n)] #hitam ke putih
labels = [f"{name}\n({size/1024/1024:.2f} MB)" for name, size in zip(file_names[:10], file_sizes[:10])]
plt.pie(sizes, labels=labels,startangle=90, colors=colors)

plt.show()
