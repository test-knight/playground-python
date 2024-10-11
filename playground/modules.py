import converters
from converters import kgs_to_lbs
import utils
from ecommerce import orderstatus

print(converters.lbs_to_kgs(35))
print(kgs_to_lbs(72))

numbers = [11, 2, 2, 1, 0, -1]
print(utils.get_max(numbers))
# print(max(numbers)) //built-in

orderstatus.check_status()
