import localcrawl
import os
import unittest


class CrawlerTest(unittest.TestCase):
    def all_contents(self, directory):
        contents = ''
        for f in os.listdir(directory):
            with open(os.path.join(directory, f), 'r') as f:
                contents += f.read()
        return contents

    def test_index(self):
        o = 'tests/temp_data/simple_site'
        c = localcrawl.Crawler('tests/data/simple_site/index.html', o).crawl()
        self.assertEqual(1, c)
        self.assertIn('<title>Simple Site</title>', self.all_contents(o))

    def test_link(self):
        o = 'tests/temp_data/linked_page'
        c = localcrawl.Crawler('tests/data/linked_page/index.html', o).crawl()
        self.assertEqual(2, c)

        contents = self.all_contents(o)
        self.assertIn('<title>Linked Page</title>', contents)
        self.assertIn('<title>Linked Page, Page 2</title>', contents)

    def test_mustache(self):
        o = 'tests/temp_data/mustache'
        c = localcrawl.Crawler('tests/data/mustache/index.html', o).crawl()
        self.assertEqual(1, c)

        contents = self.all_contents(o)
        self.assertIn('Fork: <b>$1.19</b>', contents)