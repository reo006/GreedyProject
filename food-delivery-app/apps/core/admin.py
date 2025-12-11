from django.contrib import admin
from .models import YourModelName  # ここに管理したいモデルをインポートしてください

@admin.register(YourModelName)  # ここに管理したいモデルを指定してください
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')  # 表示したいフィールドを指定してください
    search_fields = ('field1', 'field2')  # 検索可能なフィールドを指定してください
    list_filter = ('field3',)  # フィルタリング可能なフィールドを指定してください

# 他のモデルがある場合は、同様に@admin.registerを使って登録してください