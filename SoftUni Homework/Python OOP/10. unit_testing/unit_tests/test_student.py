from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student('Ivan', {'maths': [6, 6, 6], 'chemistry': [2, 3, 4]})

    def test_correct_initialization(self):
        self.assertEqual('Ivan', self.student.name)
        self.assertEqual({'maths': [6, 6, 6], 'chemistry': [2, 3, 4]}, self.student.courses)

        self.student = Student('Ivan')
        self.assertEqual({}, self.student.courses)

    def test_correct_adding_notes(self):
        expected_message = 'Course already added. Notes have been updated.'
        self.assertEqual(expected_message, self.student.enroll('maths', [6, 5, 5]))
        self.assertEqual({'maths': [6, 6, 6, 6, 5, 5], 'chemistry': [2, 3, 4]}, self.student.courses)

    def test_correct_creation_on_course(self):
        self.assertEqual(self.student.enroll('geography', 5, ''), 'Course and course notes have been added.')
        self.assertEqual({'maths': [6, 6, 6], 'chemistry': [2, 3, 4], 'geography': 5}, self.student.courses)

        self.assertEqual(self.student.enroll('history', 5, 'Y'), 'Course and course notes have been added.')
        self.assertEqual({'maths': [6, 6, 6], 'chemistry': [2, 3, 4], 'geography': 5, 'history': 5},
                         self.student.courses)

        self.assertEqual(self.student.enroll('politics', 6, 'some_message'), 'Course has been added.')
        self.assertEqual({'maths': [6, 6, 6], 'chemistry': [2, 3, 4], 'geography': 5, 'history': 5, 'politics': []},
                         self.student.courses)

    def test_correct_adding_notes_2(self):
        self.assertEqual('Notes have been updated', self.student.add_notes('maths', 4))
        self.assertEqual({'maths': [6, 6, 6, 4], 'chemistry': [2, 3, 4]}, self.student.courses)

    def test_raise_error_if_course_not_found_adding(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('unknown_course', 123)

        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_correct_remove_on_course(self):
        self.assertEqual('Course has been removed', self.student.leave_course('chemistry'))
        self.assertEqual({'maths': [6, 6, 6]}, self.student.courses)

    def test_raise_error_if_course_not_found_removing(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('unknown_course')

        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))


if __name__ == '__main__':
    main()
