# pytest-api-demo

基于 `pytest + requests` 的接口自动化练习项目：分层封装、数据驱动、契约校验、CI 一键运行。

## 结构

```
pytest-api-demo/
├─ conftest.py              # 公共 fixture：会话级 HTTP 客户端
├─ pytest.ini               # 标记与默认参数
├─ utils/api_client.py      # requests.Session 封装 + 耗时日志
├─ tests/
│  ├─ test_posts_crud.py    # 增删改查 + 参数化
│  ├─ test_httpbin_echo.py  # 状态码矩阵 / 参数回显 / JSON 回显
│  └─ test_contract.py      # 返回体字段契约（类型级断言）
└─ .github/workflows/tests.yml
```

## 运行

```bash
python -m venv .venv
.venv\Scripts\activate        # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest
```

只跑某个模块：`pytest tests/test_posts_crud.py -v`

## 设计要点

1. **分层**：用例只关心"发什么、断言什么"，URL 拼接、超时、日志统一收在 `ApiClient`。
2. **数据驱动**：`@pytest.mark.parametrize` 覆盖多个 post_id 与状态码矩阵，避免复制粘贴。
3. **契约校验**：不只看 `status_code`，还断言返回体字段存在且类型正确——接口字段悄悄改名/变类型时能立刻失败。
4. **失败可诊断**：每个请求记录方法、URL、状态码、耗时；失败时日志即现场。

## 数据源

- `jsonplaceholder.typicode.com`：只读 Fake API，写操作返回回声（POST 不真正落库）。
- `httpbin.org`：请求回显，用于校验参数、Header、JSON body 的传递。

## 已知限制

- 依赖公网，离线环境会失败，可加 `-m "not network"` 跳过。
- jsonplaceholder 是垫片服务，写接口不做真正的数据一致性校验，因此本仓库不覆盖"写后读"场景。
