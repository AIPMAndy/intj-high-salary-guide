import json
import pathlib
import unittest
import importlib.util

ROOT = pathlib.Path(__file__).resolve().parents[1]

class ProjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapters = json.loads((ROOT/'data/chapters.json').read_text(encoding='utf-8'))
        cls.templates = json.loads((ROOT/'data/templates.json').read_text(encoding='utf-8'))
        cls.plan = json.loads((ROOT/'data/plan.json').read_text(encoding='utf-8'))
        cls.html = (ROOT/'index.html').read_text(encoding='utf-8')

    def test_chapter_count_and_unique_ids(self):
        self.assertEqual(10,len(self.chapters))
        self.assertEqual(10,len({c['id'] for c in self.chapters}))
        for c in self.chapters:
            for key in ('title','lead','pitfall','example','deliverable','duration'):
                self.assertTrue(c[key], f'Missing {key} for {c["id"]}')
            self.assertEqual(4,len(c['actions']))
            self.assertGreater(len(c['tags']),0)

    def test_plan_seven_days_and_templates(self):
        self.assertEqual(list(range(1,8)),[p['day'] for p in self.plan])
        self.assertEqual(6,len(self.templates))
        self.assertEqual(6,len({t['id'] for t in self.templates}))

    def test_no_unresolved_build_placeholders(self):
        for marker in ('__CHAPTERS_JSON__','__TEMPLATES_JSON__','__PLAN_JSON__'):
            self.assertNotIn(marker,self.html)
        for name in ('chapters-data','templates-data','plan-data','chapter-list','offer-diff','progress-bar'):
            self.assertIn(name,self.html)

    def test_links_and_legal(self):
        for name in ('docs/sources.md','assets/social-preview.png','assets/favicon.svg','guides/30-day-plan.md'):
            self.assertTrue((ROOT/name).exists(),name)
        self.assertIn('https://metaver.vip/services',self.html)
        self.assertIn('https://github.com/AIPMAndy/intj-high-salary-guide',self.html)

    def test_builder_fresh(self):
        spec = importlib.util.spec_from_file_location('builder',ROOT/'scripts/build.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(self.html,module.generate())

if __name__ == '__main__':
    unittest.main()
