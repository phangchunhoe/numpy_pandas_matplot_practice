import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 250, 275, 225])
color = ["red", "yellow", "blue", "green"]

# To Create Pie Chart
# autopct="%1f" to display percentages in pie chart
# explode[x, x, x, x]; Choose the one that you want to displace
# shadow=True to include shadow
# startangle; is to rotate the pi chart
plt.pie(values, 
        labels=categories, 
        autopct="%1.1f%%", 
        colors=color, 
        explode=[0, 0, 0, .1],
        shadow=True,
        startangle=90)

# Title
plt.title("Princeston University")
plt.show()