from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination             # added for pagination logic  


class PostLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 10
	max_limit = 10 

class PostPageNumberPagination(PageNumberPagination):
	page_size = 5                                                                         # 5 posts displayed per page .. can use previous and next links to view posts in DRF