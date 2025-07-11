#  SPDX-License-Identifier: BSD-3-Clause
#  Copyright (C) 2016 Intel Corporation
#  All rights reserved.
#  Copyright (c) 2022 Dell Inc, or its subsidiaries.
#  Copyright (c) 2022-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#

import sys
import spdk.rpc as rpc  # noqa
from spdk.rpc.client import print_dict, print_json, print_array  # noqa


def add_parser(subparsers):

    def notify_get_types(args):
        print_dict(rpc.notify.notify_get_types(args.client))

    p = subparsers.add_parser('notify_get_types', help='List available notifications that user can subscribe to.')
    p.set_defaults(func=notify_get_types)

    def notify_get_notifications(args):
        ret = rpc.notify.notify_get_notifications(args.client,
                                                  id=args.id,
                                                  max=args.max)
        print_dict(ret)

    p = subparsers.add_parser('notify_get_notifications', help='Get notifications')
    p.add_argument('-i', '--id', help="""First ID to start fetching from""", type=int)
    p.add_argument('-n', '--max', help="""Maximum number of notifications to return in response""", type=int)
    p.set_defaults(func=notify_get_notifications)
