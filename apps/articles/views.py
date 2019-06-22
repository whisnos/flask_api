from apps.articles import articles

@articles.route('/')
def index():
	return 'articles'