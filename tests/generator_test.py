import pytest
from context import src, os, sys
from generator import Generator

def test_it_add_build_dir_if_none_exists():
    if os.path.isdir('./build'):
        os.system('rm -rf ./build')

    Generator().build('./tests/content/')

    assert os.path.isdir('./build')

def test_it_should_open_the_article_and_write_to_the_build_directory():
    Generator().build('./tests/content/')

    assert os.path.isfile('./build/posts/article1.html');

def test_it_should_write_index_file_to_build_dir():
    Generator().build('./tests/content/')

    assert os.path.isfile('./build/index.html');

def test_it_should_copy_assets_to_build_folder():
    Generator().build('./tests/content/')

    assert os.path.isfile('./build/assets/style.css')

def test_it_should_copy_static_files():
    Generator().build('./tests/content/')

    assert os.path.isfile('./build/about.html')
