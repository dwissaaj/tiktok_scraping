from TikTokApi import TikTokApi


api = TikTokApi.get_instance()

count = 300

tiktoks = api.by_username("jne_id", count=count)



