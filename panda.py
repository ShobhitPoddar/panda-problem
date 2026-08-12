import collections
import math
from typing import List
import config
import json

resultsFile = f"{config.MWS_username or 'panda'}-results.json"



class BambooPlot:

    def __init__(self, name, growthRates):
        self.name = name
        self.growthRates = growthRates

    def simulate(self, solution: List[int],
                 iterations: int = 1000000):
        guaranteedHarvest = guaranteed_harvest(self.growthRates, solution,
                                               iterations)
        print(f'{self.name} guaranteedHarvest={guaranteedHarvest}')
        try:
            write_results(self.name, guaranteedHarvest, solution)
        except Exception as e:
            print(f"Could not save result to {resultsFile}: {e}")


def guaranteed_harvest(growthRates: List[int], solution: List[int], iterations: int = 100000):
    queue = collections.deque(solution)
    k = len(growthRates)
    guaranteedHarvest = math.inf
    heights = k * [math.inf]
    for i in range(iterations):
        toCut = queue.popleft()
        queue.append(toCut)
        guaranteedHarvest = min(guaranteedHarvest, heights[toCut])
        heights[toCut] = 0
        for j in range(0, k):
            heights[j] += growthRates[j]
    return guaranteedHarvest


def write_dict(results):
    with open(resultsFile, 'w', encoding="utf-8") as file:
        json.dump(results, file, sort_keys=True, indent=2)


def read_dict():
    try:
        with open(resultsFile, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def write_results(plotName: str, guaranteedHarvest: int, solution: List[int]):
    results = read_dict()
    results[plotName] = guaranteedHarvest, solution
    write_dict(results)
