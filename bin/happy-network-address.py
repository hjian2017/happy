#!/usr/bin/env python

#
#    Copyright (c) 2015-2017 Nest Labs, Inc.
#    All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

##
#    @file
#       A Happy command line utility that modifies network IP prefixes.
#
#       The command is executed by instantiating and running HappyNetworkAddress class.
#

import getopt
import sys

import happy.HappyNetworkAddress
from happy.Utils import *

if __name__ == "__main__":
    options = happy.HappyNetworkAddress.option()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:qad",
                                   ["help", "id=", "quiet", "add", "delete"])

    except getopt.GetoptError as err:
        print happy.HappyNetworkAddress.HappyNetworkAddress.__doc__
        print hred(str(err))
        sys.exit(hred("%s: Failed to parse arguments." % (__file__)))

    for o, a in opts:
        if o in ("-h", "--help"):
            print happy.HappyNetworkAddress.HappyNetworkAddress.__doc__
            sys.exit(0)

        elif o in ("-q", "--quiet"):
            options["quiet"] = True

        elif o in ("-i", "--id"):
            options["network_id"] = a

        elif o in ("-a", "--add"):
            options["add"] = True

        elif o in ("-d", "--delete"):
            options["delete"] = True

        else:
            assert False, "unhandled option"

    if len(args) == 1:
        options["address"] = args[0]

    if len(args) == 2:
        options["network_id"] = args[0]
        options["address"] = args[1]

    cmd = happy.HappyNetworkAddress.HappyNetworkAddress(options)
    cmd.start()
