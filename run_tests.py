import unittest

def run_tests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(test_suite)

    return test_result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    if not success:
        exit(1)
