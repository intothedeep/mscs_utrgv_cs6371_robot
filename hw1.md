# HW1 Autonomous Mobile Robots and Programming - Mac OS

## 1. OS and System

- Macbook Pro M3 Max

## 2. Webots

### 2.1. website

- https://cyberbotics.com/

### 2.2. download

```bash
# install with download
# https://github.com/cyberbotics/webots/releases/download/R2025a/webots-R2025a.dmg

# install with brew
brew install --cask webots

```

### 2.3. install

execute webots-R2025a.dmg and install

## 3. ARGoS

### 3.1. website

- https://www.argos-sim.info/

### 3.2. download

- https://github.com/ilpincy/argos3

```bash
git clone https://github.com/ilpincy/argos3.git argos3

```

### 3.3. MacOS clang check

```bash
brew tap ilpincy/argos3

brew trust ilpincy/argos3
brew install bash-completion qt argos3
```

- brew tab owner(ilpincy/argos3) and github repository(github.com/ilpincy/argos3) owner are same.

- error

```txt
brew install bash-completion qt argos3

...
...

==> cmake ../src -DARGOS_BUILD_NATIVE=ON -DCPACK_PACKAGE_VERSION_MAJOR=3 -DCPACK_PACKAGE_VERSION_MINOR=0 -DCPACK_PACKAGE_VERSION_PATCH=0 -DCPACK_PA
Last 15 lines from /Users/tio/Library/Logs/Homebrew/argos3/01.cmake.log:
  to work with policies introduced by <max> or earlier.
This warning is for project developers.  Use -Wno-author or -Wno-deprecated
to suppress it.

CMake Error at CMakeLists.txt:15 (cmake_policy):
  Compatibility with CMake < 3.5 has been removed from CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.

  Or, add -DCMAKE_POLICY_VERSION_MINIMUM=3.5 to try configuring anyway.


-- Configuring incomplete, errors occurred!

If reporting this issue please do so at (not Homebrew/* repositories):
  https://github.com/ilpincy/homebrew-argos3/issues

These open issues may also help:
problems with the installation of Argos3  https://github.com/ilpincy/homebrew-argos3/issues/8
Problems Installing Argos3 in MacOS Big Sur https://github.com/ilpincy/homebrew-argos3/issues/9
```

- cmake version 4.4.3 but argos3 using cmake < 3.5

```sh
cmake --version # cmake version 4.4.3

# delte tap
brew untap ilpincy/argos3
```

do not use brew, build it by myself

```bash
mkdir temp
cd temp

git clone https://github.com/ilpincy/argos3.git argos3

cd argos3
mkdir build_simulator
cd build_simulator
cmake ../src -DCMAKE_POLICY_VERSION_MINIMUM=3.5 # because current version is 4.4.3
make
```

### 3.4.1 Check installation

```bash
argos3 -v

# error
# zsh: command not found: argos3
# need to setup a path
# apple silicon M series
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc

```

## 4. Running an Exmaple

### 4.1.1 Example Source

- https://www.argos-sim.info/examples.php

# install argo3

```bash
brew install pkg-config cmake libpng freeimage lua qt docbook asciidoc graphviz doxygen

git clone https://github.com/ilpincy/argos3.git argos3

cd argos3
mkdir build_simulator
cd build_simulator

# cmake version 3.5
# local user space install
cmake ../src -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_INSTALL_PREFIX=$HOME/.local

# error:
# Install the project...
# -- Install configuration: "Release"
# -- Installing: /Users/tio/.local/bin/argos3
# -- Installing: /Users/tio/.local/share/argos3/uninstall_argos3.sh
# -- Installing: /Users/tio/.local/include/argos3/core/config.h
# CMake Error at cmake_install.cmake:53 (file):
#   file INSTALL cannot find
#   "/Users/tio/Documents/temp/argos3/build_simulator/argos3.1.gz": No such
#   file or directory.
# make: *** [install] Error 1

cd ~/argos3/build_simulator
make
make doc
make install

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

argos -v


## version check
# ➜  csci6371 cmake --version
# cmake version 4.4.3

# CMake suite maintained and supported by Kitware (kitware.com/cmake).
# ➜  csci6371 brew --version
# Homebrew 6.0.21
# ➜  csci6371 uname -m
# arm64
# ➜  csci6371

```

## Example

```bash
cd argos3-examples
mkdir build
cd build
cmake ../ -DCMAKE_POLICY_VERSION_MINIMUM=3.5
make

# error
# ➜  build git:(master) ✗ cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=$HOME/.local ..
# CMake Warning (deprecated) at CMakeLists.txt:1 (cmake_minimum_required):
#   Compatibility with CMake < 3.10 will be removed from a future version of
#   CMake.

#   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
#   to tell CMake that the project requires at least <min> but has been updated
#   to work with policies introduced by <max> or earlier.
# This warning is for project developers.  Use -Wno-author or -Wno-deprecated
# to suppress it.

# -- Found ARGoS: /Users/tio/.local/lib/argos3/libargos3core_simulator.dylib
# CMake Error at /Users/tio/.local/share/argos3/cmake/ARGoSConfig.cmake:103 (find_path):
#   Could not find ARGOS_CMAKE_DIR using the following files:
#   FindARGoSQTOpenGL.cmake
# Call Stack (most recent call first):
#   CMakeLists.txt:22 (find_package)


# -- Configuring incomplete, errors occurred!


cd ~/argos3/build_simulator
rm -rf *
cmake ../src -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_INSTALL_PREFIX=$HOME/.local -DCMAKE_PREFIX_PATH=$(brew --prefix qt)

make
make doc
make install


```

# delete

**설치 스크립트에 제거 스크립트가 이미 포함돼 있다**

이유: 앞서 설치 로그에 `Installing: /Users/tio/.local/share/argos3/uninstall_argos3.sh`가 있었다. argos3 빌드 시스템이 제공하는 공식 제거 스크립트다.

```sh
bash ~/.local/share/argos3/uninstall_argos3.sh
```

**스크립트가 없거나 안 되면 수동으로 지운다**

이유: 설치 로그에 나온 경로들을 그대로 지우면 된다. `~/.local` prefix라서 sudo 필요 없다.

```sh
rm -f ~/.local/bin/argos3
rm -rf ~/.local/include/argos3
rm -rf ~/.local/lib/argos3
rm -f ~/.local/lib/libargos3*
rm -rf ~/.local/share/argos3
```

**확인**

이유: 제대로 지워졌는지 확인한다.

```sh
which argos3
```

아무것도 안 나오면 삭제 완료다.
