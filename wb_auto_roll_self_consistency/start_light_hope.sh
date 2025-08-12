#!/bin/bash
# LIGHT HOPE 快速启动脚本
# 保存为 start_light_hope.sh

echo "🌟 LIGHT HOPE 快速部署脚本"
echo "=========================="

# 设置基础路径
BASE_DIR="/home/kangxiaowen/code_lh_server/code_lh_pj_ai/pj_801_tools_m021_LH_Method_021_auto_roll_self_consistency/wb_auto_roll_self_consistency"
cd $BASE_DIR

# 1. 下载Demo文件
echo "📥 下载Demo文件..."
cat > light_hope_demo.py << 'DEMO_EOF'
# [这里插入完整的light_hope_demo.py代码]
DEMO_EOF

# 2. 安装依赖（如果需要）
echo "📦 检查依赖..."
python3 -c "import json, pathlib, shutil, subprocess" 2>/dev/null || {
    echo "❌ 缺少Python标准库"
    exit 1
}

# 3. 初始化Git（如果需要）
if ! command -v git &> /dev/null; then
    echo "⚠️ Git未安装，部分功能将受限"
else
    echo "✅ Git已就绪"
fi

# 4. 运行Demo
echo ""
echo "🚀 启动Demo..."
python3 light_hope_demo.py demo

# 5. 生成快捷命令
cat > lh << 'EOF'
#!/bin/bash
# LIGHT HOPE 快捷命令
python3 light_hope_demo.py "$@"
EOF
chmod +x lh

echo ""
echo "✨ 安装完成！"
echo ""
echo "使用方法："
echo "  ./lh create \"改进目标\"  # 创建新会话"
echo "  ./lh run SESSION_ID      # 执行修正"
echo "  ./lh status SESSION_ID   # 查看状态"
echo "  ./lh demo               # 运行完整演示"
echo "  ./lh panel              # 打开控制面板"
echo ""
echo "示例："
echo "  ./lh create \"优化网站的移动端体验\""
echo ""
