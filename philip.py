"""This Graph Show import and export in Philippines"""
import pygal
def main():
    """This Function make graph to show data"""
    bar_chart = pygal.Bar()
    bar_chart.x_labels = map(str, range(2549, 2559))
    bar_chart.add('ส่งออก', [202813.50, 188509.11, 152480.36, 150141.86, 139842.77, 154914.88, 102928.49, 115197.35, 103784.24, 97800.43])
    bar_chart.add('นำเข้า', [80388.41, 84955.74, 80391.95, 85199.39, 82479.64, 75984.04, 61276.78, 75660.74, 74560.90, 81260.04])
    bar_chart.render()
    bar_chart.render_to_file('phil.svg')
main()
