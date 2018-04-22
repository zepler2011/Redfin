
class House(object):
    """
    House class
    """
    def __init__(
        self,
        street_address=None,
        city=None,
        state=None,
        zip_code=None,
        beds=None,
        baths=None,
        sq_ft=None,
        lot_size=None,
        home_type=None
    ):
        self.street_address=street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.beds = beds
        self.baths = baths
        self.sq_ft = sq_ft
        self.lot_size = lot_size
        self.home_type = home_type
        self.redfin_data = None
        self.redfin_url = None
        return

    def as_dict(self):
        d = {
            'street_address': self.street_address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'beds': self.beds,
            'baths': self.baths,
            'parking': self.parking,
            'parking_type': self.parking_type,
            'sq_ft': self.sq_ft,
            'lot_size': self.lot_size,
            'home_type': self.home_type
        }
        return d

