test:
	xcodebuild -sdk iphonesimulator SYMROOT=build clean build > /dev/null
	# Get all built files and validate them against expected files
	find build/Debug-iphonesimulator > actual_files.txt
	diff actual_files.txt expected_files.txt
	# Validate the expected modulemaps
	diff build/Debug-iphonesimulator/Dependency.framework/Modules/module.modulemap module.modulemap
	# Verify symbols are in the app for both targets
	nm -U build/Debug-iphonesimulator/Extension.appex/Extension | grep --silent Dependency
	nm -U build/Debug-iphonesimulator/ExtensionLibrary.app/ExtensionLibrary | grep --silent Dependency
