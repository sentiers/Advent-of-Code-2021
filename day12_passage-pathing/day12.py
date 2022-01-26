from collections import defaultdict

def count_paths(cave_graph):
    paths = []
    for cave in cave_graph['start']:  # start from 'start'
        get_path(cave_graph, cave, ['start'], paths)
    return len(paths)

def get_path(cave_graph, cave, path, paths):
    if cave == 'end':
        path.append(cave)
        paths.append(path)
    elif cave != 'start':
        if not cave.islower() or cave not in path:
            path.append(cave)
            for cave in cave_graph[cave]: # start from current cave
                get_path(cave_graph, cave, path.copy(), paths)

def count_paths_2(cave_graph):
    paths = []
    for cave in cave_graph['start']:  # start from 'start'
        get_path_2(cave_graph, cave, ['start'], paths, False)
    return len(paths)

def get_path_2(cave_graph, cave, path, paths, been_twice):
    if cave == 'end':
        path.append(cave)
        paths.append(path)
    elif cave != 'start':
        if not been_twice or not cave.islower() or cave not in path:
            if cave.islower() and cave in path: # if already visited small cave
                been_twice = True
            path.append(cave)
            for cave in cave_graph[cave]: # start from current cave
                get_path_2(cave_graph, cave, path.copy(), paths, been_twice)

def calc():
    cave_graph = defaultdict(list)
    with open('cave-system.txt') as file:
        data = file.read().splitlines()
    for caves in data:
        origin, destination = caves.split('-')
        cave_graph[origin].append(destination)
        cave_graph[destination].append(origin)
    # How many paths through this cave system are there that visit small caves at most once?
    print('Paths when visiting small caves at most once: {} paths'.format(count_paths(cave_graph.copy())))
    # how many paths through this cave system are there?
    print('Paths when visiting one small cave at most twice: {} paths'.format(count_paths_2(cave_graph.copy())))


calc()
