from brand_site.models import PodcastPost
from faker import Faker  
from datetime import datetime

Faker.seed(42)
faker = Faker()

data_lst = []
create_n_data = 3
for _ in range(create_n_data):
    data = {
        'title':faker.text()[:20],
        'description':faker.text(),
        'pod_url':faker.uri(),
        'podcaster':faker.name(),
        # customize datetime(2015, 10, 09, 23, 55, 59, 342380) from int
        'record_stamp':datetime.now()
    }
    curs = PodcastPost.objects.create(**data)
    curs.save()
