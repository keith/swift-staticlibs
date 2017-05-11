test:
	xcodebuild -sdk iphonesimulator -arch i386 SYMROOT=build clean build > /dev/null
	# Get all built files and validate them against expected files
	find build/Debug-iphonesimulator > actual_files.txt
	diff actual_files.txt expected_files.txt
	# Validate expected modulemap
	diff build/Debug-iphonesimulator/SimpleFramework.framework/Modules/module.modulemap expected.modulemap
	# Validate Swift symbols exist in the app
	nm -U build/Debug-iphonesimulator/SimpleApp.app/SimpleApp | grep --silent FooBar
