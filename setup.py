from setuptools import setup

setup(
	name='snapshot-3000',
	version='0.1',
	author="Dustin Rinebold",
	author_email="test@email.com",
	description="Snapshot-3000 is a tool to manage AWAS snapshots",
	license="GPLv3+",
	packages=['shotty'],
	url="google.html",
	install_requires=[
		'click',
		'boto3'
	],
	entry_points='''
		[console_scripts]
		shotty=shotty.shotty:cli
	''',
)