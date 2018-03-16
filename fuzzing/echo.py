#!/usr/bin/env python
# Copyright 2018 The Fuchsia Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

# Simply writes argv[2:] to the file described by argv[1]
def main():
  assert len(sys.argv) > 1
  with open(sys.argv[1], 'w') as f:
    for arg in sys.argv[2:]:
      f.write(arg)
      f.write('\n')

if __name__ == '__main__':
  sys.exit(main())
