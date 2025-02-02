import torch
from torchviz import make_dot

# 変数 x, y を定義（requires_grad=True を指定）
x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

# 関数 f(x, y) = (xy)^2 を定義
f = (x * y) ** 2

# 計算グラフを可視化
dot = make_dot(f, params={"x": x, "y": y})
dot.render("./material/computation_graph_xy_squared", format="png", cleanup=True)

# 偏導関数を計算
gradients = torch.autograd.grad(f, [x, y])

# 結果を表示
print(f"df/dx = {gradients[0].item()}")  # df/dx = 2(xy)・y = 2(2・3)・3 = 36
print(f"df/dy = {gradients[1].item()}")  # df/dy = 2(xy)・x = 2(2・3)・2 = 24