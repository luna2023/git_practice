destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

print(get_destination_index("Los Angeles, USA"))
print(get_destination_index("Paris, France"))
# print(get_destination_index("Hyderabad, India"))
print(get_destination_index("São Paulo, Brazil"))

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

attractions = [[], [], [], [], []]
# attractions = [[] for i in range(len(destinations))]
# attractions = []
# for i in range(len(destinations)):
#   attractions.append([])

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
  except:
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
print(attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
# print(attractions)
 
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  # print(destination_index, "test") 
  attractions_in_city = attractions[destination_index]
  # print(attractions_in_city, "test1")
  attractions_with_interest = []
  for i in attractions_in_city:
    possible_attraction = []
    attraction_tags = []
    possible_attraction.append(i)
    # print(possible_attraction, "test2")
    attraction_tags.append (i[1])
    # print(attraction_tags, "test3")
    for interest in interests:
      for tag in attraction_tags:
        try :
          tag_index = tag.index(interest)
          # print(tag_index, "test4")
        except:
          continue
        attractions_with_interest.append(possible_attraction[0][0])
        # print(attractions_with_interest)
        # print(possible_attraction)
    
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  for x in traveler_attractions:
    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler[1] + " : " + x
    #print(interests_string)
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]) 
print(smills_france)








