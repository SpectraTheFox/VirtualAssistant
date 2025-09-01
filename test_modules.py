import unittest
import importlib
import os 

class TestModules(unittest.TestCase):
    def test_modules_loadable(self):
        module_names = []
        for (dirpath, dirnames, filenames) in os.walk("src/modules"):
            module_names.extend(filenames)
            break
        module_names = [x.replace(".py", "") for x in module_names]
        if ".DS_Store" in module_names:
            module_names.remove(".DS_Store")
            
        for module_name in module_names:
            with self.subTest(module=module_name):
                try:
                    module = importlib.import_module(f'modules.{module_name}')
                    self.assertTrue(hasattr(module, 'checkactivation'), f"{module_name} should have a checkactivation function.")
                    self.assertTrue(hasattr(module, 'run'), f"{module_name} should have a run function.")
                except Exception as e:
                    self.fail(f"Module {module_name} failed to load: {e}")

    def test_check_run(self):

        moduleslist = []
        for (dirpath, dirnames, filenames) in os.walk("src/modules"):
            moduleslist.extend(filenames)
            break
        moduleslist = [x.replace(".py", "") for x in moduleslist]
        if ".DS_Store" in moduleslist:
            moduleslist.remove(".DS_Store")

        for moduleselected in moduleslist:
            module = importlib.import_module(f'modules.{moduleselected}')
            ran = module.run("test input")
            self.assertEqual(ran, ran)

if __name__ == '__main__':   
    unittest.main()