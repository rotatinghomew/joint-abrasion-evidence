# 多地耐磨比对资料交换

`data/` 收录供演练使用的合成记录，不含真实企业或人员资料。资料使用 UTF-8 逗号分隔，首行为字段名，带逗号的单值用双引号括起。日期采用 ISO 表示，空字段表示来源未填或不适用，不代表数值零。`sources.json` 记录各表列名、身份键和可直接核对的引用。

## 业务资料

- `comparisons.csv`：各站报告的差值及标准误，正为耐磨改善，所有结果均为报告内所列终点的评分单位。lower/upper 是适用频段边界，端点包含。
- `provenance.csv`：已知重合上下界为共享试片数量；证据家族身份另外由 family 指示。相同 pair 的最新 disclosed 行替代旧声明。
- `substitution.csv`：采购范围用试验条件和频段描述，min_gain 是相对 REF 的最低差值，sources 是必须能区分的独立供货证据份数。
- `orders.csv`：需保留的订单约定。锁定时点为空表示还可更改拟选供应。
- `guarantees.csv`：替代承诺绑定一个或多个采购询证。direct_only=1 时不能用间接共同参照；excluded 可为临时禁用的试片家族。

标准误按各站报告口径给出，并非重合样本的逐件资料。未披露的重合关系不是 0；是否有独立来源只在有明确互不重合依据的范围承诺。不同端点的分值不可相加。采购同一有效范围内最低支持份数按不同供应规格及其对应用于判定的证据计。

## 本地核对

需要 Python 3.11。分析环境可使用 `python3 -m pip install -r requirements.txt` 安装锁定的数值依赖。

从仓库根目录执行 `python3 check_sources.py`，返回各表行数；其他同格式资料可用 `python3 check_sources.py 路径` 检查。脚本只读资料并报告结构或引用错误，不给出业务结论。执行 `python3 -m unittest discover -s tests -v` 检查资料约定及拒绝重复身份的行为。
