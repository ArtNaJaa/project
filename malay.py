"""This Graph Show import and export in Malaysia"""
import pygal
def main():
    """This Function make graph to show data"""
    bar_chart = pygal.Bar()
    bar_chart.x_labels = map(str, range(2549, 2559))
    bar_chart.add('ส่งออก', [342844.22, 410287.25, 393568.51, 383674.62, 373614.58, 334598.81, 260837.29, 325280.10, 269581.72, 251960.81])
    bar_chart.add('นำเข้า', [406033.17, 414464.25, 406576.27, 409623.46, 376183.48, 343889.13, 295286.73, 322995.16, 299885.33, 325326.78])
    bar_chart.render()
    bar_chart.render_to_file('malaysia.svg')
main()
