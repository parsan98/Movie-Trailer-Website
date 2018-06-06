# the module media contains the class Movie
import media
# the module fresh_tomatoes contains methods to create and display the page
import fresh_tomatoes

# Creating instances for each movie
hp1 = media.Movie("Harry Potter and </br>the Philosopher's Stone",
                  "Harry Potter, an eleven-year-old orphan,"
                  "discovers that he is a wizard and is invited "
                  "to study at Hogwarts.",
                  'https://www.warnerbros.com/sites/default/files/styles/'
                  'key_art_270x400/public/movies/media/browser/'
                  'harry_potter_sorcerers_stone_2016_keyart.jpg?itok=okfyua55',
                  'https://www.youtube.com/watch?v=eKSB0gXl9dw')
hp2 = media.Movie("Harry Potter and </br>the Chamber of Secrets",
                  "A queer creature warns Harry against returning to Hogwarts."
                  "Harry decides to ignore him. When he returns to school, "
                  "he finds himself surrounded in a web of mystery.",
                  'https://i.pinimg.com/originals/fb/7e/e7/'
                  'fb7ee741aa5d3e0b9f3054bef59f75d2.jpg',
                  "https://www.youtube.com/watch?v=uU-ET1FAv3Y")
hp3 = media.Movie("Harry Potter and </br>the Prisoner of Azkaban",
                  "In his third year at Hogwarts, Harry Potter learns that "
                  "Sirius Black has escaped from the Azkaban prison"
                  " and is planning to kill him.",
                  'https://vignette.wikia.nocookie.net/harrypotter/'
                  'images/c/c4/7VTALkqjG40vby3uVIsp03d7yXy.jpg',
                  "https://www.youtube.com/watch?v=lAxgztbYDbs")
hp4 = media.Movie("Harry Potter and </br>the Goblet of Fire",
                  "In his fourth year at Hogwarts, Harry is unwittingly "
                  "selected to "
                  "compete in the inter-school Triwizard Tournament."
                  "Meanwhile, "
                  "the wizarding world remains unaware of"
                  "the ominous rise of dark forces.",
                  'https://cdn.movieweb.com/img.teasers.posters/'
                  'FIlrIpnlFW5Vpl_357_a/'
                  'Harry-Potter-And-The-Goblet-Of-Fire.jpg',
                  "https://www.youtube.com/watch?v=PFWAOnvMd1Q")
hp5 = media.Movie("Harry Potter and </br>the Order of the Phoenix",
                  "Harry Potter and Dumbledore's warning about the return of "
                  "Lord Voldemort is not heeded by "
                  "the wizard authorities who, "
                  " in turn, look to undermine Dumbledore's"
                  "authority at Hogwarts.",
                  'https://vignette.wikia.nocookie.net/'
                  'harrypotter/images/7/70/'
                  'Harry_Potter_and_the_Order_of_the_Phoenix.jpg',
                  "https://www.youtube.com/watch?v=E9ZXOdGdTFI")
hp6 = media.Movie("Harry Potter and </br>the Half-Blood Prince",
                  "Dumbledore and Harry Potter learn more about "
                  "Voldemort's past "
                  "and his rise to power. Meanwhile, Harry stumbles "
                  "upon an old potions textbook "
                  "belonging to a person calling himself the"
                  "Half-Blood Prince.",
                  'https://vignette.wikia.nocookie.net/harrypotter/images/'
                  'd/db/Ron_and_Lavender_-_HBP_poster.jpg',
                  "https://www.youtube.com/watch?v=JYLdTuL9Wjw")
hp7 = media.Movie("Harry Potter and </br>the Deathly Hallows </br>- Part 1",
                  "To assure Lord Voldemort's death and "
                  "to protect mankind from evil, "
                  "Harry, Ron and Hermione must find"
                  "and destroy each Horcrux. "
                  "Voldemort's henchmen, the Death Eaters, "
                  "give the trio a tough time.",
                  'https://i0.wp.com/www.itncart.com/wp-content/uploads/'
                  '2016/04/Harry-Potter-and-the-Deathly-Hollows'
                  '-Part-1-Poster.jpg',
                  "https://www.youtube.com/watch?v=MxqsmsA8y5k")
hp8 = media.Movie("Harry Potter and </br>the Deathly Hallows </br>- Part 2",
                  "Harry, Ron and Hermione face a race against time to "
                  "destroy the remaining horcruxes. "
                  "Meanwhile, the students and teachers "
                  "unite to defend Hogwarts against Lord Voldemort"
                  "and his minions.",
                  "https://images-na.ssl-images-amazon.com/images/"
                  "I/51cbzR1Ji0L.jpg",
                  "https://www.youtube.com/watch?v=5NYt1qirBWg")
# Storing all movies in a list
movies = [
    hp1, hp2, hp3,
    hp4, hp5, hp6,
    hp7, hp8
]

# Calling the function that creates and displays the page
fresh_tomatoes.open_movies_page(movies)
