import matplotlib.pyplot as plt

# Line plot where (x,y) = (List of year, List of population)
plt.plot(x,y)
plt.show()

# Scatter plot (plots all countries with a dot)
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')
plt.show()

# Histogram with i number of bins
plt.hist(life_exp, i)
plt.show()

# Clean up the plot
plt.clf()

# Add axis labels
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')

# Add title
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# Size of dots in scatter plot (e.g bigger bubbles for more population)
# Store population as a numpy array: np_pop
np_pop = np.array(pop)
np_pop = np_pop * 2
plt.scatter(gdp_cap, life_exp, s = np_pop)

# add different colors for dots in scatter plot (here c = List of colors for each country)
# add alpha for transparency (with 0 being totally transparent)
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Adds text for some data
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Draw grid lines
plt.grid(True)