import PySimpleGUI as sg
from math import sin,cos,pi,sqrt

def drawPolygon(numSides:int):
# Returns a list of points of a polygon, and the perimeter of the polygon
    points = []
    perimeter = 0

    for k in range(1, numSides + 1):
        i = (2 * k * pi)/numSides + pi/2
        points.append((cos(i), sin(i)))

    perimeter = numSides * sqrt( 
        (points[0][0] - points[1][0])**2 
        + 
        (points[0][1] - points[1][1])**2 
    )
    return points, perimeter

sg.theme('LightGreen7')  
layout = [  [sg.Text("Perimeter of this polygon:"), sg.Text(key="perimeter", size=(12,1)), sg.Text("Our Calculated Value for π:"), sg.Text(key='picalc',size=(12,1))],
            [sg.Text('Enter number of sides:'), sg.Spin(values=[i for i in range(3, 1000)],key="numSides", enable_events=True,size=(6,1))],
            [sg.Graph(canvas_size=(300,300),key="graph", graph_bottom_left=(-1,-1), graph_top_right=(1.0,1.0), background_color="White")],
            [sg.Button('Exit')] ]

# Create the Window
window = sg.Window('Archimedes!', layout, element_justification='c')
sg.popup("Archimedes found a pretty accurate value for π by drawing polygons with more and more sides, both inside and outside of a circle. He knew that π would lie between the perimeter of the inside polygon and the outside polygon. Here, by inputting different values for the number of sides, you can draw inscribed polygons on a circle with radius 1. The value of the perimeter will approach 2π, since the circle's diameter is two.", title="Check it!")
# Event Loop c
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    if event == 'numSides':
        try:
            window['graph'].erase()
            points, perimeter = drawPolygon(window['numSides'].get())
            window['graph'].draw_circle((0,0), 1)
            window['graph'].draw_polygon(points, fill_color="CadetBlue4")
            window['perimeter'].update(str(perimeter)[0:12])
            window['picalc'].update(str(perimeter/2)[0:12])
        except:
            pass

window.close()