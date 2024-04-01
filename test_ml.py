from ml import *

def test_fit():
    x = [0,1]
    y = [0,1]
    slope, intercept = fit(x, y)
    assert slope == 9.812037170985635
    assert intercept == 5.175316482607568

def test_probabilities():
    lm = LogisticModel()
    x = [0, 0.2, 0.4, 0.6, 0.8, 1]
    y = [0, 0.2, 0.4, 0.6, 0.8, 1]
    lm.fit(x,y)
    ps = lm.predict_proba(x)
    for p in ps:
        assert p >= 0
        assert p <= 1

def test_predictions():
    lm = LogisticModel()
    x = [0, 0.2, 0.4, 0.6, 0.8, 1]
    lm.slope = 0.5
    lm.intercept = 0.5
    ys = lm.predict(x)
    for y in ys:
        assert (y == 0 or y == 1)