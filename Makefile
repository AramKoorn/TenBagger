release:
	pip install --upgrade setuptools wheel && python3 setup.py sdist bdist_wheel

publish:
	pip install --upgrade twine && twine upload dist/* --skip-existing
