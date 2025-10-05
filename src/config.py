# config.py
import math


#NUM_CELLS = [64, 100, 256, 529, 1024]  # Different grid sizes for experiments

#default G = 256
NUM_CELLS = [250]


COMBO = [
    # (100, 20),
    # (200, 20),
    # (500, 20),
    # # # #(1000, 10),
    # # # #(1000, 15),
    (1000, 20),
    # #(1000, 50),
    # (5000, 20)
]

GAMMAS = [1]  # example values for g


DATASET_NAMES = [
    "1994_FIFA_World_Cup_squads",
    "List_of_Phi_Beta_Sigma_chapters",
    "2013–14_Tulsa_Golden_Hurricane_men's_basketball_team",
    "1998_FIFA_World_Cup_squads",
    "2002_FIFA_World_Cup_squads",
    "2010_FIFA_World_Cup_squads",
    "2012–13_Dayton_Flyers_men's_basketball_team",
    "2012–13_UMass_Minutemen_basketball_team",
    "2013–14_Oregon_Ducks_men's_basketball_team",
    "2013–14_Tulsa_Golden_Hurricane_men's_basketball_team",
    "List_of_Harvard_University_people",
]


DBPEDIA_DATASET_NAMES = [
    "1994_FIFA_World_Cup_squads",
    "List_of_Phi_Beta_Sigma_chapters",
    "2013–14_Tulsa_Golden_Hurricane_men's_basketball_team",
    "1998_FIFA_World_Cup_squads",
    "2002_FIFA_World_Cup_squads",
    "2010_FIFA_World_Cup_squads",
    "2012–13_Dayton_Flyers_men's_basketball_team",
    "2012–13_UMass_Minutemen_basketball_team",
    "2013–14_Oregon_Ducks_men's_basketball_team",
    "2013–14_Tulsa_Golden_Hurricane_men's_basketball_team",
    "List_of_Harvard_University_people",
]

YAGO_DATASET_NAMES = [
    "Narita_International_Airport",
    "Akai",
    "Haneda_Airport",
    "Chanai",
    "Kazan_metropolitan_area",
    "Empire_of_Japan",
    "Nagareyama__Chiba",
    "Hamura__Tokyo",
    "Fussa__Tokyo",
    "Kashiwanoha",
    "Greater_Tokyo_Area",
    "Tobu_Museum",
    "Shitamachi_Museum",
    "Yamakita__Kanagawa",
    "Kaisei__Kanagawa",
    "Yachiyo__Chiba",
    "Sakura__Chiba",
    "Tako__Chiba",
    "Yotsukaido__Chiba",
    "Kyonan__Chiba",
    "Salt_Creek__South_Australia",
    "Itaga",
    "Wellington__South_Australia",
    "Bel_Ami",
    "Île_de_la_Cité",
    "Musée_du_Louvre",
    "Galerie_de_paléontologie_et_d_anatomie_comparée",
    "Musée_Rodin",
]

SIMULATED_DATASETS = [
    
]

'''

    
    
(500, 10),
    (500, 15),
    (500, 50),
"1998_FIFA_World_Cup_squads",
    "2002_FIFA_World_Cup_squads",
    "2010_FIFA_World_Cup_squads",
    "2012–13_Dayton_Flyers_men's_basketball_team",
    "2012–13_UMass_Minutemen_basketball_team",
    "2013–14_Oregon_Ducks_men's_basketball_team",
    "2013–14_Tulsa_Golden_Hurricane_men's_basketball_team",
    "List_of_Harvard_University_people",

#ddefault K combo
#COMBO = [(500, 20)]

COMBO = [
    (1000, 20),
]

(100, 20),
    (200, 20),
    (500, 20),
    (1000, 20),
    (2000, 20)

    
(1000, 20),
   
    
(100, 20),
    (200, 20),
    (500, 20),
    (1000, 20),
    
COMBO = [
    (500, 10),
    (500, 15),
    (500, 50),
]

COMBO = [
    (100, 50),
    (200, 50),
    (500, 50), 
    (1000, 50),
    (2000, 50),
]

DBPEDIA_DATASET_NAMES = [
    "dbpedia_1994_FIFA_World_Cup_squads",
    "dbpedia_1998_FIFA_World_Cup_squads",
    "dbpedia_2002_FIFA_World_Cup_squads",
    "dbpedia_2012–13_Dayton_Flyers_men's_basketball_team",
    "dbpedia_2012–13_UMass_Minutemen_basketball_team",
    "dbpedia_2013–14_Oregon_Ducks_men's_basketball_team",
]


'''
# Generate GRID_RANGE dynamically based on NUM_CELLS
def get_grid_range_for_cells(num_cells: int, cell_size: float = 1.0) -> tuple:
    G = int(math.sqrt(num_cells))
    return (0, G * cell_size)

CELL_SIZE = 1.0
GRID_RANGES = {g: get_grid_range_for_cells(g, CELL_SIZE) for g in NUM_CELLS}
