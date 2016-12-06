"""This Graph Show import and export in Indonisia"""
import pygal
def main():
    """This Function make graph to show data"""
    bar_chart = pygal.HorizontalBar(print_values=True, print_values_position='top')
    bar_chart.title = "นำเข้า-ส่งออกในประเทศอินโดนีเซีย"
    bar_chart.x_labels = map(str, range(2549, 2559))
    bar_chart.add('ส่งออก', [327430.22, 305610.92, 263740.00, 346267.03, 303877.17, 232856.21, 158917.86, 208017.51, 165970.57, 126196.91])
    bar_chart.add('นำเข้า', [223589.27, 236779.36, 247113.43, 252896.75, 225335.37, 182214.96, 130908.94, 180271.39, 138550.21, 131938.76])
    bar_chart.render()
    bar_chart.render_to_file('Indo.svg')
main()
