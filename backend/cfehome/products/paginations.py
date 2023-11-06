from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class MyPaginatin(PageNumberPagination):
    page_size = 5                                          # Page size per page 
    page_size_query_param = 'records'                      # For client to send page_size it can not be greater than max page size
    max_page_size = 5                                      # Maximum page size
    page_query_param = 'p'                                 # 'p' denotes the page number query in url/endpoint
    
class MyLimitPagination(LimitOffsetPagination):
    default_limit = 4
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 6