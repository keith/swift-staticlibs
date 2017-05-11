require 'xcodeproj'

main_project = Xcodeproj::Project.open('PodsDependencies.xcodeproj')
main_target = main_project.targets.first
main_target.build_phases.delete_if do |phase|
  phase.display_name == '[CP] Embed Pods Frameworks'
end
main_project.save
