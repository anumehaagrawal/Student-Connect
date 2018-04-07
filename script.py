from dashboard.analytics import generate_ratings
from dashboard.models import College

colleges = College.objects().all()
for col in range(len(colleges)):
    review = colleges[col].reviews
    rating = generate_ratings(review)
    colobj = colleges[col]
    colobj.ratings = rating
    colobj.save()