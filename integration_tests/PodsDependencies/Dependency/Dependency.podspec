Pod::Spec.new do |s|
  s.name                = 'Dependency'
  s.version             = '0.0.1'
  s.summary             = 'A test pod'
  s.homepage            = 'https://github.com/keith/swift-staticlibs'
  s.license             = 'MIT'
  s.author              = { 'Keith Smiley' => 'k@keith.so' }
  s.source              = {
    git: 'https://github.com/keith/swift-staticlibs.git'
  }
  s.source_files        = 'Sources/*.swift'
  s.platform            = :ios, '10.0'
end
