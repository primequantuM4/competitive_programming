class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        foodDependencies = defaultdict(list)
        degreesOfFood = defaultdict(int)
        firstFoods = deque([])

        foodThatCanBeMade = []
        for recipe in range(len(recipes)):
            foodDependencies[recipes[recipe]] = []
            indexDict[recipes[recipe]] = recipe
            for ingredient in ingredients[recipe]:
                if ingredient in recipes:
                    foodDependencies[ingredient].append(recipes[recipe])
                    degreesOfFood[recipes[recipe]] += 1

        for food in foodDependencies.keys():
            if degreesOfFood[food] == 0:
                firstFoods.append(food)

        while firstFoods:
            food = firstFoods.popleft()
            foodIdx = indexDict[food]
            isAFoodThatCanBeMade = True
            for ingredient in ingredients[foodIdx]:
                if ingredient not in dynamicSupplies:
                    isAFoodThatCanBeMade = False
                    break

            if isAFoodThatCanBeMade:
                foodThatCanBeMade.append(food)
                dynamicSupplies.add(food)

            for nextFood in foodDependencies[food]:
                degreesOfFood[nextFood] -= 1
                if degreesOfFood[nextFood] == 0:
                    firstFoods.append(nextFood)


        return foodThatCanBeMade
