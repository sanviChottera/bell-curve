import random 
import plotly.express as px
import plotly.figure_factory as ff

#string, integer, list , dictionary - datatypes in python 
count = []
dice_result = []
for i in range(1,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2 )
    count.append(i)

#fig = px.bar( x = dice_result , y = count)
fig = ff.create_distplot(  [ dice_result] , [ "my dice result"]  , show_hist = True)

fig.show()