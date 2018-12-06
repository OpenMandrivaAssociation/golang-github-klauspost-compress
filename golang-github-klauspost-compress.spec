%global goipath    github.com/klauspost/compress
Version: 1.2.1

%global common_description %{expand:
This package is based on an optimized Deflate function, which is used by
gzip/zip/zlib packages.

It offers slightly better compression at lower compression settings, and up to
3x faster encoding at highest compression level.}

%gometa

Name:           %{goname}
Release:        3%{?dist}
Summary:        Optimized compression packages
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/klauspost/compress/commit/b88785bfd699aa994985ea91b90ee8a1721c3fe1
Patch0:         0001-Fix-Println-arg-list-ends-with-redundant-newline-83.patch
# https://github.com/klauspost/compress/commit/e80ca55b53e5e6f53deed5c7842e7b7da95e1dc7
Patch1:         0001-Change-back-to-official-crc32.patch
BuildRequires: dos2unix
BuildRequires: golang(github.com/klauspost/cpuid)

%description
%{common_description}

%package devel
Summary: %{summary}

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q
%patch0 -p1
%patch1 -p1 -b .crc32
dos2unix -k README.md

%install
%goinstall

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 11 2018 Dominik Mierzejewski <dominik@greysector.net> - 1.2.1-2
- fix end-of-line encoding in README.md
- build as archful due to assembly usage on x86_64

* Mon Mar 26 2018 Dominik Mierzejewski <dominik@greysector.net> - 1.2.1-1
- initial package for Fedora
