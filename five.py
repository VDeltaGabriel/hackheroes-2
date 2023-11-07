import numpy as np
from sklearn.linear_model import LinearRegression

training_set_inputs = np.array([
    [708, 1415, 2, 29, 55, 29, 9899, 32, 0],
    [312, 1230, 1, 18, 62, 16, 108107, 17, 1],
    [1228, 1645, 4, -1, 70, -4, 12299, -3, 1],
    [519, 1510, 1, 24, 60, 20, 115108, 26, 0],
    [1003, 1455, 3, 16, 65, 13, 12299, 15, 0],
    [225, 1140, 4, -4, 75, -6, 115110, -8, 1],
    [815, 1025, 2, 26, 58, 25, 9899, 28, 0],
    [430, 1335, 1, 21, 63, 18, 108107, 20, 0],
    [124, 955, 4, -2, 70, -4, 12299, -5, 0],
    [1103, 1550, 3, 13, 68, 11, 100115, 12, 1],
    [627, 1705, 2, 30, 55, 26, 115108, 32, 0],
    [910, 1420, 3, 17, 62, 17, 12299, 18, 0],
    [319, 1240, 1, 17, 65, 16, 9899, 18, 0],
    [1215, 935, 4, -3, 70, -4, 115110, -6, 1],
    [808, 1600, 2, 27, 60, 25, 108107, 28, 1],
    [406, 1115, 1, 20, 62, 18, 12299, 22, 0],
    [130, 1410, 4, -1, 68, -4, 108107, -3, 0],
    [1125, 1730, 3, 12, 65, 11, 12299, 11, 0],
    [602, 1355, 2, 25, 60, 26, 9899, 26, 0],
    [917, 1545, 3, 18, 63, 17, 115108, 20, 1],
    [210, 1040, 4, -4, 68, -6, 115110, -7, 1],
    [1210, 1635, 4, -2, 70, -4, 108107, -4, 1],
    [531, 1220, 1, 23, 62, 20, 9899, 26, 0],
    [1023, 1425, 3, 15, 65, 13, 12299, 16, 0],
    [306, 1115, 1, 19, 62, 16, 115108, 20, 0],
    [712, 1055, 2, 27, 60, 29, 9899, 30, 1],
    [128, 1405, 4, -3, 70, -4, 108107, -4, 1],
    [1118, 1550, 3, 13, 68, 11, 100115, 12, 0],
    [615, 1340, 2, 25, 60, 26, 115108, 28, 1],
    [922, 1625, 3, 17, 63, 17, 12299, 18, 1],
    [403, 1010, 1, 18, 65, 18, 9899, 20, 1],
    [828, 1115, 2, 28, 58, 25, 9899, 30, 0],
    [222, 1500, 4, -5, 70, -6, 108107, -7, 1],
    [1205, 1450, 4, -1, 68, -4, 12299, -3, 0],
    [508, 1730, 1, 21, 65, 20, 100115, 19, 1],
    [1015, 1245, 3, 16, 68, 14, 12299, 16, 1],
    [331, 920, 1, 17, 62, 16, 115108, 18, 1],
    [703, 1610, 2, 28, 55, 29, 115108, 30, 0],
    [218, 1140, 4, -3, 70, -6, 108107, -6, 1],
    [1220, 1555, 4, 0, 70, -4, 12299, -4, 1],
    [524, 1640, 1, 23, 60, 20, 9899, 26, 0],
    [1030, 1425, 3, 15, 65, 13, 108107, 15, 0],
    [326, 1015, 1, 16, 65, 16, 100115, 14, 0],
    [723, 1150, 2, 29, 55, 28, 115108, 32, 0],
    [118, 1320, 4, -4, 68, -4, 12299, -6, 1],
    [1110, 1710, 3, 11, 70, 11, 12299, 10, 1],
    [620, 1245, 2, 27, 58, 26, 108107, 28, 0],
    [915, 1610, 3, 17, 63, 17, 115108, 18, 1],
    [412, 1125, 1, 19, 62, 18, 9899, 20, 0],
    [831, 1500, 2, 27, 60, 25, 9899, 30, 1],
    [214, 1405, 4, -2, 68, -6, 108107, -5, 1],
    [1225, 1620, 4, 0, 70, -4, 115110, -3, 1],
    [515, 1035, 1, 22, 65, 20, 12299, 24, 0],
    [1027, 1230, 3, 14, 68, 13, 100115, 14, 1],
    [322, 1530, 1, 18, 62, 16, 9899, 19, 0],
    [730, 1345, 2, 30, 55, 29, 115108, 33, 1],
    [115, 1140, 4, -5, 70, -4, 108107, -7, 1],
    [1105, 1455, 3, 12, 70, 11, 12299, 11, 0],
    [610, 1600, 2, 28, 58, 26, 9899, 31, 0],
    [907, 1255, 3, 18, 63, 17, 115108, 20, 0],
    [424, 1020, 1, 20, 62, 18, 9899, 21, 1],
    [812, 1505, 2, 26, 60, 25, 108107, 28, 1],
    [206, 1720, 4, -6, 70, -6, 115110, -8, 1],
    [1201, 1235, 4, -2, 68, -4, 12299, -4, 1],
    [504, 1540, 1, 21, 65, 20, 100115, 20, 1],
    [1019, 1050, 3, 15, 65, 13, 108107, 15, 0],
    [317, 1615, 1, 17, 62, 16, 115108, 18, 0],
    [718, 1445, 2, 29, 55, 29, 9899, 32, 0],
    [105, 1300, 4, -6, 68, -4, 12299, -8, 1],
    [1128, 1745, 3, 11, 70, 11, 12299, 10, 1]
])
training_set_outputs = np.array([[24, 20, 25, 22, 19, 25, 20, 19, 22, 21, 20, 20, 18, 25, 22, 19, 23, 20, 18, 20, 24, 20, 19, 20, 18, 24, 22, 20, 25, 23, 20, 22, 25, 22, 22, 23, 21, 19, 24, 22, 19, 20, 21, 17, 24, 22, 20, 21, 20, 21, 23, 26, 20, 22, 20, 21, 24, 21, 19, 20, 22, 23, 26, 24, 22, 20, 20, 18, 25, 23]]).T

#Bezchmurne - bc (98 99 w ascii) 
#Lekki deszcz - lk (108 107 w ascii )
#Słonecznie - sl (115 108 w ascii)
#Zachmurzenie - zc (122 99 w ascii)
#Śnieg - sn ( 115 110 w ascii)
#Deszcz - ds (100 115 w ascii)

#Lato-1
#Wiosna-2
#Jesień-3
#Zima-4

#tak-1
#nie-0


#Data (mm-dd)
#     Godzina (hh-mm)
#    pora roku
#   temperatura
#    wilgotność
#  średnia temperatura w miesiącu
#      pogoda w ascii
#      odczuwalna temperatura
#        czy lubie ciepło


# ogólny wzór neurona
# model.fit(training_set_inputs, training_set_outputs)
#new_input = np.array([[1220, 2330, 4, -14, 67, -12, 115100, -18, 1]])
#predicted_output = model.predict(new_input)
#print("Przewidziana wartość dla nowego inputu:")
#print(predicted_output)

model = LinearRegression()

#dla wszystkich neuronów set testowy to: [1220, 2330, 4, -14, 67, -12, 115100, -18, 1]
#w postaci jednego neuronu wychodziło: 23.86306044
def weathertemp():
    model.fit(training_set_inputs[4, 7], training_set_outputs)
    new_input = np.array([[-14, 115100]])
    predicted_output1 = model.predict(new_input)
    print("[WeatherTemp] Przewidziana wartość dla nowego inputu:")
    print(predicted_output1)

def datetime():
    model.fit(training_set_inputs[1, 2], training_set_outputs)
    new_input = np.array([[1220, 2330]])
    predicted_output2 = model.predict(new_input)
    print("[DateTime] Przewidziana wartość dla nowego inputu:")
    print(predicted_output2)

def prefertempfeel():
    model.fit(training_set_inputs[4, 7], training_set_outputs)
    new_input = np.array([[-14, 115100]])
    predicted_output3 = model.predict(new_input)
    print("[PreferTempFeel] Przewidziana wartość dla nowego inputu:")
    print(predicted_output3)

def wtdt():
    model.fit(training_set_inputs[predicted_output1, predicted_output2], training_set_outputs)
    new_input = np.array([[predictedoutput1, predictedoutput2]])
    predicted_output4 = model.predict(new_input)
    print("[PreferTempFeel] Przewidziana wartość dla nowego inputu:")
    print(predicted_output4)