from math import cos, asin, sqrt
import sys

# function to calculate distance between two points based on their latitude and longitude
# thanks to https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
def distance(c1, c2):
    ''' function to calculate distance between two points based on their latitude and longitude '''
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((c2.lat - c1.lat) * p)/2 + cos(c1.lat * p) * cos(c2.lat * p) * (1 - cos((c2.lon - c1.lon) * p)) / 2
    return int(12742 * asin(sqrt(a)))

# function to verify if two nodes is equal
def is_same_node(c1, c2):
    ''' function to verify if two nodes is equal '''
    return c1.lat==c2.lat and c1.lon==c2.lon

# class to represent coordinate of city with lat(latitude) and lon(longitude)
class Coord:
    ''' class to represent coordinate of city with lat(latitude) and lon(longitude) '''
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# class to represent each node of graph
class City:
    ''' class to represent each node(city) of graph '''
    def __init__(self, coord, name):
        self.coord = coord
        self.name = name
        self.costG = 0
        self.costH = 0
        self.costF = 0
        self.parent = None
        self.neighbors = None

    def add_neighbors(self, neighbors):
        self.neighbors = neighbors

# class to represent the link between two cities with cost which is the distance(integer) in this case study
class Bow:
    ''' class to represent the link between two cities with cost which is the distance(integer) in this case study '''
    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost

class AStar:
    ''' class which implement a star algorithm '''
    current_coord = Coord(0,0)
    open_set = dict()
    close_set = dict()

    def __init__(self, map_graph, source_coord, target_coord):
        super().__init__()
        self.map_graph = map_graph
        self.source_coord = source_coord
        self.target_coord = target_coord
        
        self.current_coord = self.source_coord

    # compute g value for any node
    def compute_g(self, node):
        ''' compute g value for any node
            g value is the cost from source to node(variable passed in parameter) '''
        if is_same_node(node.coord, self.source_coord):
            return 0
        ci = 0
        for c in node.neighbors:
            if is_same_node(node.parent, c.dest):
                ci = c.cost
                break
        return ci + self.compute_g(self.map_graph[node.parent])

    # validate neighbors of current node
    def validate_neighbors(self):
        ''' validate neighbors of current node '''
        
        for bow in self.map_graph[self.current_coord].neighbors:

            if bow.dest in self.close_set:
                continue

            tmp_node = self.map_graph[bow.dest]
            tmp_node.parent = self.current_coord
            tmp_node.costG = self.compute_g(tmp_node)

            if tmp_node.costH == 0:
                tmp_node.costH = distance(bow.dest, self.target_coord)
                self.map_graph[bow.dest].costH = tmp_node.costH
            tmp_node.costF = tmp_node.costG + tmp_node.costH
            
            if tmp_node.coord in self.open_set:
                if tmp_node.costF < self.open_set[tmp_node.coord].costF:
                    # print('adding '+tmp_node.name+' to open set...')
                    self.open_set[tmp_node.coord] = tmp_node
            else:
                # print('adding '+tmp_node.name+' to open set...')
                self.open_set[tmp_node.coord] = tmp_node
        
    # look for the good neighbor of current node and return it
    def searching_good_neighbor(self):
        ''' look for the good neighbor of current node and return it '''

        min_cost = sys.maxsize
        min_coord = Coord(0,0)
        # print('==================')
        for key, value in self.open_set.items():
            # print('City: '+value.name+' => G: '+str(value.costG)+' => H: '+str(value.costH)+' => F: '+str(value.costF))
            if min_cost > value.costF:
                min_cost = value.costF
                min_coord = key

        # print('==================')
        return min_coord

    def rebuild_route(self):
        ''' function which rebuild the path from target to source'''
        tmp = self.close_set[self.target_coord]
        print(tmp.name+' => ', end='')

        while tmp.parent is not None:
            tmp = self.close_set[tmp.parent]
            print(tmp.name+' => ', end='')

    def a_star(self):
        ''' a star algorithm main function '''
        # initialize current_coord, open_set and close_set
        self.map_graph[self.source_coord].costF = self.map_graph[self.source_coord].costH = distance(self.source_coord, self.target_coord)
        self.close_set[self.current_coord] = self.open_set[self.current_coord] = self.map_graph[self.current_coord]

        while not is_same_node(self.current_coord, self.target_coord) and self.open_set:
            # print('\nNew iteration...')

            # call validate_neighbors function
            self.validate_neighbors()
            # call searching_good_neighbor function and change current_coord value
            self.current_coord = self.searching_good_neighbor()
            # print('\ncurrent city '+self.open_set[self.current_coord].name+'\n')

            # add new current_coord to close_set and delete it from open_set
            self.close_set[self.current_coord] = self.open_set[self.current_coord]
            del self.open_set[self.current_coord]
        
        if is_same_node(self.current_coord, self.target_coord):
            print('We found a route.')
            self.rebuild_route()
        else:
            print('We did not find any route.')