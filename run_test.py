from run import isTriangle,ThirdAngle

def test_isTriangle():
    assert isTriangle(1,2,3) == False
    assert isTriangle(3.2,4,5)
    assert isinstance(isTriangle(0,0,0), bool)

def test_ThirdAngle():
    assert ThirdAngle(60,60) == 60