import check50
import os
import unittest
import sys
import re

def setFromEnv(varname,default=None):
    result = default
    if varname in os.environ:
        result = os.environ[varname]
    return result

grader_dir = setFromEnv("GRADER_DIR","/Users/admin/gitlab/ece551/new-assns/graders")
quiz_name = setFromEnv("QUIZ_NAME","default_quiz")

def firstLetter(line):
    result = ""
    pattern = re.compile(r"[A-Za-z]")
    m = pattern.search(line)
    if m:
        result = m.group().upper()
    return result

def read_answers_file(pathname):
    answers = []
    ansfile = open(pathname, "r")
    lines_remaining = True
    while lines_remaining:
        line = ansfile.readline()
        answer = firstLetter(line)
        if answer != "":
            answers.append(firstLetter(line))
        lines_remaining = line
    ansfile.close()
    return answers

def read_hints_file(pathname):
    hints = []
    if os.path.exists(pathname):
        hintsfile = open(pathname, "r")
        lines_remaining = True
        while lines_remaining:
            line = hintsfile.readline()
            hints.append(line)
            #print("line in hints file",line)
            lines_remaining = line
        hintsfile.close()
    return hints    

def overallGrade(grade):
    print("")
    print("Overall Grade: ",grade)

def plural(count):
    if count > 1:
        return "s"
    else:
        return ""

@check50.check()
def setup():
    """Checking for proper grader setup"""
    if not "GRADER_DIR" in os.environ:
        check50.Failure("It's not you, it's me: Ask the course staff to set the GRADER_DIR env_variable.")
    if not "QUIZ_NAME" in os.environ:
        check50.Failure("It's not you, it's me: Ask the course staff to set the QUIZ_NAME env variable.")

@check50.check(setup)
def exists():
    """Reading your quiz answers from answers.txt"""
    check50.exists("answers.txt")

@check50.check(exists)
def reading_quiz():
    """Check whether answer.txt contents matches quiz answers"""
    # TODO: migrate to /dev/fd/4
    grader_dir = setFromEnv("GRADER_DIR","/Users/admin/gitlab/ece551/new-assns/graders/")
    quiz_name = setFromEnv("QUIZ_NAME","default_quiz")

    print("quiz: ",quiz_name)
    expected = read_answers_file(grader_dir + os.sep + quiz_name + os.sep + "4")
    hints = read_hints_file(grader_dir + os.sep + quiz_name + os.sep + "hints")
    actual = read_answers_file("answers.txt")
    if len(expected) != len(actual):
        help = "Please check your answers file and add the missing entries."
        raise check50.Failure("Your answer file has "+ str(len(actual)) + " answers, but I expected " +str(len(expected)),help=help)
        overallGrade("FAILED")
        sys.exit()
    incorrect = 0
    suggestions = []
    for answer_index in range(len(expected)):
        if actual[answer_index] not in expected[answer_index]:
            incorrect += 1
            # here's the place to add a hint
            if hints:
                suggestions.append(hints[answer_index])
    if incorrect > 0:
            overallGrade("FAILED")
            advice = "You have "+str(incorrect)+" incorrect answer"+plural(incorrect)+".\n"
            if suggestions:
                advice += ''.join(suggestions)
            raise check50.Failure("FAILED",help=advice)
    else:
        print("Your quiz answers are correct.")
        overallGrade("PASSED")

class TestGrader(unittest.TestCase):
    def test_first_letter(self):
        self.assertEqual("A",firstLetter("A\n"))
        self.assertEqual("A",firstLetter("a\n"))
        self.assertEqual("A",firstLetter("3. a\n"))


    def test_read_ch01_rq_answers_file(self):
        answers = read_answers_file(grader_dir + os.sep + "ch01_rq" + os.sep + "4")
        print("test quiz_name",quiz_name)
        print("answers",answers)
        self.assertEqual(answers[0] == "C", True, "Should be True")
        self.assertEqual(answers[1] == "A", True, "Should be True")
        self.assertEqual(answers[2] == "B", True, "Should be True")
        self.assertEqual(answers[3] == "C", True, "Should be True")
        self.assertEqual(answers[4] == "C", True, "Should be True")
        self.assertEqual(answers[5] == "B", True, "Should be True")
        self.assertEqual(answers[6] == "C", True, "Should be True")
        self.assertEqual(answers[7] == "A", True, "Should be True")
        self.assertEqual(answers[8] == "A", True, "Should be True")
        self.assertEqual(answers[9] == "B", True, "Should be True")

    def test_read_student_answers(self):
        actual = read_answers_file("/Users/admin/pjm52_510solns/ch01_rq/student/answers.txt")
        print("actual",actual)
        pass

if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main()

    if len(sys.argv) == 2: # assume first arg is quiz directory name (e.g. ch01_rq)
        quiz_name = sys.argv[1]
        print("main quiz_name",quiz_name)