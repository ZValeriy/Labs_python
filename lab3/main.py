from getID_class import *
from get_friends import *
from countBdate import *

makegist(
    count_bdate(
        Friends(
            GetUserID(
                input()
            ).get_data()
        ).make_list()
    )
)

