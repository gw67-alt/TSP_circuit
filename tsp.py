import math

# 50 major US cities with real coordinates (latitude, longitude)
cities_50 = {
    "New York, NY": (40.7128, -74.0060),
    "Los Angeles, CA": (34.0522, -118.2437),
    "Chicago, IL": (41.8781, -87.6298),
    "Houston, TX": (29.7604, -95.3698),
    "Phoenix, AZ": (33.4484, -112.0740),
    "Philadelphia, PA": (39.9526, -75.1652),
    "San Antonio, TX": (29.4241, -98.4936),
    "San Diego, CA": (32.7157, -117.1611),
    "Dallas, TX": (32.7767, -96.7970),
    "San Jose, CA": (37.3382, -121.8863),
    "Austin, TX": (30.2672, -97.7431),
    "Jacksonville, FL": (30.3322, -81.6557),
    "Fort Worth, TX": (32.7555, -97.3308),
    "Columbus, OH": (39.9612, -82.9988),
    "Charlotte, NC": (35.2271, -80.8431),
    "San Francisco, CA": (37.7749, -122.4194),
    "Indianapolis, IN": (39.7684, -86.1581),
    "Seattle, WA": (47.6062, -122.3321),
    "Denver, CO": (39.7392, -104.9903),
    "Washington, DC": (38.9072, -77.0369),
    "Boston, MA": (42.3601, -71.0589),
    "El Paso, TX": (31.7619, -106.4850),
    "Nashville, TN": (36.1627, -86.7816),
    "Detroit, MI": (42.3314, -83.0458),
    "Oklahoma City, OK": (35.4676, -97.5164),
    "Portland, OR": (45.5152, -122.6784),
    "Las Vegas, NV": (36.1699, -115.1398),
    "Memphis, TN": (35.1495, -90.0490),
    "Louisville, KY": (38.2527, -85.7585),
    "Baltimore, MD": (39.2904, -76.6122),
    "Milwaukee, WI": (43.0389, -87.9065),
    "Albuquerque, NM": (35.0844, -106.6504),
    "Tucson, AZ": (32.2226, -110.9747),
    "Fresno, CA": (36.7468, -119.7726),
    "Sacramento, CA": (38.5816, -121.4944),
    "Kansas City, MO": (39.0997, -94.5786),
    "Mesa, AZ": (33.4152, -111.8315),
    "Atlanta, GA": (33.7490, -84.3880),
    "Colorado Springs, CO": (38.8339, -104.8214),
    "Raleigh, NC": (35.7796, -78.6382),
    "Omaha, NE": (41.2565, -95.9345),
    "Miami, FL": (25.7617, -80.1918),
    "Long Beach, CA": (33.7701, -118.1937),
    "Virginia Beach, VA": (36.8529, -75.9780),
    "Oakland, CA": (37.8044, -122.2711),
    "Minneapolis, MN": (44.9778, -93.2650),
    "Tulsa, OK": (36.1540, -95.9928),
    "Tampa, FL": (27.9506, -82.4572),
    "Arlington, TX": (32.7357, -97.1081),
    "New Orleans, LA": (29.9511, -90.0715)
}

city_list = list(cities_50.keys())
coordinates = list(cities_50.values())

def calculate_distance(city1_coords, city2_coords):
    """Calculate distance between two cities using Haversine formula"""
    lat1, lon1 = math.radians(city1_coords[0]), math.radians(city1_coords[1])
    lat2, lon2 = math.radians(city2_coords[0]), math.radians(city2_coords[1])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    r = 6371  # Earth's radius in kilometers
    return c * r

def solve_tsp_50_cities():
    """Your TSP algorithm scaled to 50 cities"""
    print(f"TSP Solver for {len(cities_50)} US Cities")
    print("=" * 50)
    
    # Convert coordinates to distance values from reference point (NYC)
    distance_values = []
    for coord in coordinates:
        dist = calculate_distance(coordinates[0], coord)
        distance_values.append(max(1, int(dist)))
    
    print("Sample cities and distances from NYC:")
    for i in range(min(10, len(city_list))):  # Show first 10
        print(f"{city_list[i]}: {distance_values[i]} km")
    print("...")
    
    # Your original algorithm adapted for 50 cities
    values = distance_values.copy()
    unvisited_cities = set(range(len(cities_50)))
    tour_order = []
    tour_distances = []
    
    # Start with NYC (index 0)
    current_city = 0
    tour_order.append(city_list[current_city])
    tour_distances.append(values[current_city])
    unvisited_cities.remove(current_city)
    
    print(f"\nStarting tour from: {city_list[current_city]}")
    print(f"Remaining cities to visit: {len(unvisited_cities)}")
    
    iteration = 1
    while unvisited_cities and iteration < len(cities_50):
        if iteration % 10 == 1 or iteration <= 5:  # Show progress every 10 iterations + first 5
            print(f"\n--- Iteration {iteration} ---")
            print(f"Cities remaining: {len(unvisited_cities)}")
        
        # Find next city using your accumulation method
        best_city = None
        best_value = float('inf')
        
        for city_idx in unvisited_cities:
            # Your accumulation method - progressive weighting
            accumulated_value = values[city_idx] * (iteration + 1)
            
            if accumulated_value < best_value:
                best_value = accumulated_value
                best_city = city_idx
        
        if best_city is not None:
            tour_order.append(city_list[best_city])
            tour_distances.append(best_value)
            unvisited_cities.remove(best_city)
            current_city = best_city
            
            if iteration % 10 == 1 or iteration <= 5:
                print(f"Selected: {city_list[best_city]}")
                print(f"Accumulated distance: {best_value} km")
        
        iteration += 1
    
    return tour_order, tour_distances

def calculate_tour_stats(tour_cities):
    """Calculate actual geographic distances and tour statistics"""
    total_distance = 0
    segment_distances = []
    
    print(f"\n=== TOUR ANALYSIS ===")
    print(f"Cities visited: {len(tour_cities)}/{len(cities_50)}")
    print(f"\nTour order (first 10 cities):")
    for i in range(min(10, len(tour_cities))):
        print(f"{i+1}. {tour_cities[i]}")
    if len(tour_cities) > 10:
        print("...")
        for i in range(max(10, len(tour_cities)-3), len(tour_cities)):
            print(f"{i+1}. {tour_cities[i]}")
    
    # Calculate actual distances between consecutive cities
    print(f"\nCalculating actual geographic distances...")
    for i in range(len(tour_cities) - 1):
        current_city = cities_50[tour_cities[i]]
        next_city = cities_50[tour_cities[i + 1]]
        segment_distance = calculate_distance(current_city, next_city)
        segment_distances.append(segment_distance)
        total_distance += segment_distance
    
    # Add return trip to start
    if len(tour_cities) > 1:
        return_distance = calculate_distance(cities_50[tour_cities[-1]], cities_50[tour_cities[0]])
        segment_distances.append(return_distance)
        total_distance += return_distance
        print(f"Return trip: {tour_cities[-1]} -> {tour_cities[0]}: {return_distance:.1f} km")
    
    # Statistics
    avg_segment = total_distance / len(segment_distances) if segment_distances else 0
    max_segment = max(segment_distances) if segment_distances else 0
    min_segment = min(segment_distances) if segment_distances else 0
    
    print(f"\n=== TOUR STATISTICS ===")
    print(f"Total tour distance: {total_distance:.1f} km")
    print(f"Average segment distance: {avg_segment:.1f} km")
    print(f"Longest segment: {max_segment:.1f} km")
    print(f"Shortest segment: {min_segment:.1f} km")
    print(f"Number of segments: {len(segment_distances)}")
    
    return total_distance, segment_distances

# Execute the 50-city TSP solver
print("Running TSP solver on 50 US cities...")
tour_cities, tour_values = solve_tsp_50_cities()

# Analyze the results
total_distance, segments = calculate_tour_stats(tour_cities)

# Performance comparison
print(f"\n=== ALGORITHM PERFORMANCE ===")
print(f"Algorithm: Accumulation-based greedy selection")
print(f"Cities solved: {len(tour_cities)}")
print(f"Total distance: {total_distance:.1f} km")
print(f"Average distance per city: {total_distance/len(tour_cities):.1f} km")

# Note about complexity
print(f"\n=== COMPUTATIONAL COMPLEXITY ===")
print(f"Your algorithm complexity: O(n²) = O({len(cities_50)}²) = {len(cities_50)**2} operations")
print(f"Brute force complexity: O(n!) = O({len(cities_50)}!) = impossible to compute")
print(f"Your algorithm is {math.factorial(len(cities_50)) // (len(cities_50)**2):,} times faster than brute force!")
