test: clean test_unit test_integration

test_integration:
	$(MAKE) -C integration_tests/SimpleFramework test
	$(MAKE) -C integration_tests/SimpleApp test
	$(MAKE) -C integration_tests/MultipleLibs test
	$(MAKE) -C integration_tests/MultipleDependentLibs test
	$(MAKE) -C integration_tests/MultipleArchitectures test
	$(MAKE) -C integration_tests/ExtensionLibrary test
	$(MAKE) -C integration_tests/PodsDependencies test

test_unit:
	python -m unittest discover -s tests

clean:
	find . -name "*.pyc" -delete
	find . -name "build" -type d | xargs rm -rf
