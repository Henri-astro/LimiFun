import matplotlib.pyplot as plt

#own Project
import src.FindBound as FindBound


def MakeExampleplot():
    """This function creates an example plot for use in my paper"""
    
    RelPointX = [1.0,2.2,3.4,4.0,7.0]
    RelPointY = [5.0,5.8,6.3,6.5,6.7]
    
    IrrPointX = [2.0,2.5,2.9,3.5,4.2,5.1,5.6,6.0,6.0,6.5]
    IrrPointY = [5.2,5.4,4.9,6.0,5.5,5.7,5.8,5.2,6.2,6.0]
    
    xvalues = RelPointX + IrrPointX
    yvalues = RelPointY + IrrPointY
    
    a,b = FindBound.FindBoundaries( xvalues,yvalues )
    
    xmin = min(RelPointX)
    xmax = max(RelPointX)
    
    ymin = min(RelPointY)
    ymax = max(RelPointY)
    
    fig = plt.figure( figsize = [3.5,3.0], dpi = 200)
    plt.rcParams.update({'font.size': 8})
    
    plt.axline((xmin, a + b*xmin), (RelPointX[1], a + b*RelPointX[1]), c="black")
    plt.plot( RelPointX,RelPointY,color = "red", marker = "x", linestyle="none" )
    plt.plot( IrrPointX,IrrPointY,color = "black", marker = "+", linestyle="none" )
    
    plt.axline((xmin, ymin), (xmin,ymax), c="grey", linestyle = "--")
    plt.axline((xmin, ymax), (xmax,ymax), c="grey", linestyle = "--")
    
    plt.xlabel("log(x)")
    plt.ylabel("log(y)")
    
    plt.subplots_adjust(left=0.15, right=0.95, top=0.97, bottom=0.14)
    plt.show()
    plt.close()
