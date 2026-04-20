import os
import glob

def migrate():
    os.makedirs(".trae/rules", exist_ok=True)
    skills_dir = "skills"
    
    if not os.path.exists(skills_dir):
        print("未找到 skills 目录")
        return

    skill_files = glob.glob(os.path.join(skills_dir, "*", "SKILL.md"))
    
    for skill_file in skill_files:
        skill_name = os.path.basename(os.path.dirname(skill_file))
        target_file = f".trae/rules/{skill_name}.md"
        
        with open(skill_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"已迁移: {skill_name} -> {target_file}")
        
    print("✅ 完整工作流已打包到 .trae/rules/ 目录中。")

    # 附加：生成 Monolith 单文件版本
    monolith_file = "superpowers-monolith.md"
    with open(monolith_file, "w", encoding="utf-8") as f_out:
        f_out.write("# Superpowers 完整工作流系统\n\n")
        f_out.write("这是一套强制执行的多Agent工作流。你必须按照以下定义的技能和步骤进行软件开发。\n\n")
        for skill_file in skill_files:
            skill_name = os.path.basename(os.path.dirname(skill_file))
            f_out.write(f"\n## Skill: {skill_name}\n")
            with open(skill_file, "r", encoding="utf-8") as f_in:
                f_out.write(f_in.read())
            f_out.write("\n---\n")
    print(f"✅ 单文件全量版本已生成: {monolith_file} (可用于全局AI规则粘贴)")

if __name__ == "__main__":
    migrate()
