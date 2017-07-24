# swift-staticlibs

**NOTE**: As of Xcode 9 beta 4, Xcode natively supports static libraries
with Swift sources, meaning this ~~hack~~ workaround is no longer
needed!

This repo contains a replacement linker script for building iOS static
frameworks that contain Swift sources from **within Xcode**

## Usage

For each dynamic framework target in Xcode that you would like to be
build statically:

1. Set the undocumented `LD` Xcode build setting to point to `ld.py`
2. Add the target to your main target's `Link Binary With Libraries`
   build phase.

You can set this setting through a user defined build setting in Xcode,
or with a [`xcconfig`][xcconfigs] file like this:

```
LD = $(PROJECT_DIR)/path/to/ld.py
```

## CocoaPods

There are a few issues with using this script alongside CocoaPods:

- With the below configuration, there is no differentiation between
  targets, if for some reason you didn't want to use these scripts for
  all targets, you would have to handle that
- You must delete the `[CP] Embed Pods Frameworks` build phase from all
  targets that depend on CocoaPods. Otherwise your final `.app` bundle
  will contain frameworks that are not referenced and just bloating your
  app size
- If you have any pre-compiled dynamic frameworks that are included with
  CocoaPods, deleting the Embed Pods Frameworks phase will mean these
  are no longer included
- Resources that pods vendor are not handled by these scripts, there are
  2 different ways CocoaPods handles resources:
  - If your pods use the [`resources`][resources] directive
    (which is [not recommended][resources]), your must handle copying
    the resources, **and any conflicts** caused by duplicate naming
  - If your pods are using the recommended [`resource_bundles`][bundles]
    directive, you still have to handle copying the resource bundle into
    your targets, otherwise it is ignored

If you feel comfortable working around these issues, you can add
something like this to your `Podfile`:

```ruby
post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['LD'] = '$(PROJECT_DIR)/path/to/ld.py'
    end
  end
end
```

If you need a more elaborate configuration in CocoaPods, you can use the
[`xcodeproj`](https://github.com/CocoaPods/xcodeproj/) gem in order to
make decisions based on project configuration.

## Why?

1. Xcode has [never supported][radar] building static libraries (and
   definitely not static frameworks) containing Swift sources (although
   this has always been supported by [Swift Package Manager][swiftpm])

2. Dynamic frameworks cause an [impact][eigen] [on][loaf]
   [launch][mjtsai] [times][wwdc]. While this has improved since the
   original issues, there's still significant overhead when you have a
   large amount of modules

3. By using static libraries (or, in this case, static frameworks), you
   don't have to deal with all the overhead of dynamic framework
   loading. See [this session][wwdc] from WWDC 2016 for more details
   around this.

## How?

By replacing the `libtool` invocation from Xcode, this script hijacks
the passed arguments, and transforms them into the arguments necessary
for building static _frameworks_, instead of dynamic frameworks. Then
since the product ends up existing in the same place as the dynamic
framework that would have otherwise been included, Xcode happily links
the static framework instead.

Static _frameworks_ are very similar to dynamic frameworks, except the
binary contained within the framework ends up being linked statically,
instead of dynamically (see [this article][staticvsdynamic] for more
details). They differ from traditional static _libraries_ in that they
have the `.framework` directory structure identical to dynamic
frameworks. This makes it easier to integrate from within Xcode since
Xcode already expects the products from dynamic framework targets to
follow this structure.

[bundles]: https://guides.cocoapods.org/syntax/podspec.html#resource_bundles
[eigen]: https://github.com/artsy/eigen/issues/586
[loaf]: https://useyourloaf.com/blog/slow-app-startup-times
[mjtsai]: https://mjtsai.com/blog/2015/10/26/dynamic-frameworks-and-app-launch-times
[radar]: http://www.openradar.me/17233107
[resources]: https://guides.cocoapods.org/syntax/podspec.html#resources
[staticvsdynamic]: https://pewpewthespells.com/blog/static_and_dynamic_libraries.html
[swiftpm]: https://github.com/apple/swift-package-manager/blob/6bb27929727a1b059168aa6600e10621296bc7fa/Documentation/PackageDescriptionV4.md#products
[wwdc]: https://developer.apple.com/videos/play/wwdc2016/406
[xcconfigs]: https://pewpewthespells.com/blog/xcconfig_guide.html
