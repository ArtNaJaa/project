"""This Graph Show import and export in All Country"""
import pygal
def main():
    """This Function make graph to show data"""
    bar_chart = pygal.HorizontalBar(print_values=True, print_values_position='top')
    bar_chart.title = "นำเข้า-ส่งออกทุกประเทศในอาเซียน"
    bar_chart.x_labels = ['บรูไน', 'กัมพูชา', 'อินโดนีเซีย', 'ลาว', 'มาเลเซ๊ย', 'พม่า', 'ฟิลิปปินส์', 'สิงคโปร์', 'เวียดนาม']
    bar_chart.add('ส่งออก', [41711.05, 928117.64, 2438884.40, 846406.79, 3346247.91, 798018.50, 1408412.99, 3172794.32, 1857897.60])
    bar_chart.add('นำเข้า', [93039.46, 86118.46, 1949598.44, 307496.69, 3600263.76, 1060624.68, 782157.63, 2304604.85, 734878.77])
    bar_chart.render()
    bar_chart.render_to_file('All.svg')
main()
