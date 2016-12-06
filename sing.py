"""This Graph Show import and export in Singapore"""
import pygal
def main():
    """This Function make graph to show data"""
    bar_chart = pygal.HorizontalBar(print_values=True, print_values_position='top')
    bar_chart.title = "นำเข้า-ส่งออกในประเทศสิงคโปร์"
    bar_chart.x_labels = map(str, range(2549, 2559))
    bar_chart.add('ส่งออก', [294436.78, 335520.29, 339782.51, 334639.05, 343976.47, 284693.62, 257967.52, 332443.81, 330737.05, 318597.22])
    bar_chart.add('นำเข้า', [242928.39, 256211.29, 250732.46, 244933.04, 237668.33, 201897.17, 197352.40, 236131.91, 218679.86, 218070.00])
    bar_chart.render()
    bar_chart.render_to_file('sing.svg')
main()
