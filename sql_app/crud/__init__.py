from ..core.config import settings

from fastapi import Depends, HTTPException, Security, status
from sqlalchemy.orm import Session

from datetime import datetime, timedelta
from typing import Optional

import pprint
pp = pprint.PrettyPrinter(indent=4)
