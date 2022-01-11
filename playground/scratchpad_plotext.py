import plotext as pt

# wave plot
# y = pt.plot()
# pt.plot(y)
# pt.title('Sine Wave')
# pt.show()

# bar plot
# pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
# percentages = [14, 36, 11, 8, 7, 4]

# pt.bar(pizzas, percentages)
# pt.title("Most Favored Pizzas in the World")
# pt.show()


# sketchy bar plat
# pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
# percentages = [14, 36, 11, 8, 7, 4]

# pt.bar(pizzas, percentages, orientation = "horizontal", width = 0.3) # or shorter orientation = 'h'
# pt.title("Most Favoured Pizzas in the World")
# pt.clc() # to remove colors
# pt.plotsize(100, 2 * len(pizzas) - 1 + 4) # 4 = 1 for x numerical ticks + 2 for x axes + 1 for title
# pt.show()

# multi bar plot
pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
male_percentages = [14, 36, 11, 8, 7, 4]
female_percentages = [12, 20, 35, 15, 2, 1]

pt.multiple_bar(pizzas, [male_percentages, female_percentages], label = ["men", "women"])
pt.title("Most Favored Pizzas in the World by Gender")
pt.show()
pt.doc.multiple_bar()
pt.doc.bar()
pt.doc.plot()

# # stacked bar plot
#
# pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
# male_percentages = [14, 36, 11, 8, 7, 4]
# female_percentages = [12, 20, 35, 15, 2, 1]
#
# pt.stacked_bar(pizzas, [male_percentages, female_percentages], label = ["men", "women"])
# pt.title("Most Favored Pizzas in the World by Gender")
# pt.show()Z