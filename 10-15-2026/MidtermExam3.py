def make_movie(movie_title, movie_director, movie_star, movie_runtime=90):
    return {
        'title': movie_title,
        'director': movie_director,
        'star': movie_star,
        'length': movie_runtime,
    }


while True:
    movie_title = input("What is the title of the movie (or q for quit)? ")

    if movie_title == 'q':
        break

    movie_director = input("Who is the director of the movie? ")
    movie_star = input("Who is the star of the movie? ")
    movie_runtime = input("What is the runtime of the movie in minutes? ")

    movie_dict = make_movie(movie_title, movie_director, movie_star, movie_runtime)
    print(movie_dict)