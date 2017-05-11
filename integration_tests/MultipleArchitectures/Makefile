test:
	xcodebuild -sdk iphonesimulator SYMROOT=build clean build > /dev/null
	# Get all built files and validate them against expected files
	find build/Debug-iphonesimulator > actual_files.txt
	diff actual_files.txt expected_files.txt
	# Validate the expected modulemaps
	diff build/Debug-iphonesimulator/First.framework/Modules/module.modulemap first.modulemap
	diff build/Debug-iphonesimulator/Second.framework/Modules/module.modulemap second.modulemap
	# Verify Second's symbols are in First for both architectures
	nm -u -arch=i386 build/Debug-iphonesimulator/First.framework/First | grep --silent Second
	nm -u -arch=x86_64 build/Debug-iphonesimulator/First.framework/First | grep --silent Second
	# Verify symbols are in the app for both architectures
	nm -U -arch=i386 build/Debug-iphonesimulator/MultipleArchitectures.app/MultipleArchitectures | grep --silent First
	nm -U -arch=x86_64 build/Debug-iphonesimulator/MultipleArchitectures.app/MultipleArchitectures | grep --silent First
	nm -U -arch=i386 build/Debug-iphonesimulator/MultipleArchitectures.app/MultipleArchitectures | grep --silent Second
	nm -U -arch=x86_64 build/Debug-iphonesimulator/MultipleArchitectures.app/MultipleArchitectures | grep --silent Second
