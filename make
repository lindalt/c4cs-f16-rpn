basic_test:
	python3 -m unittest

coverage_test:
	coverage run test_rpn.py
	coverage report
