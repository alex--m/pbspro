# coding: utf-8

# Copyright (C) 1994-2020 Altair Engineering, Inc.
# For more information, contact Altair at www.altair.com.
#
# This file is part of the PBS Professional ("PBS Pro") software.
#
# Open Source License Information:
#
# PBS Pro is free software. You can redistribute it and/or modify it under the
# terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# PBS Pro is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Commercial License Information:
#
# For a copy of the commercial license terms and conditions,
# go to: (http://www.pbspro.com/UserArea/agreement.html)
# or contact the Altair Legal Department.
#
# Altair’s dual-license business model allows companies, individuals, and
# organizations to create proprietary derivative works of PBS Pro and
# distribute them - whether embedded or bundled with other software -
# under a commercial license agreement.
#
# Use of Altair’s trademarks, including but not limited to "PBS™",
# "PBS Professional®", and "PBS Pro™" and Altair’s logos is subject to Altair's
# trademark licensing policies.

from tests.functional import *


class TestQsubWblock(TestFunctional):
    """
    This test suite contains the block job feature tests
    """
    def test_block_job(self):
        """
        Test to submit a block job and verify the Server response
        """
        j = Job(TEST_USER, attrs={ATTR_block: 'true'})
        j.set_sleep_time(1)
        jid = self.server.submit(j)
        client_host = socket.getfqdn(self.server.client)
        msg = 'Server@%s;Job;%s;check_block_wt: Write successful' \
              ' to client %s for job %s' % \
              (self.server.shortname, jid, client_host, jid)
        self.server.log_match(msg, tail=True, interval=2, max_attempts=30)

    def test_block_job_array(self):
        """
        Test to submit a block array job and verify the Server response
        """
        j = Job(TEST_USER, attrs={ATTR_block: 'true', ATTR_J: '1-3'})
        j.set_sleep_time(1)
        jid = self.server.submit(j)
        client_host = socket.getfqdn(self.server.client)
        msg = 'Server@%s;Job;%s;check_block_wt: Write successful ' \
              'to client %s for job %s' % \
              (self.server.shortname, jid, client_host, jid)
        self.server.log_match(msg, tail=True, interval=2, max_attempts=30)
