from redfin import RedFin

redfin = RedFin()
redfin.use_proxies = False
redfin.get_search_results()
redfin.get_one_property_data()
