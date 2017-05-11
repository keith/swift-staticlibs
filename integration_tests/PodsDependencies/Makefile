test:
	rm -rf build
	bundle check || bundle install
	bundle exec pod install
	# Delete the embed frameworks phase
	bundle exec ruby delete_embed.rb
	xcodebuild -workspace PodsDependencies.xcworkspace -scheme PodsDependencies -sdk iphonesimulator -derivedDataPath build clean build > /dev/null
	# Validate produced .app
	find build/Products/Debug-iphonesimulator/PodsDependencies.app > actual_files.txt
	diff actual_files.txt expected_files.txt
	# Check for the Dependency's symbols in the produced app binary
	nm -U build/Products/Debug-iphonesimulator/PodsDependencies.app/PodsDependencies | grep --silent doStuff
