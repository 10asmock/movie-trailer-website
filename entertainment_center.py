import fresh_tomatoes
import media 

# Displays all movies which will be presented on the HTML web page.
# If desired, create a movie variable accompanied by the movie name,
# rating, brief description, poster URL and trailer URL to add a new
# movie instance. Be sure to add your new movie to list movies.
silent_hill = media.Movie(
  "Silent Hill",
  "Rated R",
  "A woman must save her daughter from Silent Hill.",
  "https://www.movieposter.com/posters/archive/main/34/MPW-17029",
  "https://www.youtube.com/watch?v=f5mT5LhbRJw")

avengers = media.Movie(
  "The Avengers",
  "Rated PG-13",
  "The superhero Avengers must rescue Earth from Loki.",
  "https://tinyurl.com/ybsvn9wy",
  "https://www.youtube.com/watch?v=eOrNdBpGMv8")
                         
star_wars = media.Movie(
  "Star Wars IV",
  "Rated PG",
  "The Rebel Alliance must save the galaxy from the evil Galactic Empire.",
  "https://tinyurl.com/y78fqazj",
  "https://www.youtube.com/watch?v=9gvqpFbRKtQ")

baby_driver = media.Movie(
  "Baby Driver",
  "Rated R",
  "A getaway driver must escape a life of crime.",
  "https://tinyurl.com/y7pdg95s",
  "https://www.youtube.com/watch?v=zTvJJnoWIPk")

john_wick_2 = media.Movie(
  "John Wick: Chapter 2",
  "Rated R",
  "A hitman goes on the run after a bounty is placed on his head.",
  "https://tinyurl.com/ydhlrc2b",
  "https://www.youtube.com/watch?v=ChpLV9AMqm4")

saving_private_ryan = media.Movie(
  "Saving Private Ryan",
  "Rated R",
  "A group of U.S. soldiers must find Private James Ryan.",
  "https://tinyurl.com/yb3sgfjb",
  "https://www.youtube.com/watch?v=RYID71hYHzg")
                        
movies = [silent_hill, 
          avengers, 
          star_wars, 
          baby_driver, 
          john_wick_2, 
          saving_private_ryan
         ]

#imports generated web page to display listed movies
fresh_tomatoes.open_movies_page(movies)

