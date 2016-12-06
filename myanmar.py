"""This Graph Show import and export in Myanmar"""
import pygal
def main():
    """This Function make graph to show data"""
    bar_chart = pygal.Bar()
    bar_chart.title = "นำเข้า-ส่งออกในประเทศพม่า"
    bar_chart.x_labels = map(str, range(2549, 2559))
    bar_chart.add('ส่งออก', [140789.55, 136270.14, 114520.67, 96523.51, 85879.95, 65631.18, 52652.37, 43859.02, 33043.11, 28849.00, 798018.50])
    bar_chart.add('นำเข้า', [121185.58, 127276.08, 123690.94, 114820.15, 106511.02, 90000.45, 95975.92, 112426.00, 80030.63, 88707.91])
    bar_chart.render()
    bar_chart.render_to_file('myamar.svg')
main()
