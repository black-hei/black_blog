from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Black_Blog'
    site_title = 'Black_Blog 管理后台'
    site_url = '首页'


custom_site = CustomSite(name='custom_admin')


