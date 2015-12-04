import weather
import NN as nn 
get_pm5_prediction = nn.setup()
# SAMPLE usage, Delete before using it as library
def predictPollution(precipitation_prob, relative_humidity, temp, wind_direction, wind_speed):
    O3PreictedVal = 5.03704930e+01 + (precipitation_prob * 9.66895471e-02) + (relative_humidity * -2.99780572e-03) + (temp * -2.26017118e-01) + (wind_direction * -8.96663780e-03) + (wind_speed *  9.98339351e+00)
    PM25PredictedVal = 1.36006991e+01 +  (temp * -9.32461073e-02)  +   (wind_direction * -3.35510810e-04) +   (wind_speed * -7.50369156e-01)
    nnPrediction = get_pm5_prediction(TMP = temp,WDIR = wind_direction,WSPD = wind_speed)
    #3.6 is average
    if abs(nnPrediction - PM25PredictedVal) > 7.2:
        if abs(nnPrediction - 3.6) > abs(PM25PredictedVal - 3.6):
            return O3PreictedVal, PM25PredictedVal
        else:
            return O3PreictedVal, nnPrediction
    return O3PreictedVal, (nnPrediction + PM25PredictedVal)/2
        
    
def pollutionAPi(lat, lon, offset):
    return predictPollution(*weather.get_weather(lat, lon, offset))

#offset -> [0,2], 0 means now, 1 means one hour from now, and 2 means 2 hour from now
print pollutionAPi(51.0123, 0.3, 0)