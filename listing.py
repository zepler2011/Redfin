
class Listing(object):
    """
    Listing class
    """
    def __init__(
        self,
        house=None,
        list_price=None,
        days_on_market=None,
        status=None,
        mls_id=None,
        open_house_date=None
    ):
        """ reserve open house details, zestimate
        """
        self.house = house
        self.list_price = list_price
        #self.zestimate = zestimate
        self.days_on_market = days_on_market
        #self.original_list_price = original_list_price
        self.status = status
        self.mls_id = mls_id
        self.open_house_date = open_house_date
        #self.open_house_start_time = open_house_start_time
        #self.open_house_end_time = open_house_end_time
        return

