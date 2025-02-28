import pulp
import numpy as np

# 個体数・グループ数の設定
num_individuals = 99
num_groups = 9
group_size = num_individuals // num_groups  # 11

# 重量データ（ランダムなサンプル）
np.random.seed(42)
weights = np.random.uniform(50, 60, num_individuals)  # 50g ~ 60g の範囲でランダムな重量
weights = np.sort(weights)

# 最適化問題の定義
prob = pulp.LpProblem("Minimize_Weight_Variance", pulp.LpMinimize)

# 変数定義 (個体 i がグループ j に属するか)
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_individuals) for j in range(num_groups)), cat="Binary")

# 各グループの平均重量を表す変数
group_weight = {j: pulp.LpVariable(f"w_{j}") for j in range(num_groups)}

# 各個体はちょうど1つのグループに所属
for i in range(num_individuals):
    prob += pulp.lpSum(x[i, j] for j in range(num_groups)) == 1

# 各グループには11個の個体が割り当てられる
for j in range(num_groups):
    prob += pulp.lpSum(x[i, j] for i in range(num_individuals)) == group_size

# 各グループの平均重量の計算
for j in range(num_groups):
    prob += group_weight[j] == pulp.lpSum(weights[i] * x[i, j] for i in range(num_individuals)) / group_size

### 解法1: 平均重量のばらつきを最小化（分散最小化）

mean_weight = pulp.lpSum(group_weight[j] for j in range(num_groups)) / num_groups
prob += pulp.lpSum((group_weight[j] - mean_weight) for j in range(num_groups))  # 分散の最小化

# ここで2乗したいけど、それだと非線形になって一気に解きづらくなる。

###

### 解法2: 最大最小の範囲を最小化

# 最大・最小グループ平均重量の変数を定義
w_max = pulp.LpVariable("w_max")
w_min = pulp.LpVariable("w_min")

# 各グループの平均重量は w_max 以下
for j in range(num_groups):
    prob += group_weight[j] <= w_max

# 各グループの平均重量は w_min 以上
for j in range(num_groups):
    prob += group_weight[j] >= w_min

# 目的関数：最大平均重量と最小平均重量の差を最小化
prob += w_max - w_min

# 制約のせいか、時間がかかりすぎる。
# 他にも補助変数をもちいて平均との差の絶対値の和を合計する方法もあるが、同様に時間がかかる。

###

# ソルバーを用いて最適化
prob.solve()

# 最適化結果の出力
if pulp.LpStatus[prob.status] == "Optimal":
    group_assignments = {j: [] for j in range(num_groups)}

    for i in range(num_individuals):
        for j in range(num_groups):
            if pulp.value(x[i, j]) == 1:
                group_assignments[j].append(weights[i])

    # 各グループの重量平均を表示
    for j in range(num_groups):
        print(f"Group {j+1}: Avg Weight = {np.mean(group_assignments[j]):.2f}, Members = {group_assignments[j]}")
else:
    print("Optimal solution not found.")
