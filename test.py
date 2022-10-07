import yaml
import unittest
from dataclasses import dataclass

class TestYAMLContents(unittest.TestCase):

    def test_YAML(self):
        with open('config.yaml') as ymlfile:
            contents = yaml.load(ymlfile, Loader=yaml.FullLoader)
            self.assertIn('targets', contents)
            for entry in contents['targets']:
                required_keys = [
                    'api', 'place', 'placeName', 'campground',
                    'day', 'nights', 'months', 'telegramChats']
                for k in required_keys:
                    self.assertIn(k, entry)
                if 'ranges' in entry:
                    for range in entry['ranges']:
                        for k in ['startDate', 'endDates']:
                            self.assertIn(k, range, f'Full erroneous object:\n{yaml.dump(entry)}')
                if 'sites' in entry:
                    self.assertTrue(isinstance(entry['sites'], list, f'Full erroneous object:\n{yaml.dump(entry)}'))

if __name__ == '__main__':
    unittest.main()