import PySimpleGUI as sg
from math import sin,cos,pi,sqrt,tan

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

def calculateInnerRadius(points):
    # Find the midpoint between two adjacent points
    # This represents the intersection of the incircle and the polygon (tangent)
    midpoint = ((points[0][0]+points[1][0])/2, (points[0][1]+points[1][1])/2)

    # Calculate the distance from the midpoint to the origin
    # This represents the radius of the incircle
    return sqrt(midpoint[0]**2 + midpoint[1]**2)

def about():
    sg.popup("Archimedes found a pretty accurate value for π by drawing polygons with more and more sides, both inside and outside of a circle. He knew that π would lie between the perimeter of the inside polygon and the outside polygon. Here, by inputting different values for the number of sides, you can draw inscribed polygons on a circle with radius 1. The value of the perimeter will approach 2π, since the circle's diameter is two.", title="Check it!")

def loop(window):
    # Event Loop c
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks the "Exit" button
            return
        if event == 'numSides' or 'Calculate':
            try:
                numSides = window['numSides'].get()
                window['graph'].erase()
                window['graph'].draw_circle((0,0), 1)
                points, perimeter = drawPolygon(numSides)
                window['graph'].draw_polygon(points, fill_color="CadetBlue4")
                # Calculate the radius of the incircle
                inradius = calculateInnerRadius(points)
                # Calculate the ratio of the circumradius (1) to the inradius
                rad_ratio = 1 - inradius
                # Calculate the approximate perimeter of the circumscribed polygon
                perimeterc = perimeter + perimeter * rad_ratio
                window['graph'].draw_circle((0,0), calculateInnerRadius(points), fill_color="red")
                window['perimeterc'].update(str(perimeter)[0:12])
                window['perimeteri'].update(str(perimeterc)[0:12])
                window['picalcl'].update(str(perimeter/2)[0:12])
                window['picalcu'].update(str(perimeterc/2)[0:12])
            except:
                pass
        if event == 'How It Works':
            about()

def initialize():
    sg.theme('LightGreen7')
    layout = [  [sg.Text("Perimeter of the inscribed polygon:"), sg.Text(key="perimeteri", size=(12,1)), sg.Text("Perimeter of the circumscribed polygon:"), sg.Text(key="perimeterc", size=(12,1))],
                [sg.Text("Upper bound for π:"), sg.Text(key='picalcu',size=(12,1)), sg.Text("Lower bound for π:"), sg.Text(key='picalcl',size=(12,1))],
                [sg.Text('Enter number of sides:'), sg.Spin(values=[i for i in range(3, 1000)],key="numSides", enable_events=True,size=(6,1)), sg.Button('Calculate')],
                [sg.Graph(canvas_size=(300,300),key="graph", graph_bottom_left=(-1,-1), graph_top_right=(1.0,1.0), background_color="White")],
                [sg.Button('Exit'), sg.Button('How It Works')]]

    # Create the Window
    return sg.Window('Archimedes!', layout, element_justification='c')

window = initialize()
loop(window)
window.close()
