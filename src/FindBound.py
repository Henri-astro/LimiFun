import math


def CompAB( X1, Y1, X2, Y2 ):
    """computes the parameters of a line a + b*x through the points (X1,Y1) and (X2,Y2)"""
    
    b = ( Y2 - Y1 ) / ( X2 - X1 )
    a = Y1 - b* X1
    
    return a,b


def FindBoundaries( xvalues, yvalues, BPos = True, Max = True ):
    """Find find boundaries around data in linear space
    xvalues: the x-values of the points given
    yvalues: the y-values of the points given"""
    
    #find the points at the edges of the graph
    if Max:
        YExt = max( yvalues )
    else:
        YExt = min( yvalues )
        
    IndYExt = [i for i,y in enumerate(yvalues) if y==YExt]
    if BPos == Max:
        IndYExt = [i for i in IndYExt if xvalues[i] == min( [ xvalues[i] for i in IndYExt ] )][0]
    else:
        IndYExt = [i for i in IndYExt if xvalues[i] == max( [ xvalues[i] for i in IndYExt ] )][0]
            
    if BPos == Max:
        Xext = min( xvalues )
    else:
        Xext = max( xvalues )
        
    IndXext = [i for i,x in enumerate(xvalues) if x==Xext]
    if Max:
        IndXext = [i for i in IndXext if yvalues[i] == max( [ yvalues[j] for j in IndXext ] )][0]
    else:
        IndXext = [i for i in IndXext if yvalues[i] == min( [ yvalues[j] for j in IndXext ] )][0]
    
    #make the line between the points at the edges
    a,b = CompAB( Xext,yvalues[ IndXext ],xvalues[ IndYExt ],YExt )
    
    f = lambda x: a + b*x
    
    #find all relevant Points
    RelPoints = []
    for nElem in range( len( xvalues )):
        if nElem == IndXext or nElem == IndYExt:
            continue
        
        if ( Max and f(xvalues[nElem]) < yvalues[nElem] ) or ( not Max and f(xvalues[nElem]) > yvalues[nElem] ):
            RelPoints.append( nElem )
            
    if [] == RelPoints:
        return a,b
    
    #make lines through all the relevant points and move them to their optimal position
    #sort relevant points by xvalue
    sortfkt = lambda index: xvalues[index]
    RelPoints.sort( key = sortfkt )
    
    if BPos == Max:
        RelPoints = [IndXext] + RelPoints + [IndYExt]
    else:
        RelPoints = [IndYExt] + RelPoints + [IndXext]
    
    #delete points not relevant enough
    nElem = 0
    while True:
        Index1 = RelPoints[nElem]
        Index2 = RelPoints[nElem + 1]
        
        if xvalues[Index1] == xvalues[Index2]:      #this situation can only occur, when the second point is to be deleted or at the beginning
            if nElem == 0:
                RelPoints = RelPoints[1:]
            else:
                RelPoints = RelPoints[:nElem+1] + RelPoints[nElem+2:]
            continue
        
        a,b = CompAB( xvalues[ Index1],yvalues[ Index1],xvalues[ Index2],yvalues[ Index2] )
        
        
        delete = False
        for nElem2 in range( nElem + 2, len( RelPoints ) ):
            index = RelPoints[nElem2]
            
            if ( Max and a + b*xvalues[index] < yvalues[index] ) or ( not Max and a + b*xvalues[index] > yvalues[index] ):
                delete = True
                break
            
        if delete:
            RelPoints = RelPoints[:nElem+1] + RelPoints[nElem+2:]
        else:
            nElem += 1
        
        if nElem == len( RelPoints ) - 2:
            break
    
    #maximise the areas of a line through the points so that no point is left outside the boundary
    #the line that achieves that is always a connecting line between two of the dots
    AreaOutSide = 0.0
    for nElem in range( len( RelPoints ) - 1 ):
        Index1 = RelPoints[ nElem ]
        Index2 = RelPoints[ nElem + 1]
        aTemp,bTemp = CompAB( xvalues[Index1], yvalues[Index1], xvalues[Index2], yvalues[Index2] )
        
        if ( BPos and bTemp < 0.0 ) or ( not BPos and bTemp > 0.0 ):
            continue
        
        if BPos:
            Area = (YExt - aTemp - bTemp * Xext) * ((YExt - aTemp)/bTemp - Xext)
        else:
            Area = (aTemp + bTemp * Xext - YExt) * ((YExt - aTemp)/bTemp - Xext)
        
        if Area > AreaOutSide:
            AreaOutSide = Area
            a = aTemp
            b = bTemp
            
    return a,b
    

def FindBoundariesLog( xvalues, yvalues, BPos = True, Max = True ):
    """Find find boundaries around data in log space
    xvalues: the x-values of the points given
    yvalues: the y-values of the points given"""
    
    logxvalues = [ math.log10( val ) for val in xvalues ]
    logyvalues = [ math.log10( val ) for val in yvalues ]
    
    Res = FindBoundaries( logxvalues, logyvalues, BPos, Max )
    
    return pow( 10.0, Res[0] ),Res[1]
    
    
def FindBoundariesLogX( xvalues, yvalues, BPos = True, Max = True ):
    """Find find boundaries around data in log(x)-y space
    xvalues: the x-values of the points given
    yvalues: the y-values of the points given"""
    
    logxvalues = [ math.log10( val ) for val in xvalues ]
    
    Res = FindBoundaries( logxvalues, yvalues, BPos, Max )
    
    return Res
    

def FindBoundariesLogY( xvalues, yvalues, BPos = True, Max = True ):
    """Find find boundaries around data in log space
    xvalues: the x-values of the points given
    yvalues: the y-values of the points given"""
    
    logyvalues = [ math.log10( val ) for val in yvalues ]
    
    Res = FindBoundaries( xvalues, logyvalues, BPos, Max )
    
    return pow( 10.0, Res[0] ),Res[1]
