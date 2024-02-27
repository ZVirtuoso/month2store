from skill_system.skill_deployer import SkillDeployer
class SkillManager:
    def __init__(self):
        self.skill_deployer = SkillDeployer()

    def use_skill(self):
        print("使用技能")
        self.skill_deployer.skill_deployer()