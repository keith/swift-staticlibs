test:
	xcodebuild -destination generic/platform=iOS -arch armv7s SYMROOT=build clean build > /dev/null
	# Get all built files and validate them against expected files
	find build/Debug-iphoneos > actual_files.txt
	diff actual_files.txt expected_files.txt
	# Validate expected modulemap
	diff build/Debug-iphoneos/SimpleFramework.framework/Modules/module.modulemap expected.modulemap
	# Validate Swift symbols exist in the product
	nm -U build/Debug-iphoneos/SimpleFramework.framework/SimpleFramework \
		| grep --silent FooBar
