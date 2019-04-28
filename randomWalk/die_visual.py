from die import Die
import pygal

die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
# print(results)
frequent = []
for value in range(1,die.num_sides+1 ):
    fre = results.count(value)
    frequent.append(fre)
print(frequent)

# drawing
hist = pygal.Bar()
hist.title = 'resultes of rolling one D6 100 times'
hist.x_labels = ['1','2','3','4','5','6']
hist.y_title = 'frequency'
hist.add('D6', frequent)
hist.render_to_file('die.visual.svg')

