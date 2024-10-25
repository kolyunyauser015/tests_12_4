import unittest
import running_tournament_1 as rt
import logging

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner_1 = rt.Runner('Maxim', -5)
            for n in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logging.info('"ftest_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner_2 = rt.Runner(5)
            for n in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logging.info('"ftest_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = rt.Runner('Olga', 5)
        runner_4 = rt.Runner('Petr', 7)
        for n in range(10):
            runner_3.walk()
            runner_4.walk()
        d_1 = runner_3.distance
        d_2 = runner_4.distance
        for n in range(10):
            runner_3.run()
            runner_4.run()
        d_3 = runner_3.distance
        d_4 = runner_4.distance
        self.assertNotEqual(d_1, d_3)
        self.assertNotEqual(d_2, d_4)
        self.assertNotEqual(d_1, d_2)
        self.assertNotEqual(d_3, d_4)

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                    encoding="UTF-8", format="%(asctime)s | %(levelname)s | %(message)s")
