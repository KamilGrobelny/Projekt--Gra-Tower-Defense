MAPS = {
    "Mapa 1": (
        [(x, 2) for x in range(18)] +
        [(18, y) for y in range(2, 4)] +
        [(x, 4) for x in range(18, 2, -1)] +
        [(2, y) for y in range(4, 12)] +
        [(x, 12) for x in range(2,5)] +
        [(5, y) for y in range(12, 6, -1)] +
        [(x, 6) for x in range(5,14)]+
        [(14, y) for y in range(6, 12)]+
        [(x, 12) for x in range(14,20)]

    ),
    "Mapa 2": (
        [(x, 2) for x in range(3)] +
        [(x, x) for x in range(2,8)] +
        [(8,6),(9,5),(10,4),(11,3),(12,2)] +
        [(x, 2) for x in range(13,18)] +
        [(16,3),(15,4),(14,5),(13,6),(12,7)] +
        [(x, 7) for x in range(13,18)] +
        [(17, y) for y in range(8,9)] +
        [(x, 9) for x in range(17,2,-1)] +
        [(3,10),(4,11),(5,12),(6,13),(7,12)] +
        [(x, 11) for x in range(8,18)] +
        [(18,12),(19,13)]
        
    ),
    "Test Mapa":
        [(x, 2) for x in range(5)],

    }