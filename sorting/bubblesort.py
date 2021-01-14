import time
import logging
logging.basicConfig(filename="testlog.log", level=logging.DEBUG)
        
def bubbleSort(arr):
    
    for k in range(len(arr)-1):
        i=k
        j=i+1
        #print(arr)
        while len(arr)>j>i:
            if arr[i]>arr[j]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
                logging.info("info message")
            i+=1
            j+=1
    
    return arr
    
    
# arr=[8,2,6,4,5]
# out=bubbleSort(arr)
#print(out)


A = [11111, 16, 25, 33, 39, 50, 57, 61, 62, 63, 73, 74, 78, 85, 90, 94, 97, 101, 102, 105, 132, 133, 134, 135, 136, 138, 142, 143, 144, 145, 146, 147, 149, 150, 153, 156, 157, 166, 167, 168, 175, 177, 178, 180, 181, 185, 189, 190, 192, 199, 205, 208, 214, 215, 220, 221, 223, 227, 228, 234, 241, 243, 258, 262, 271, 273, 276, 279, 280, 283, 284, 287, 288, 291, 296, 301, 302, 305, 307, 310, 315, 326, 327, 336, 337, 339, 341, 342, 347, 353, 359, 362, 364, 365, 376, 377, 378, 379, 381, 382, 383, 387, 392, 404, 405, 406, 421, 425, 428, 430, 436, 445, 450, 452, 458, 462, 469, 471, 475, 476, 492, 494, 499, 5020, 501, 504, 517, 519, 520, 531, 533, 535, 536, 541, 549, 553, 557, 563, 566, 572, 576, 584, 587, 589, 601, 604, 605, 606, 610, 614, 615, 617, 622, 625, 629, 631, 633, 639, 6241, 642, 644, 660, 666, 667, 674, 675, 678, 683, 687, 695, 698, 700, 705, 706, 709, 718, 723, 727, 734, 738, 739, 743, 748, 749, 750, 754, 758, 763, 765, 776, 778, 779, 781, 782, 785, 786, 788, 792, 793, 800, 803, 806, 810, 815, 816, 820, 823, 828, 829, 831, 834, 836, 841, 844, 846, 847, 853, 856, 857, 867, 870, 876, 880, 889, 892, 894, 898, 899, 900, 901, 904, 905, 912, 914, 925, 929, 941, 946, 953, 959, 960, 963, 966, 967, 968, 973, 979, 982, 986, 989, 999, 1000, 1003, 1004, 1010, 1013, 1014, 1016, 1021, 1031, 1049, 1053, 1054, 1056, 1057, 1065, 1067, 1068, 1072, 1081, 1083, 1087, 1090, 1091, 1094, 1098, 1099, 1105, 1112, 1130, 1131, 1133, 1135, 1138, 1139, 1140, 1146, 1147, 1151, 1152, 1158, 1160, 1162, 1163, 1164, 1168, 1172, 1174, 1176, 1177, 1181, 1185, 1189, 1192, 1197, 1201, 1206, 1208, 1215, 1216, 1222, 1225, 1244, 1248, 1250, 1256, 1257, 1261, 1262, 1265, 1266, 1271, 1277, 1280, 1285, 1288, 1289, 1290, 1292, 1296, 1301, 1314, 1315, 1319, 1321, 1333, 1334, 1336, 1340, 1341, 1343, 1344, 1347, 1351, 1352, 1355, 1357, 1364, 1375, 1376, 1377, 1380, 1382, 1383, 1384, 1387, 1392, 1407, 1410, 1412, 1415, 1423, 1428, 1434, 1436, 1440, 1455, 1462, 1464, 1466, 1476, 1478, 1480, 1485, 1487, 1488, 1490, 1493, 1494, 1495, 1498, 1500, 1509, 1512, 1513, 1515, 1520, 1521, 1534, 1540, 1541, 1542, 1544, 1546, 1551, 1558, 1560, 1561, 1563, 1566, 1567, 1568, 1577, 1582, 1585, 1590, 1591, 1592, 1594, 1596, 1611, 1616, 1617, 1618, 1619, 1620, 1623, 1626, 1641, 1643, 1647, 1651, 1654, 1655, 1661, 1662, 1665, 1667, 1668, 1681, 1682, 1691, 1692, 1693, 1703, 1707, 1710, 1716, 1719, 1723, 1731, 1738, 1741, 1742, 1751, 1753, 1759, 1775, 1777, 1778, 1780, 1783, 1788, 1797, 1800, 1803, 1806, 1810, 1818, 1826, 1827, 1828, 1831, 1838, 1840, 1842, 1844, 1848, 1851, 1853, 1854, 1858, 1861, 1866, 1868, 1871, 1873, 1878, 1887, 1889, 1901, 1902, 1903, 1916, 1918, 1939, 1943, 1948, 1951, 1954, 1959, 1962, 1968, 1970, 1972, 1980, 1983, 1995, 1997, 1999]

start_time = time.time()
output=bubbleSort(A)
print("Total Time %s" %(time.time() - start_time))
