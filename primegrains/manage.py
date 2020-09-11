#!/usr/bin/env python
import os

from flask_script import Manager

from app import create_app

application = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(application)


@manager.command
def test():
    """Run the unit tests."""
    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def setup_dev():
    """Runs the set-up needed for local development."""
    setup_general()


@manager.command
def setup_prod():
    """Runs the set-up needed for production."""
    setup_general()


def setup_general():
    """Runs the set-up needed for both local development and production.
       Also sets up first admin user."""
    pass


if __name__ == '__main__':
    manager.run()
