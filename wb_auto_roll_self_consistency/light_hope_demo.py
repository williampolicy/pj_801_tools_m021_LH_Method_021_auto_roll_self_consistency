#!/usr/bin/env python3
"""
LIGHT HOPE 网站自动修正系统 - 极简Demo版
不需要API密钥，使用模拟数据先跑通流程
"""

import os
import json
import time
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
import hashlib

# ==================== 配置 ====================
BASE_DIR = Path(__file__).parent
WEBSITE_DIR = BASE_DIR / "website_demo"
SESSIONS_DIR = BASE_DIR / "sessions"
BACKUPS_DIR = BASE_DIR / "backups"

# ==================== 初始化 ====================
def init_project():
    """初始化项目结构"""
    # 创建必要目录
    for dir_path in [WEBSITE_DIR, SESSIONS_DIR, BACKUPS_DIR]:
        dir_path.mkdir(exist_ok=True)
    
    # 创建Demo网站文件
    if not (WEBSITE_DIR / "index.html").exists():
        print("📦 创建Demo网站...")
        
        # index.html
        (WEBSITE_DIR / "index.html").write_text("""<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Welcome to Demo Site</h1>
        <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>
    <main>
        <section id="home">
            <h2>Home Section</h2>
            <p>This is a demo website for LIGHT HOPE auto-editing system.</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2025 Demo Site</p>
    </footer>
</body>
</html>""")
        
        # style.css
        (WEBSITE_DIR / "style.css").write_text("""body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

header {
    background: #333;
    color: #fff;
    padding: 1rem;
}

nav a {
    color: #fff;
    text-decoration: none;
    margin: 0 15px;
}

main {
    padding: 20px;
}

footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px;
    position: fixed;
    bottom: 0;
    width: 100%;
}""")
        
        # app.js
        (WEBSITE_DIR / "app.js").write_text("""// Demo JavaScript
console.log('Demo website loaded');

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM ready');
});""")
    
    # 初始化Git仓库
    if not (WEBSITE_DIR / ".git").exists():
        print("🔧 初始化Git仓库...")
        os.chdir(WEBSITE_DIR)
        subprocess.run(["git", "init"], capture_output=True)
        subprocess.run(["git", "add", "."], capture_output=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], capture_output=True)
        os.chdir(BASE_DIR)
        print("✅ Git仓库初始化完成")

# ==================== 模拟AI引擎 ====================
class MockAIEngine:
    """模拟AI引擎，用于Demo演示"""
    
    def __init__(self):
        self.round_counter = 0
    
    def generate_patch(self, goal, context, round_num):
        """生成模拟的修改补丁"""
        self.round_counter = round_num
        
        # 根据轮次生成不同的模拟补丁
        patches = {
            1: self._patch_add_comment(),
            2: self._patch_improve_style(),
            3: self._patch_add_feature(),
            4: self._patch_optimize(),
            5: self._patch_final_touch()
        }
        
        return patches.get(round_num, self._patch_empty())
    
    def _patch_add_comment(self):
        """第1轮：添加注释"""
        return """diff --git a/index.html b/index.html
index 1234567..abcdefg 100644
--- a/index.html
+++ b/index.html
@@ -1,4 +1,5 @@
 <!DOCTYPE html>
+<!-- Auto-improved by LIGHT HOPE Round 1 -->
 <html lang="zh">
 <head>
     <meta charset="UTF-8">"""
    
    def _patch_improve_style(self):
        """第2轮：改进样式"""
        return """diff --git a/style.css b/style.css
index 1234567..abcdefg 100644
--- a/style.css
+++ b/style.css
@@ -1,6 +1,7 @@
 body {
     font-family: Arial, sans-serif;
     margin: 0;
     padding: 0;
     line-height: 1.6;
+    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
 }"""
    
    def _patch_add_feature(self):
        """第3轮：添加功能"""
        return """diff --git a/app.js b/app.js
index 1234567..abcdefg 100644
--- a/app.js
+++ b/app.js
@@ -3,4 +3,9 @@ console.log('Demo website loaded');
 
 document.addEventListener('DOMContentLoaded', function() {
     console.log('DOM ready');
+    
+    // Add smooth scrolling
+    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
+        anchor.addEventListener('click', smoothScroll);
+    });
 });"""
    
    def _patch_optimize(self):
        """第4轮：优化代码"""
        return """diff --git a/index.html b/index.html
index 1234567..abcdefg 100644
--- a/index.html
+++ b/index.html
@@ -4,6 +4,7 @@
 <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <meta name="description" content="Demo website for LIGHT HOPE system">
     <title>Demo Website</title>"""
    
    def _patch_final_touch(self):
        """第5轮：最终优化"""
        return """diff --git a/style.css b/style.css
index 1234567..abcdefg 100644
--- a/style.css
+++ b/style.css
@@ -10,6 +10,7 @@ header {
     background: #333;
     color: #fff;
     padding: 1rem;
+    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
 }"""
    
    def _patch_empty(self):
        """空补丁"""
        return ""
    
    def critique(self, patch, round_num):
        """生成批评建议"""
        critiques = {
            1: "添加了注释，但可以进一步改进样式",
            2: "样式有改进，建议添加更多交互功能",
            3: "功能增强了，需要优化性能",
            4: "性能优化完成，再做最后的美化",
            5: "LGTM - 所有改进已完成"
        }
        return critiques.get(round_num, "继续改进")

# ==================== 核心引擎 ====================
class LightHopeEngine:
    """LIGHT HOPE 核心引擎"""
    
    def __init__(self):
        self.ai_engine = MockAIEngine()
        init_project()
    
    def create_session(self, goal):
        """创建新会话"""
        session_id = hashlib.md5(f"{goal}{time.time()}".encode()).hexdigest()[:8]
        session_data = {
            "id": session_id,
            "goal": goal,
            "created": datetime.now().isoformat(),
            "rounds": [],
            "status": "active"
        }
        
        session_file = SESSIONS_DIR / f"{session_id}.json"
        session_file.write_text(json.dumps(session_data, indent=2, ensure_ascii=False))
        
        print(f"✅ 会话创建成功: {session_id}")
        return session_id
    
    def execute_round(self, session_id, dry_run=True):
        """执行一轮修正"""
        # 加载会话
        session_file = SESSIONS_DIR / f"{session_id}.json"
        if not session_file.exists():
            print(f"❌ 会话不存在: {session_id}")
            return None
        
        session = json.loads(session_file.read_text())
        round_num = len(session["rounds"]) + 1
        
        print(f"\n🔄 执行第 {round_num} 轮修正...")
        
        # 收集上下文
        context = self._collect_context()
        
        # 生成补丁
        patch = self.ai_engine.generate_patch(session["goal"], context, round_num)
        
        # 验证补丁
        is_valid = self._validate_patch(patch)
        
        # 生成批评
        critique = self.ai_engine.critique(patch, round_num)
        
        # 应用补丁（如果有效且非dry-run）
        applied = False
        if patch and is_valid and not dry_run:
            applied = self._apply_patch(patch, session_id, round_num)
        
        # 记录轮次
        round_data = {
            "number": round_num,
            "timestamp": datetime.now().isoformat(),
            "patch_size": len(patch),
            "valid": is_valid,
            "applied": applied,
            "critique": critique,
            "dry_run": dry_run
        }
        
        session["rounds"].append(round_data)
        session_file.write_text(json.dumps(session, indent=2, ensure_ascii=False))
        
        # 输出结果
        print(f"  📝 补丁大小: {len(patch)} 字符")
        print(f"  ✓ 验证结果: {'通过' if is_valid else '失败'}")
        print(f"  💭 批评建议: {critique}")
        print(f"  🚀 应用状态: {'已应用' if applied else 'Dry-run模式' if dry_run else '未应用'}")
        
        return round_data
    
    def _collect_context(self):
        """收集文件上下文"""
        context = []
        for file_path in WEBSITE_DIR.glob("*"):
            if file_path.is_file() and file_path.suffix in [".html", ".css", ".js"]:
                content = file_path.read_text()[:500]  # 前500字符
                context.append(f"File: {file_path.name}\n{content}\n")
        return "\n".join(context)
    
    def _validate_patch(self, patch):
        """验证补丁（简化版）"""
        if not patch:
            return False
        # 简单检查是否包含diff格式
        return "diff --git" in patch
    
    def _apply_patch(self, patch, session_id, round_num):
        """应用补丁（模拟）"""
        try:
            # 备份
            backup_dir = BACKUPS_DIR / f"{session_id}_round{round_num}"
            shutil.copytree(WEBSITE_DIR, backup_dir)
            
            # 这里实际应该用 git apply
            # 为了Demo简化，只记录应用状态
            
            # Git提交
            os.chdir(WEBSITE_DIR)
            subprocess.run(["git", "add", "-A"], capture_output=True)
            subprocess.run(["git", "commit", "-m", f"Round {round_num} changes"], capture_output=True)
            os.chdir(BASE_DIR)
            
            return True
        except Exception as e:
            print(f"  ⚠️ 应用失败: {e}")
            return False
    
    def show_status(self, session_id):
        """显示会话状态"""
        session_file = SESSIONS_DIR / f"{session_id}.json"
        if not session_file.exists():
            print(f"❌ 会话不存在: {session_id}")
            return
        
        session = json.loads(session_file.read_text())
        
        print(f"\n📊 会话状态: {session_id}")
        print(f"  目标: {session['goal']}")
        print(f"  创建时间: {session['created']}")
        print(f"  执行轮次: {len(session['rounds'])}")
        
        if session['rounds']:
            print("\n  历史记录:")
            for r in session['rounds']:
                status = "✅" if r['applied'] else "⏸️"
                print(f"    {status} 第{r['number']}轮 - {r['critique']}")

# ==================== 简单Web界面 ====================
def create_simple_html():
    """创建简单的HTML控制界面"""
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>LIGHT HOPE Control Panel</title>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            background: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        h1 {
            color: #667eea;
            text-align: center;
        }
        .status {
            background: #f0f0f0;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            font-family: monospace;
        }
        .btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            margin: 5px;
        }
        .btn:hover {
            background: #764ba2;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌟 LIGHT HOPE Auto Editor</h1>
        <p>极简的网站自动修正系统</p>
        
        <div class="status">
            <h3>当前状态</h3>
            <p>系统已启动，请使用命令行工具执行操作</p>
        </div>
        
        <h3>使用说明</h3>
        <ol>
            <li>创建会话: <code>python light_hope_demo.py create "改进目标"</code></li>
            <li>执行修正: <code>python light_hope_demo.py run SESSION_ID</code></li>
            <li>查看状态: <code>python light_hope_demo.py status SESSION_ID</code></li>
        </ol>
        
        <h3>Demo网站预览</h3>
        <iframe src="website_demo/index.html" style="width:100%;height:400px;border:1px solid #ddd;"></iframe>
    </div>
</body>
</html>"""
    
    (BASE_DIR / "control_panel.html").write_text(html_content)
    print(f"✨ 控制面板已创建: {BASE_DIR / 'control_panel.html'}")

# ==================== 命令行接口 ====================
def main():
    import sys
    
    print("""
╔══════════════════════════════════════╗
║     🌟 LIGHT HOPE Auto Editor 🌟     ║
║         极简网站自动修正系统          ║
╚══════════════════════════════════════╝
    """)
    
    engine = LightHopeEngine()
    
    if len(sys.argv) < 2:
        print("使用方法:")
        print("  创建会话: python light_hope_demo.py create \"你的改进目标\"")
        print("  执行修正: python light_hope_demo.py run SESSION_ID [--apply]")
        print("  查看状态: python light_hope_demo.py status SESSION_ID")
        print("  运行Demo: python light_hope_demo.py demo")
        print("  打开面板: python light_hope_demo.py panel")
        return
    
    command = sys.argv[1]
    
    if command == "create":
        if len(sys.argv) < 3:
            print("❌ 请提供改进目标")
            return
        goal = sys.argv[2]
        session_id = engine.create_session(goal)
        print(f"\n下一步: python light_hope_demo.py run {session_id}")
    
    elif command == "run":
        if len(sys.argv) < 3:
            print("❌ 请提供会话ID")
            return
        session_id = sys.argv[2]
        dry_run = "--apply" not in sys.argv
        
        # 执行5轮
        for i in range(5):
            print(f"\n--- 第 {i+1}/5 轮 ---")
            result = engine.execute_round(session_id, dry_run)
            if not result:
                break
            time.sleep(1)  # 模拟处理时间
        
        print(f"\n✅ 完成所有轮次")
        engine.show_status(session_id)
    
    elif command == "status":
        if len(sys.argv) < 3:
            print("❌ 请提供会话ID")
            return
        session_id = sys.argv[2]
        engine.show_status(session_id)
    
    elif command == "demo":
        print("🚀 运行完整Demo流程...")
        
        # 创建会话
        session_id = engine.create_session("改进网站的视觉设计和用户体验")
        
        # 执行5轮（dry-run）
        for i in range(5):
            print(f"\n--- Demo 第 {i+1}/5 轮 ---")
            engine.execute_round(session_id, dry_run=True)
            time.sleep(1)
        
        # 显示最终状态
        engine.show_status(session_id)
        
        print("\n✨ Demo完成！")
        print(f"  查看结果: {SESSIONS_DIR}/{session_id}.json")
        print(f"  网站文件: {WEBSITE_DIR}/")
    
    elif command == "panel":
        create_simple_html()
        import webbrowser
        webbrowser.open(f"file://{BASE_DIR}/control_panel.html")
    
    else:
        print(f"❌ 未知命令: {command}")

if __name__ == "__main__":
    main()
