#   -*- coding: utf-8 -*-
#
#   This file is part of node-cli
#
#   Copyright (C) 2022-Present SKALE Labs
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os

from configs import NODE_DATA_PATH, DATAFILES_FOLDER


DEFAULT_SSL_CHECK_PORT = 4536
SKALED_SSL_TEST_SCRIPT = os.path.join(DATAFILES_FOLDER, 'skaled-ssl-test')

SSL_FOLDER_PATH = os.path.join(NODE_DATA_PATH, 'ssl')
SSL_CERT_FILEPATH = os.path.join(SSL_FOLDER_PATH, 'ssl_cert')
SSL_KEY_FILEPATH = os.path.join(SSL_FOLDER_PATH, 'ssl_key')

CERTS_UPLOADED_ERR_MSG = 'SSL Certificates are already uploaded'
CERTS_INVALID_FORMAT = 'Certificates have invalid format'
