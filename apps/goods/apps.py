from django.apps import AppConfig


class GoodsConfig(AppConfig):
    name = 'goods'
    verbose_name = "商品"

    def ready(self):
        import goods.signals