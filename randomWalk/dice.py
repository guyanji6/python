from die import Die
import pygal

die1 = Die()
die2 = Die()
results = []
for roll_num in range(100):
    result = die1.roll() + die2.roll()
    results.append(result)
# print(results)
frequent = []
maxx = die1.num_sides+die2.num_sides
for value in range(1,maxx+1 ):
    fre = results.count(value)/100
    frequent.append(fre)
print(frequent)

# drawing
hist = pygal.Bar()
hist.title = 'resultes of rolling one D6 100 times'
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
hist.y_title = 'frequency'
hist.add('D6', frequent)
hist.render_to_file('dice.visual.svg')

