#!/usr/bin/env python

import argparse
import json

from redfin import RedFin
from house import House
from listing import Listing

def get_args():
    parser = argparse.ArgumentParser(description='Search Redfin for houses.')
    parser.add_argument('--filter', dest='filter', default=None, action='store',
                        help='path to json file for search filter')
    args = parser.parse_args()
    return args

def main():
    a = get_args()
    filter = None
    if a.filter:
        # XXX change to logging
        print 'search filter present'
        filter = json.load(open(a.filter))

    redfin = RedFin()
    redfin.use_proxies = False
    redfin.get_search_results(filter=filter)

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

if __name__ == "__main__":
    main()

