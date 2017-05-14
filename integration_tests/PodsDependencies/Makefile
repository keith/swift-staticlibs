OLD_PWD = $(PWD)

test:
	rm -rf build
	# Uncomment when updating CocoaPods logic, otherwise Pods are checked in
	# bundle check || bundle install
	# bundle exec pod install
	# bundle exec ruby delete_embed.rb
	xcodebuild -workspace PodsDependencies.xcworkspace -scheme PodsDependencies -sdk iphonesimulator -derivedDataPath build clean build > /dev/null
	# Validate produced .app
	cd $(shell ./build_dir.sh)/PodsDependencies.app && \
		find . > $(OLD_PWD)/actual_files.txt
	diff actual_files.txt expected_files.txt
	# Check for the Dependency's symbols in the produced app binary
	nm -U $(shell ./build_dir.sh)/PodsDependencies.app/PodsDependencies | grep --silent doStuff
