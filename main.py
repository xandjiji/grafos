from functions import *

office = read_weighted_adjacency_matrix('thurman_office.txt')
MST_office = prim_mst(office)
officek2 = groups(MST_office, 2)
officek5 = groups(MST_office, 5)

draw(office, True, 'grafo office')
draw(MST_office, True, 'MST de office')
draw(officek2, True, 'office em 2 grupos')
draw(officek5, True, 'office em 5 grupos')