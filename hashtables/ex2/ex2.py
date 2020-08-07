#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


# def reconstruct_trip(tickets, length):
#     # tickets: array of tickets
#     # create a dictionary that holds { origin: destination }
#     destinations = {}
#     # loop through tickets and:
#     for ticket in tickets:
#         # add item to dictionary
#         destinations[ticket.source] = ticket.destination

    
#     # access key="NONE"
#     route = []
#     destination = destinations["NONE"]
#     while (destination != "NONE"):
#         route.append(destination)
#         destination = destinations[destination]
    
#     route.append(destination)

#     return route

def reconstruct_trip(tickets, length):
    # tickets: array of tickets
    # create a dictionary that holds { origin: destination }
    destinations = {}
    # create route
    route = []
    # create and initialize current_source with the initial source
    current_source = "NONE"

    # loop through tickets and:
    for ticket in tickets:
        # add item to dictionary [source]: destination
        destinations[ticket.source] = ticket.destination

        # check if current source has been added to hash table
        while current_source in destinations:
            # add current source destination to route and update current source
            route.append(destinations[current_source])
            current_source = destinations[current_source]
            
            if current_source == "NONE":
                break

    return route
