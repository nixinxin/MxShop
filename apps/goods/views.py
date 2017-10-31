# from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
# from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from django_filters.rest_framework import DjangoFilterBackend
from .models import Goods, GoodsCategory, Banner, HotSearchWords

from rest_framework.authentication import TokenAuthentication
from goods.filters import GoodsFilter
from .serializers import GoodsSerializer, CategorySerializer, BannerSerializer, IndexGategorySerializer, \
    HotWordsSerializer
from rest_framework_extensions.cache.mixins import CacheResponseMixin

# Create your views here.


# class GoodsListView(APIView):
#     """
#     descriptions: list all  goods, or create a net goods
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#     # def post(self, request, format=None):
#     #     serializer = GoodsSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data, status=status.HTTP_200_OK)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """
#     descriptions: list all  goods, or create a net goods
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


# class GoodsListView(generics.ListAPIView):
#     """
#     descriptions: list all  goods, or create a net goods
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination


class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品列表数据,该注释直接会在docs文档中生成相关说明
    """
    # throttle_classes = (UserRateThrottle, AnonRateThrottle)
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # authentication_classes = (TokenAuthentication, )  # 针对特定的接口认证

    # django不会提醒补齐filter_backends,要记住
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # filter_fields = ("name", 'shop_price') 已经自定义 GoodsFilter就不用filter_fields
    filter_class = GoodsFilter
    # 模糊搜索
    # '^' 以什么开头
    # '=' 精确搜索
    # '@' 全文搜索。（目前只支持Django的MySQL后端。）
    # '$' 正则表达式搜索。
    search_fields = ('name', 'goods_brief', 'goods_desc',)
    ordering_fields = ('sold_num', 'add_time')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # 自定义返回query,过滤
    # def get_queryset(self):
    #     price_min = self.request.query_params.get('price_min', 0)
    #     if price_min:
    #         self.queryset = self.queryset.filter(shop_price__gt=int(price_min))
    #     return self.queryset


class GategoryViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class HotSearchsViewset(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer


class BannerViewset(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取轮播图
    """
    queryset = Banner.objects.all().order_by('index')
    serializer_class = BannerSerializer


class IndexCategoryViewset(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=['生鲜食品', '酒水饮料'])
    serializer_class = IndexGategorySerializer
