from django.core.management import call_command
from boot_django import boot_django
import os, sys, xmlrunner

boot_django()

results_dir = os.path.join(os.getcwd(), "test-results")
os.makedirs(results_dir, exist_ok=True)

call_command("test",
    verbosity=2,
    failfast=False,
    stdout=sys.stdout,
    stderr=sys.stderr,
    test_runner='xmlrunner.extra.djangotestrunner.XMLTestRunner',
    output_dir=results_dir)