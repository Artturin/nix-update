from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


@dataclass
class Version:
    number: str
    prerelease: Optional[bool] = None
    rev: Optional[str] = None


class VersionPreference(Enum):
    STABLE = auto()
    UNSTABLE = auto()
    FIXED = auto()
    SKIP = auto()
    BRANCH = auto()

    @staticmethod
    def from_str(version: str) -> "VersionPreference":
        # auto is deprecated
        if version == "auto" or version == "stable":
            return VersionPreference.STABLE
        elif version == "unstable":
            return VersionPreference.UNSTABLE
        elif version == "skip":
            return VersionPreference.SKIP
        elif version == "branch" or version.startswith("branch="):
            return VersionPreference.BRANCH
        return VersionPreference.FIXED
