from brand_site.models import VideoPost
from faker import Faker  

Faker.seed(42)
faker = Faker()

data_lst = []
create_n_data = 3
for _ in range(create_n_data):
    data = {
        'title':faker.text()[:20],
        'description':faker.text(),
        'vdo_url':faker.uri(),
        'video_stamp':'video stamp'
    }
    curs = VideoPost.objects.create(**data)
    curs.save()
