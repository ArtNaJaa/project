"""This Graph Show import and export in Vietnam"""
import pygal
def main():
    """This Function make graph to show data"""
    bar_chart = pygal.Bar()
    bar_chart.title = "นำเข้า-ส่งออกในประเทศเวียดนาม"
    bar_chart.x_labels = map(str range(2549, 2559))
    bar_chart.add('ส่งออก', [217546.25, 253260.62, 217546.25, 200274.70, 212703.66, 184463.07, 159224.41, 165101.24, 130870.51, 116906.89])
    bar_chart.add('นำเข้า', [137847.97, 127978.55, 99991.87, 93359.47, 61983.85, 44714.08, 47747.78, 48110.97, 38655.38, 34488.85])
    bar_chart.render()
    bar_chart.render_to_file('vietnam.svg')
main()
