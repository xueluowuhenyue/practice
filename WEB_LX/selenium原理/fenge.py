# d={"value":{"element-6066-11e4-a52e-4f735466cecf":"35be6f1b-bdde-4471-b62c-77b92fc87d7d"}}
# j=d['value']


def get_value(d):
    for j in d.values():
        # print(j)
        return j


if __name__ == '__main__':
    s={"element-6066-11e4-a52e-4f735466cecf":"35be6f1b-bdde-4471-b62c-77b92fc87d7d"}
    get_value(s)