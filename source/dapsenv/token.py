#
# Copyright (c) 2016 SUSE Linux GmbH
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 3 of the GNU General Public License as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, contact SUSE LLC.
#
# To contact SUSE about this file by physical or electronic mail,
# you may find current contact information at www.suse.com

from dapsenv.general import CLIENT_TOKEN_PATH, TOKEN_LENGTH
from dapsenv.utils import randomString

def getToken():
    """Reads the client token

    :return string: client token
    """

    token = ""

    with open(CLIENT_TOKEN_PATH, "r") as token_file:
        token = token_file.read()

    return token

def regenerateToken():
    """Regenerates the client token

    :param string: new client token
    """

    token = randomString(TOKEN_LENGTH)

    with open(CLIENT_TOKEN_PATH, "w") as token_file:
        token_file.write(token)

    return token