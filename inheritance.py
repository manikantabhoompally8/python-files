# Parent Class
class Course:
    def __init__(self, course_name, price):
        self.course_name = course_name
        self.price = price

    def show_course(self):
        print("Course Name:", self.course_name)
        print("Price:", self.price)


# Child Class
class ProgrammingCourse(Course):
    def __init__(self, course_name, price, language, duration):
        super().__init__(course_name, price)  # using super()
        self.language = language
        self.duration = duration

    def show_programming_course(self):
        self.show_course()  # calling parent method
        print("Language:", self.language)
        print("Duration:", self.duration)
        print("----------------------")


# Creating 2 programming courses
c1 = ProgrammingCourse("Python Course", 5000, "Python", "3 Months")
c2 = ProgrammingCourse("Java Course", 7000, "Java", "4 Months")

# Printing details
c1.show_programming_course()
c2.show_programming_course()








# Parent Class 1
class Camera:
    def __init__(self, camera_mp):
        self.camera_mp = camera_mp

    def take_photo(self):
        print(f"Taking photo with {self.camera_mp}MP camera")


# Parent Class 2
class MusicPlayer:
    def __init__(self, brand):
        self.brand = brand

    def play_music(self):
        print(f"Playing music using {self.brand} sound system")


# Child Class
class SmartPhone(Camera, MusicPlayer):
    def __init__(self, model_name, camera_mp, brand):
        # Calling both parent constructors using super() chain
        Camera.__init__(self, camera_mp)
        MusicPlayer.__init__(self, brand)

        self.model_name = model_name

    def show_details(self):
        print(f"Model: {self.model_name}")
        print(f"Camera: {self.camera_mp}MP")
        print(f"Music Brand: {self.brand}")

# Smartphone 1
phone1 = SmartPhone("iPhone 15", 48, "Dolby")
phone1.show_details()
phone1.take_photo()
phone1.play_music()

print("------")

# Smartphone 2
phone2 = SmartPhone("Samsung S23", 108, "Sony")
phone2.show_details()
phone2.take_photo()
phone2.play_music()
