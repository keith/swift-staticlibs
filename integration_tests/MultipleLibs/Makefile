test:
	xcodebuild -sdk iphonesimulator -arch x86_64 SYMROOT=build clean build > /dev/null
	# Get all built files and validate them against expected files
	find build/Debug-iphonesimulator > actual_files.txt
	diff actual_files.txt expected_files.txt
	# Validate the expected modulemaps
	diff build/Debug-iphonesimulator/First.framework/Modules/module.modulemap first.modulemap
	diff build/Debug-iphonesimulator/Second.framework/Modules/module.modulemap second.modulemap
	# Verify Second's symbols are in First
	nm -u build/Debug-iphonesimulator/First.framework/First | grep --silent Second
	nm -U build/Debug-iphonesimulator/MultipleLibs.app/MultipleLibs | grep --silent First
	nm -U build/Debug-iphonesimulator/MultipleLibs.app/MultipleLibs | grep --silent Second
