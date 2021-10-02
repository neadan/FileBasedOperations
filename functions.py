def read_file_bad():
    story_file = open('files/iconic_short_story.txt', 'r')
    story = story_file.read()
    story_file.close() # this is bad because no with
    return story


def read_file_good():
    # with open(r'C:\Users\Tiberiu\PycharmProjects\FileBasedOperations\files\iconic_short_story.txt', 'r') as story_file:
    with open('/files\\iconic_short_story.txt', 'r') as story_file:
        story = story_file.read() # returns a string
    return story


def read_lines(): # returns a list
    with open('files/iconic_short_story.txt', 'r') as story_file:
        story_lines = story_file.readlines() # returns a list
    return story_lines


def read_grades():
    with open('files/grades.txt', 'r') as grades_file:
        grades_lines = grades_file.readlines()  # returns a list
    return grades_lines


def append_grades():
    with open('files/grades.txt', 'a') as grades_file:
        grades_file.write("\nJim,99,Passed")


def overwrite_grades():
    with open('files/grades.txt', 'w') as grades_file:
        grades_file.write("\nJim,99,Passed")