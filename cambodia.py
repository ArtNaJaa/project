"""This Graph Show import and export in Cambodia"""
import pygal
def main():
    """This Function make graph to show data"""
    bar_chart = pygal.Bar()
    bar_chart.title = "Import and Export in Cambodia"
    bar_chart.x_labels = map(str, range(2549, 2559))
    bar_chart.add('ส่งออก', [47002.96, 46709.05, 67025.57, 53917.76, 74265.08, 81238.91, 116780.03, 128643.32, 145486.68, 167048.28])
    bar_chart.add('นำเข้า', [4813.75, 3900.48, 3007.48, 2659.58, 6869.95, 5372.83, 7800.23, 10920.05, 19180.85, 21593.26])
    bar_chart.render()
    bar_chart.render_to_file('Cambodia.svg')
main()
