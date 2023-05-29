import folium
import random

max_distance = 1

teams = [
    {"name": "Team 1", "capacity": 100},
    {"name": "Team 2", "capacity": 100},
    {"name": "Team 3", "capacity": 100},
    {"name": "Team 4", "capacity": 100},
    {"name": "Team 5", "capacity": 100},
    {"name": "Team 6", "capacity": 100},
    {"name": "Team 7", "capacity": 100},
    {"name": "Team 8", "capacity": 100},
    {"name": "Team 9", "capacity": 100},
    {"name": "Team 10", "capacity": 100},
    {"name": "Team 11", "capacity": 100},
    {"name": "Team 12", "capacity": 100},
]

work_to_be_done = [
    {"name": "Lisbon", "capacity": 20, "x":  38.736946, "y":  -9.142685},
    #porto
    {"name": "Porto", "capacity": 20, "x": 41.157944, "y": -8.629105},
    #braga
    {"name": "Braga", "capacity": 20, "x": 41.545448, "y": -8.426507},
    #coimbra
    {"name": "Coimbra", "capacity": 20, "x": 40.203314, "y": -8.410257},
    #aveiro
    {"name": "Aveiro", "capacity": 20, "x": 40.644269, "y": -8.645535},
    #faro
    {"name": "Faro", "capacity": 20, "x": 37.019354, "y": -7.930439},
    #bragança
    {"name": "Bragança", "capacity": 20, "x": 41.805817, "y": -6.757711},
    #guarda
    {"name": "Guarda", "capacity": 20, "x": 40.537328, "y": -7.267261},
    #leiria
    {"name": "Leiria", "capacity": 20, "x": 39.743621, "y": -8.80705},
    #santarém
    {"name": "Santarém", "capacity": 20, "x": 39.236626, "y": -8.685602},
    #viana do castelo
    {"name": "Viana do Castelo", "capacity": 20, "x": 41.693692, "y": -8.832149},
    #vila real
    {"name": "Vila Real", "capacity": 20, "x": 41.297415, "y": -7.745331},
    #viseu
    {"name": "Viseu", "capacity": 20, "x": 40.657777, "y": -7.913866},
    #setubal
    {"name": "Setúbal", "capacity": 20, "x": 38.5244, "y": -8.8882},
    #evora
    {"name": "Évora", "capacity": 20, "x": 38.5667, "y": -7.9},
    #beja
    {"name": "Beja", "capacity": 20, "x": 38.0151, "y": -7.8631},
    #castelo branco
    {"name": "Castelo Branco", "capacity": 20, "x": 39.8222, "y": -7.4904},
    #portalegre
    {"name": "Portalegre", "capacity": 20, "x": 39.2975, "y": -7.4304},
    # almada
    {"name": "Almada", "capacity": 20, "x": 38.678, "y": -9.161},
    # amadora
    {"name": "Amadora", "capacity": 20, "x": 38.7597, "y": -9.2397},
    # matosinhos
    {"name": "Matosinhos", "capacity": 20, "x": 41.1825, "y": -8.6892},
    # agualva-cacem
    {"name": "Agualva-Cacém", "capacity": 20, "x": 38.767, "y": -9.298},
    # guimaraes
    {"name": "Guimarães", "capacity": 20, "x": 41.4425, "y": -8.2917},
    # valenca
    {"name": "Valença", "capacity": 20, "x": 42.0294, "y": -8.6439},
    # mourao
    {"name": "Mourão", "capacity": 20, "x": 38.3833, "y": -7.35},
    # portel
    {"name": "Portel", "capacity": 20, "x": 38.3, "y": -7.7},
    # loule
    {"name": "Loulé", "capacity": 20, "x": 37.1372, "y": -8.0197},
    # tavira
    {"name": "Tavira", "capacity": 20, "x": 37.1333, "y": -7.65},
    # albufeira
    {"name": "Albufeira", "capacity": 20, "x": 37.1333, "y": -8.25},
    # chaves
    {"name": "Chaves", "capacity": 20, "x": 41.7333, "y": -7.4667},
    # val pacos
    {"name": "Valpaços", "capacity": 20, "x": 41.6, "y": -7.3},
    # mirandela
    {"name": "Mirandela", "capacity": 20, "x": 41.4833, "y": -7.1833},
    # Gaviao
    {"name": "Gavião", "capacity": 20, "x": 39.4667, "y": -7.9333},
    # olhao
    {"name": "Olhão", "capacity": 20, "x": 37.0333, "y": -7.8333},
    # portimao
    {"name": "Portimão", "capacity": 20, "x": 37.1333, "y": -8.5333},
    # Lagos
    {"name": "Lagos", "capacity": 20, "x": 37.1, "y": -8.6667},
    # silves
    {"name": "Silves", "capacity": 20, "x": 37.1833, "y": -8.4333},
    # sintra
    {"name": "Sintra", "capacity": 20, "x": 38.8, "y": -9.3833},
    # cascais
    {"name": "Cascais", "capacity": 20, "x": 38.7, "y": -9.4167},
    # barreiro
    {"name": "Barreiro", "capacity": 20, "x": 38.6667, "y": -9.0667},
    # amora
    {"name": "Amora", "capacity": 20, "x": 38.6167, "y": -9.1167},
    # alcobaca
    {"name": "Alcobaça", "capacity": 20, "x": 39.55, "y": -8.9833},
    # valenca
    {"name": "Valença", "capacity": 20, "x": 42.0294, "y": -8.6439},
    # paredes de coura
    {"name": "Paredes de Coura", "capacity": 20, "x": 41.9167, "y": -8.5667},


]

# function to reorder work to be done by distance to 0,0
def reorder_work(work_to_be_done):
    # initialize the reordered work to be done
    reordered_work_to_be_done = []
    # for each task
    for task in work_to_be_done:
        # calculate the distance between the task and 0,0
        distance = abs(task["x"]) + abs(task["y"])
        # append the distance to the task
        task["distance"] = distance
        # append the task to the reordered work to be done
        reordered_work_to_be_done.append(task)
    # sort the reordered work to be done by distance
    reordered_work_to_be_done = sorted(
        reordered_work_to_be_done, key=lambda i: i["distance"]
    )
    return reordered_work_to_be_done

#function to calculate the middle point from a list of tasks
def middle_point(tasks):
    # initialize the middle point
    middle_point = {"x": 0, "y": 0}
    # for each task
    for task in tasks:
        # update the middle point
        middle_point["x"] = middle_point["x"] + task["x"]
        middle_point["y"] = middle_point["y"] + task["y"]
    # divide the middle point by the number of tasks
    middle_point["x"] = middle_point["x"] / len(tasks)
    middle_point["y"] = middle_point["y"] / len(tasks)
    return middle_point

# function to find the closest task, given a list of tasks
def closest_task(tasks, work_to_be_done):
    task = middle_point(tasks)
    # initialize the closest task
    closest_task = None
    # initialize the closest distance
    closest_distance = None
    # for each task
    for task_to_be_done in work_to_be_done:
        # calculate the distance between task and middle point of task already scheduled
        distance = abs(task["x"] - task_to_be_done["x"]) + abs(
            task["y"] - task_to_be_done["y"]
        )
        # if the distance is closer than the closest distance
        if closest_distance == None or distance < closest_distance:
            # update the closest task
            closest_task = task_to_be_done
            # update the closest distance
            closest_distance = distance
    # if the closest distance is bigger than the max distance
    if closest_distance > max_distance:
        return None
    
    return closest_task

# function to attribute tasks to teams based on capacity
def schedule_work(teams, work_to_be_done):
    schedule_work = []

    for team in teams:
        team_tasks = []
        team_capacity = team["capacity"]
         # if team dont have any task assigned get the first task
        if team_tasks == []:
            # if there is no more work to be done
            if work_to_be_done == []:
                # break the loop
                break
            # pop the first taks from the list
            task = work_to_be_done.pop(0)
            # append the task to the team tasks
            team_tasks.append(task)
            team_capacity = team_capacity - task["capacity"]
        # while the team has capacity
        while team_capacity >= 0:
            # if there is no more work to be done
            if work_to_be_done == []:
                # break the loop
                break
            # get the closest task
            task = closest_task(team_tasks, work_to_be_done)
            if task == None:
                break
            # pop the task from the list
            work_to_be_done.remove(task)
            # append the task to the team tasks
            team_tasks.append(task)
            # update the team capacity
            team_capacity = team_capacity - task["capacity"]
        # append the team tasks to the schedule work
        schedule_work.append({"team":team['name'],"unused_capacity":team_capacity,"schedule":team_tasks})
    return schedule_work

# crete a map image with the tasks and teams assigned as zones
def create_map(schedule_work):
    # create a map
    m = folium.Map(location=[48.856613, 2.352222], zoom_start=5)
    # for each team
    for team in schedule_work:
        # create a list of coordinates
        coordinates = []
        # for each task
        for task in team["schedule"]:
            # append the coordinates to the list
            coordinates.append([task["x"], task["y"]])
        # create a polygon with the coordinates
        #random color
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))       
        folium.Polygon(
            locations=coordinates,
            color=color,
            fill=True,
            fill_color="blue",
            fill_opacity=0.25,
        ).add_to(m)
    # save the map as an html file
    m.save("map.html")

# reorder the work to be done to optimize the routes
work_to_be_done = reorder_work(work_to_be_done)
# schedule the work to be done and map the routes
schedule = schedule_work(teams, work_to_be_done)
create_map(schedule)
# print the schedule
print(schedule)
# print unscheduled work
print(work_to_be_done)
