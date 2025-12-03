"""Test basic imports and package structure."""

import pytest


def test_import_vla_arena():
    """Test that vla_arena can be imported."""
    import vla_arena

    assert vla_arena is not None


def test_version():
    """Test that version information is available."""
    import vla_arena

    assert hasattr(vla_arena, '__version__')
    assert isinstance(vla_arena.__version__, str)
    assert len(vla_arena.__version__) > 0


def test_package_metadata():
    """Test that package metadata is accessible."""
    try:
        from importlib.metadata import metadata, version

        pkg_version = version('vla-arena')
        pkg_metadata = metadata('vla-arena')

        assert pkg_version is not None
        assert pkg_metadata['Name'] == 'vla-arena'
    except Exception:
        # Package not installed yet, skip test
        pytest.skip('Package not installed')
