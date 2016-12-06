"""This Graph Show import and export in Laow"""
import pygal
def main():
    """This Function make graph to show data"""
    bar_chart = pygal.Bar()
    bar_chart.title = "นำเข้า-ส่งออกในประเทศลาว"
    bar_chart.x_labels = map(str, range(2549, 2559))
    bar_chart.add('ส่งออก', [142909.28, 129666.32, 113542.08, 110802.47, 83534.30, 67606.02, 56045.36, 58392.22, 45185.27, 38720.47])
    bar_chart.add('นำเข้า', [50291.27, 45841.95, 41693.35, 38682.24, 34488.78, 23935.72, 15944.04, 20571.63, 16295.00, 19752.71])
    bar_chart.render()
    bar_chart.render_to_file('laow.svg')
main()
