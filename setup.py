from setuptools import setup
from setuptools_scm.version import get_local_node_and_date

def normalize_branch_name(name):
    """Normalize branch name to snake_case"""
    return name.lower().replace('/', '_').replace('-', '_')

def local_scheme(version):
    """Custom version scheme that uses branch name, date, and short hash"""
    if version.exact:
        return ""
    node = version.node[:5] if version.node else 'UNKNOWN'
    branch = normalize_branch_name(version.branch) if version.branch else 'unknown'
    date = version.time.strftime('%Y%m%d') if version.time else ''
    return f"{branch}-{date}-{node}"

def version_scheme(version):
    """Custom version scheme that handles both tagged and non-tagged versions"""
    if version.exact:
        # Remove 'v' prefix if present
        tag = version.tag.base_version
        if tag.startswith('v'):
            tag = tag[1:]
        return tag
    
    # For non-tagged versions, use branch name and commit hash
    return f"0.0.0+{local_scheme(version)}"

setup(
    use_scm_version={
        "version_scheme": version_scheme,
        "local_scheme": lambda _: "",  # We handle local version in version_scheme
        "write_to": "src/pudim_hunter_driver/_version.py",
        "tag_regex": r'^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$',
        "relative_to": __file__,
    }
) 