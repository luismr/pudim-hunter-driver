from setuptools import setup
from setuptools_scm.version import get_local_node_and_date

def normalize_branch_name(name):
    """Normalize branch name to snake_case"""
    return name.lower().replace('/', '_').replace('-', '_')

def local_scheme(version):
    if version.exact:
        return ''
    node = version.node[:5] if version.node else 'UNKNOWN'
    branch = normalize_branch_name(version.branch) if version.branch else 'unknown'
    date = version.time.strftime('%Y%m%d') if version.time else ''
    return f"{branch}-{date}-{node}"

setup(
    use_scm_version={
        "version_scheme": "release-branch-semver",
        "local_scheme": local_scheme,
        "write_to": "src/pudim_hunter_driver/_version.py",
        "tag_regex": r'^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$'
    }
) 