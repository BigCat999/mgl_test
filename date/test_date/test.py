
import yaml

with open('test_agent_audit_page.yml', 'r', encoding='gbk', errors='ignore') as f:
    data = yaml.load(f.read(), Loader=yaml.SafeLoader)

print(data)