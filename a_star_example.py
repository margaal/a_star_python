import a_star_module as Astar


# Examples data
arad = Astar.City(Astar.Coord(46.18333, 21.31667), 'Arad')
zerind = Astar.City(Astar.Coord(46.623518, 21.516981), 'Zerind')
sibiu = Astar.City(Astar.Coord(45.797391, 24.151920), 'Sibiu')
oradea = Astar.City(Astar.Coord(47.06667, 21.93333), 'Oradea')
fagaras = Astar.City(Astar.Coord(45.844943, 24.96667), 'Fagaras')
bucharest = Astar.City(Astar.Coord(44.432250, 26.106260), 'Bucharest')
urziceni = Astar.City(Astar.Coord(44.716670, 26.633330), 'Urziceni')
vaslui = Astar.City(Astar.Coord(46.63333, 27.73333), 'Vaslui')
hirsova = Astar.City(Astar.Coord(44.68574, 27.94819), 'Hirsova')
giurgiu = Astar.City(Astar.Coord(43.88333, 25.96667), 'Giurgiu')
craiova = Astar.City(Astar.Coord(44.31667, 23.796561), 'Craiova')
drobeta = Astar.City(Astar.Coord(44.625783, 22.653197), 'Drobeta')
mehadia = Astar.City(Astar.Coord(44.903767, 22.363817), 'Mehadia')
lugoj = Astar.City(Astar.Coord(45.68861, 21.90306), 'Lugoj')
timisoara = Astar.City(Astar.Coord(45.75372, 21.22571), 'Timisoara')
rimnicu_vilcea = Astar.City(Astar.Coord(45.103173, 24.36667), 'Rimnicu Vilcea')
pitesti = Astar.City(Astar.Coord(44.857234, 24.86667), 'Pitesti')

# Add Neighbors for each Astar.City
arad.add_neighbors([Astar.Bow(zerind.coord, 75), Astar.Bow(timisoara.coord, 118), Astar.Bow(sibiu.coord, 140)])
zerind.add_neighbors([Astar.Bow(arad.coord, 75), Astar.Bow(oradea.coord, 71)])
sibiu.add_neighbors([Astar.Bow(oradea.coord, 151), Astar.Bow(arad.coord, 140), Astar.Bow(fagaras.coord, 99), Astar.Bow(rimnicu_vilcea.coord, 80)])
oradea.add_neighbors([Astar.Bow(zerind.coord, 71), Astar.Bow(sibiu.coord, 151)])
fagaras.add_neighbors([Astar.Bow(sibiu.coord, 99), Astar.Bow(bucharest.coord, 211)])
bucharest.add_neighbors([Astar.Bow(giurgiu.coord, 90), Astar.Bow(fagaras.coord, 211), Astar.Bow(pitesti.coord, 101), Astar.Bow(urziceni.coord, 85)])
urziceni.add_neighbors([Astar.Bow(vaslui.coord, 142), Astar.Bow(hirsova.coord, 98), Astar.Bow(bucharest.coord, 85)])
vaslui.add_neighbors([Astar.Bow(urziceni.coord, 142)])
hirsova.add_neighbors([Astar.Bow(urziceni.coord, 98)])
giurgiu.add_neighbors([Astar.Bow(bucharest.coord, 90)])
craiova.add_neighbors([Astar.Bow(pitesti.coord, 138), Astar.Bow(rimnicu_vilcea.coord, 146), Astar.Bow(drobeta.coord, 120)])
drobeta.add_neighbors([Astar.Bow(craiova.coord, 120), Astar.Bow(mehadia.coord, 75)])
mehadia.add_neighbors([Astar.Bow(drobeta.coord, 75), Astar.Bow(lugoj.coord, 70)])
lugoj.add_neighbors([Astar.Bow(mehadia.coord, 70), Astar.Bow(timisoara.coord, 111)])
timisoara.add_neighbors([Astar.Bow(lugoj.coord, 111), Astar.Bow(arad.coord, 118)])
rimnicu_vilcea.add_neighbors([Astar.Bow(pitesti.coord, 97), Astar.Bow(craiova.coord, 146), Astar.Bow(sibiu.coord, 80)])
pitesti.add_neighbors([Astar.Bow(rimnicu_vilcea.coord, 97), Astar.Bow(craiova.coord, 138), Astar.Bow(bucharest.coord, 101)])

# dict to represent my graph
town_graph = {
    arad.coord : arad,
    zerind.coord : zerind,
    oradea.coord : oradea,
    sibiu.coord : sibiu,
    fagaras.coord : fagaras,
    bucharest.coord : bucharest,
    urziceni.coord : urziceni,
    vaslui.coord : vaslui,
    hirsova.coord : hirsova,
    giurgiu.coord : giurgiu,
    craiova.coord : craiova,
    drobeta.coord : drobeta,
    mehadia.coord : mehadia,
    lugoj.coord : lugoj,
    timisoara.coord : timisoara,
    rimnicu_vilcea.coord : rimnicu_vilcea,
    pitesti.coord : pitesti,
}


# call to a_star function
astar = Astar.AStar(map_graph=town_graph, source_coord=arad.coord, target_coord=giurgiu.coord)
astar.a_star()