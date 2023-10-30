from rest_framework.throttling import UserRateThrottle                                                                                      
from rest_framework.response import Response

class ScoperThrot(UserRateThrottle):
    scope = 'saqib'
    