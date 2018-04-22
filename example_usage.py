from redfin import RedFin
from house import House
from listing import Listing

redfin = RedFin()
redfin.use_proxies = False
redfin.get_search_results()

r_data = redfin.get_one_property_data()
h = House(street_address = r_data['street_address'],
          city = r_data['address_locality'],
          state = r_data['address_region'],
          zip_code = r_data['postal_code'],
          beds = r_data['beds'],
          baths = r_data['baths'],
          sq_ft = r_data['sqFt'],
          lot_size = None,
          home_type = 'sfh')
l = Listing(house = h)
