import unittest
import main

class TestMain(unittest.TestCase):
    def test_main_function_exists(self):
        self.assertTrue(callable(main.run), "The main function should be callable.")

    def test_main_runs_without_error(self):
        try:
            main.run("text","exit")
        except Exception as e:
            self.fail(f"The main function raised an exception: {e}")

        


if __name__ == '__main__':
    unittest.main()