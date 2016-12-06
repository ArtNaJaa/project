"""This Graph Show import and export in Brunei"""
import pygal
def main():
    """This Function make graph to show data"""
    bar_chart = pygal.Bar()
    bar_chart.title = "นำเข้า-ส่งออกในบรูไน"
    bar_chart.x_labels = map(str, range(2549, 2559))
    bar_chart.add('ส่งออก', [3145.27, 3210.72, 4074.40, 4001.45, 4076.56, 4134.71, 5894.85, 3568.11, 4585.18, 5019.80])
    bar_chart.add('นำเข้า', [1322.80, 1688.57, 2969.30, 3800.22, 3100.42, 4014.86, 13763.52, 16878.89, 21220.72, 24280.16])
    bar_chart.render()
    bar_chart.render_to_file('Brunei.svg')
main()
