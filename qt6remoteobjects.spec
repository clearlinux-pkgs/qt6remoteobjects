#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
Name     : qt6remoteobjects
Version  : 6.6.2
Release  : 11
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtremoteobjects-everywhere-src-6.6.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtremoteobjects-everywhere-src-6.6.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6remoteobjects-lib = %{version}-%{release}
Requires: qt6remoteobjects-libexec = %{version}-%{release}
Requires: qt6remoteobjects-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
These files are generated by the script located at tests/auto/external_IODevice/cert/generate.sh

%package dev
Summary: dev components for the qt6remoteobjects package.
Group: Development
Requires: qt6remoteobjects-lib = %{version}-%{release}
Provides: qt6remoteobjects-devel = %{version}-%{release}
Requires: qt6remoteobjects = %{version}-%{release}

%description dev
dev components for the qt6remoteobjects package.


%package lib
Summary: lib components for the qt6remoteobjects package.
Group: Libraries
Requires: qt6remoteobjects-libexec = %{version}-%{release}
Requires: qt6remoteobjects-license = %{version}-%{release}

%description lib
lib components for the qt6remoteobjects package.


%package libexec
Summary: libexec components for the qt6remoteobjects package.
Group: Default
Requires: qt6remoteobjects-license = %{version}-%{release}

%description libexec
libexec components for the qt6remoteobjects package.


%package license
Summary: license components for the qt6remoteobjects package.
Group: Default

%description license
license components for the qt6remoteobjects package.


%prep
%setup -q -n qtremoteobjects-everywhere-src-6.6.2
cd %{_builddir}/qtremoteobjects-everywhere-src-6.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708118300
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1708118300
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6remoteobjects
cp %{_builddir}/qtremoteobjects-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6remoteobjects/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtremoteobjects-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6remoteobjects/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtremoteobjects-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6remoteobjects/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtremoteobjects-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6remoteobjects/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtremoteobjects-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6remoteobjects/f45ee1c765646813b442ca58de72e20a64a7ddba || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6remoteobjects_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6remoteobjectsqml_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/features/remoteobjects_repc.prf
/usr/lib64/qt6/mkspecs/features/repcclient.pri
/usr/lib64/qt6/mkspecs/features/repccommon.pri
/usr/lib64/qt6/mkspecs/features/repcmerged.pri
/usr/lib64/qt6/mkspecs/features/repcserver.pri
/usr/lib64/qt6/mkspecs/features/repparser.prf
/usr/lib64/qt6/mkspecs/modules/qt_lib_remoteobjects.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_remoteobjects_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_remoteobjectsqml.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_remoteobjectsqml_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_repparser.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_repparser_private.pri
/usr/lib64/qt6/modules/RemoteObjects.json
/usr/lib64/qt6/modules/RemoteObjectsQml.json
/usr/lib64/qt6/modules/RepParser.json
/usr/lib64/qt6/qml/QtRemoteObjects/plugins.qmltypes
/usr/lib64/qt6/qml/QtRemoteObjects/qmldir

%files dev
%defattr(-,root,root,-)
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qconnection_local_backend_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qconnection_tcpip_backend_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qconnectionfactories_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qremoteobjectabstractitemmodeltypes_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qremoteobjectcontainers_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qremoteobjectnode_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qremoteobjectpacket_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qremoteobjectpendingcall_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qremoteobjectregistrysource_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qremoteobjectreplica_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qremoteobjectsource_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qremoteobjectsourceio_p.h
/usr/include/QtRemoteObjects/6.6.2/QtRemoteObjects/private/qtremoteobjects-config_p.h
/usr/include/QtRemoteObjects/QAbstractItemModelReplica
/usr/include/QtRemoteObjects/QConnectionAbstractServer
/usr/include/QtRemoteObjects/QIntHash
/usr/include/QtRemoteObjects/QRemoteObjectAbstractPersistedStore
/usr/include/QtRemoteObjects/QRemoteObjectDynamicReplica
/usr/include/QtRemoteObjects/QRemoteObjectHost
/usr/include/QtRemoteObjects/QRemoteObjectHostBase
/usr/include/QtRemoteObjects/QRemoteObjectNode
/usr/include/QtRemoteObjects/QRemoteObjectPendingCall
/usr/include/QtRemoteObjects/QRemoteObjectPendingCallWatcher
/usr/include/QtRemoteObjects/QRemoteObjectPendingReply
/usr/include/QtRemoteObjects/QRemoteObjectRegistry
/usr/include/QtRemoteObjects/QRemoteObjectRegistryHost
/usr/include/QtRemoteObjects/QRemoteObjectReplica
/usr/include/QtRemoteObjects/QRemoteObjectSettingsStore
/usr/include/QtRemoteObjects/QRemoteObjectSourceLocation
/usr/include/QtRemoteObjects/QRemoteObjectSourceLocationInfo
/usr/include/QtRemoteObjects/QRemoteObjectSourceLocations
/usr/include/QtRemoteObjects/QtROClientFactory
/usr/include/QtRemoteObjects/QtROClientIoDevice
/usr/include/QtRemoteObjects/QtROIoDeviceBase
/usr/include/QtRemoteObjects/QtROServerFactory
/usr/include/QtRemoteObjects/QtROServerIoDevice
/usr/include/QtRemoteObjects/QtRemoteObjects
/usr/include/QtRemoteObjects/QtRemoteObjectsDepends
/usr/include/QtRemoteObjects/QtRemoteObjectsVersion
/usr/include/QtRemoteObjects/qconnectionfactories.h
/usr/include/QtRemoteObjects/qremoteobjectabstractitemmodelreplica.h
/usr/include/QtRemoteObjects/qremoteobjectdynamicreplica.h
/usr/include/QtRemoteObjects/qremoteobjectnode.h
/usr/include/QtRemoteObjects/qremoteobjectpendingcall.h
/usr/include/QtRemoteObjects/qremoteobjectregistry.h
/usr/include/QtRemoteObjects/qremoteobjectreplica.h
/usr/include/QtRemoteObjects/qremoteobjectsettingsstore.h
/usr/include/QtRemoteObjects/qremoteobjectsource.h
/usr/include/QtRemoteObjects/qtremoteobjectglobal.h
/usr/include/QtRemoteObjects/qtremoteobjects-config.h
/usr/include/QtRemoteObjects/qtremoteobjectsexports.h
/usr/include/QtRemoteObjects/qtremoteobjectsversion.h
/usr/include/QtRemoteObjectsQml/6.6.2/QtRemoteObjectsQml/private/qremoteobjectsqml_p.h
/usr/include/QtRemoteObjectsQml/QtRemoteObjectsQml
/usr/include/QtRemoteObjectsQml/QtRemoteObjectsQmlDepends
/usr/include/QtRemoteObjectsQml/QtRemoteObjectsQmlVersion
/usr/include/QtRemoteObjectsQml/qtremoteobjectsqmlversion.h
/usr/include/QtRepParser/QtRepParserDepends
/usr/include/QtRepParser/parser.g
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtRemoteObjectsTestsConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_remoteobjectsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_remoteobjectsConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_remoteobjectsConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_remoteobjectsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_remoteobjectsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_remoteobjectsTargets.cmake
/usr/lib64/cmake/Qt6RemoteObjects/Qt6RemoteObjectsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6RemoteObjects/Qt6RemoteObjectsConfig.cmake
/usr/lib64/cmake/Qt6RemoteObjects/Qt6RemoteObjectsConfigVersion.cmake
/usr/lib64/cmake/Qt6RemoteObjects/Qt6RemoteObjectsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6RemoteObjects/Qt6RemoteObjectsDependencies.cmake
/usr/lib64/cmake/Qt6RemoteObjects/Qt6RemoteObjectsMacros.cmake
/usr/lib64/cmake/Qt6RemoteObjects/Qt6RemoteObjectsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6RemoteObjects/Qt6RemoteObjectsTargets.cmake
/usr/lib64/cmake/Qt6RemoteObjects/Qt6RemoteObjectsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6RemoteObjectsQml/Qt6RemoteObjectsQmlAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6RemoteObjectsQml/Qt6RemoteObjectsQmlConfig.cmake
/usr/lib64/cmake/Qt6RemoteObjectsQml/Qt6RemoteObjectsQmlConfigVersion.cmake
/usr/lib64/cmake/Qt6RemoteObjectsQml/Qt6RemoteObjectsQmlConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6RemoteObjectsQml/Qt6RemoteObjectsQmlDependencies.cmake
/usr/lib64/cmake/Qt6RemoteObjectsQml/Qt6RemoteObjectsQmlTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6RemoteObjectsQml/Qt6RemoteObjectsQmlTargets.cmake
/usr/lib64/cmake/Qt6RemoteObjectsQml/Qt6RemoteObjectsQmlVersionlessTargets.cmake
/usr/lib64/cmake/Qt6RemoteObjectsTools/Qt6RemoteObjectsToolsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6RemoteObjectsTools/Qt6RemoteObjectsToolsConfig.cmake
/usr/lib64/cmake/Qt6RemoteObjectsTools/Qt6RemoteObjectsToolsConfigVersion.cmake
/usr/lib64/cmake/Qt6RemoteObjectsTools/Qt6RemoteObjectsToolsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6RemoteObjectsTools/Qt6RemoteObjectsToolsDependencies.cmake
/usr/lib64/cmake/Qt6RemoteObjectsTools/Qt6RemoteObjectsToolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6RemoteObjectsTools/Qt6RemoteObjectsToolsTargets.cmake
/usr/lib64/cmake/Qt6RemoteObjectsTools/Qt6RemoteObjectsToolsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6RepParser/Qt6RepParserAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6RepParser/Qt6RepParserConfig.cmake
/usr/lib64/cmake/Qt6RepParser/Qt6RepParserConfigVersion.cmake
/usr/lib64/cmake/Qt6RepParser/Qt6RepParserConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6RepParser/Qt6RepParserDependencies.cmake
/usr/lib64/cmake/Qt6RepParser/Qt6RepParserTargets.cmake
/usr/lib64/cmake/Qt6RepParser/Qt6RepParserVersionlessTargets.cmake
/usr/lib64/libQt6RemoteObjects.prl
/usr/lib64/libQt6RemoteObjects.so
/usr/lib64/libQt6RemoteObjectsQml.prl
/usr/lib64/libQt6RemoteObjectsQml.so
/usr/lib64/pkgconfig/Qt6RemoteObjects.pc
/usr/lib64/pkgconfig/Qt6RemoteObjectsQml.pc
/usr/lib64/pkgconfig/Qt6RepParser.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6RemoteObjects.so.6.6.2
/V3/usr/lib64/libQt6RemoteObjectsQml.so.6.6.2
/V3/usr/lib64/qt6/qml/QtRemoteObjects/libdeclarative_remoteobjectsplugin.so
/usr/lib64/libQt6RemoteObjects.so.6
/usr/lib64/libQt6RemoteObjects.so.6.6.2
/usr/lib64/libQt6RemoteObjectsQml.so.6
/usr/lib64/libQt6RemoteObjectsQml.so.6.6.2
/usr/lib64/qt6/qml/QtRemoteObjects/libdeclarative_remoteobjectsplugin.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/repc
/usr/libexec/repc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6remoteobjects/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt6remoteobjects/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6remoteobjects/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6remoteobjects/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6remoteobjects/f45ee1c765646813b442ca58de72e20a64a7ddba
