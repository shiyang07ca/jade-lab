import numpy as np

# 创建示例用户-物品评分矩阵
ratings = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4],
])

print("用户-物品评分矩阵:")
print(ratings)

# 计算物品相似度矩阵
def item_similarity(ratings):
    n_items = ratings.shape[1]
    sim = np.zeros((n_items, n_items))

    for i in range(n_items):
        for j in range(n_items):
            # 找到对物品i和j都有评分的用户
            mask = np.logical_and(ratings[:,i] != 0, ratings[:,j] != 0)
            if np.sum(mask) == 0:
                sim[i,j] = 0
            else:
                # 使用余弦相似度
                i_ratings = ratings[mask,i]
                j_ratings = ratings[mask,j]
                sim[i,j] = np.dot(i_ratings, j_ratings) / (np.linalg.norm(i_ratings) * np.linalg.norm(j_ratings))

    return sim

sim_matrix = item_similarity(ratings)
print("\n物品相似度矩阵:")
print(sim_matrix)

# 为用户生成推荐
def recommend(user_id, ratings, sim_matrix, n_recommendations=2):
    user_ratings = ratings[user_id]
    scores = np.zeros(ratings.shape[1])

    for i in range(len(user_ratings)):
        if user_ratings[i] == 0:  # 只预测用户未评分的物品
            for j in range(len(user_ratings)):
                if user_ratings[j] != 0:  # 使用用户评分过的物品进行预测
                    scores[i] += sim_matrix[i,j] * user_ratings[j]

    # 获取评分最高的N个物品索引
    recommended_items = np.argsort(scores)[::-1][:n_recommendations]
    return recommended_items, scores[recommended_items]

# 为用户0生成推荐
user_id = 0
recommended_items, scores = recommend(user_id, ratings, sim_matrix)

print(f"\n为用户{user_id}推荐的物品:")
for item, score in zip(recommended_items, scores):
    print(f"物品{item}, 预测评分: {score:.2f}")
