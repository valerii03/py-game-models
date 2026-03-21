import json
from db.models import Player, Race, Skill, Guild

def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        # --- РАСА ---
        race_data = player_data.get("race")
        race_obj = None
        if race_data:
            race_obj, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                defaults={"description": race_data.get("description")}
            )

            # --- НАВИЧКИ ---
            for skill_data in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data.get("name"),
                    defaults={"bonus": skill_data.get("bonus"), "race": race_obj}
                )

        # --- ГІЛЬДІЯ ---
        guild_data = player_data.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        # --- ГРАВЕЦЬ ---
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race_obj,
                "guild": guild_obj
            }
        )
