import os
import json
from PIL import Image, ImageDraw, ImageFont


def get_reward_icon_image(reward_icons, code, size) -> Image:
    if code not in reward_icons:
        file_path = "icons\\icon_reward_%s.png" % code
        im = Image.open(file_path).convert('RGBA')  # type: Image
        im = im.resize((size, size), Image.ANTIALIAS)
        reward_icons[code] = im
    return reward_icons[code]


def icon_text(reward_icons, value, icon_code, icon_size):
    percent = int(round(value * 100))
    text = "%+d" % (percent - 100)
    icon = get_reward_icon_image(reward_icons, icon_code, icon_size)
    return icon, text


def draw(background, x, y, width, height, icon, text, font):
    canvas = Image.new('RGBA', background.size, (255, 255, 255, 0))
    canvas_draw = ImageDraw.Draw(canvas, 'RGBA')
    canvas_draw.rectangle([(x, y), (x + width, y + height)], (0, 0, 0, 145))

    tx = x + icon.width - 1

    # shadow
    shadow_color = 'black'

    # thick
    # canvas_draw.text((tx - 1, y - 1), text, font=font, fill=shadow_color)
    # canvas_draw.text((tx + 1, y - 1), text, font=font, fill=shadow_color)
    # canvas_draw.text((tx - 1, y + 1), text, font=font, fill=shadow_color)
    # canvas_draw.text((tx + 1, y + 1), text, font=font, fill=shadow_color)

    # thin
    canvas_draw.text((tx - 1, y), text, font=font, fill=shadow_color)
    canvas_draw.text((tx + 1, y), text, font=font, fill=shadow_color)
    canvas_draw.text((tx, y + 1), text, font=font, fill=shadow_color)
    canvas_draw.text((tx, y + 1), text, font=font, fill=shadow_color)

    canvas_draw.text((tx, y), text, (255, 255, 255, 255), font)

    result = Image.alpha_composite(background, canvas)
    result.paste(icon, (x, y), icon)

    return result


def next_step(x, y, width, height, max_height):
    y += height
    if y >= max_height:
        y = 0
        x += width
    return x, y


def main():
    font = ImageFont.truetype("fonts\\default.ttf", 10, encoding="unic")
    reward_icons = {}

    with open('db\\data.json') as f:
        data = json.load(f)

    os.makedirs("out\\gui\\camouflages", exist_ok=True)
    os.makedirs("out\\gui\\permoflages", exist_ok=True)

    camouflages = os.listdir('res\\gui\\camouflages')
    permoflages = os.listdir('res\\gui\\permoflages')

    for unit in data:
        source_image = ''
        target_image = ''
        if unit['typeinfo']['type'] == 'Exterior' and unit['typeinfo']['species'] == 'Camouflage':
            camo_name = "%s.png" % unit['name'].lower()
            for filename in camouflages:
                if camo_name == filename.lower():
                    source_image = "res\\gui\\camouflages\\%s" % filename
                    target_image = "out\\gui\\camouflages\\%s.png" % unit['name']
                    break
        elif unit['typeinfo']['type'] == 'Exterior' and unit['typeinfo']['species'] == 'Permoflage':
            camo_name = "%s.png" % unit['name'].lower()
            for filename in permoflages:
                if camo_name == filename.lower():
                    source_image = "res\\gui\\permoflages\\%s" % filename
                    target_image = "out\\gui\\permoflages\\%s.png" % unit['name']
                    break

        if source_image and os.path.isfile(source_image):
            print(source_image)
            y = 0
            step = 14
            y_max = step * 3
            x = 0
            width = 37
            background = Image.open(source_image).convert('RGBA')
            if 'expFactor' in unit['modifiers'] and unit['modifiers']['expFactor'] != 1.0:
                icon, text = icon_text(reward_icons, unit['modifiers']['expFactor'], 'expCoeff', step)
                background = draw(background, x, y, width, step, icon, text, font)
                (x, y) = next_step(x, y, width, step, y_max)
            if 'freeExpFactor' in unit['modifiers'] and unit['modifiers']['freeExpFactor'] != 1.0:
                icon, text = icon_text(reward_icons, unit['modifiers']['freeExpFactor'], 'freexpCoeff', step)
                background = draw(background, x, y, width, step, icon, text, font)
                (x, y) = next_step(x, y, width, step, y_max)
            if 'crewExpFactor' in unit['modifiers'] and unit['modifiers']['crewExpFactor'] != 1.0:
                icon, text = icon_text(reward_icons, unit['modifiers']['crewExpFactor'], 'crewPointsCoeff', step)
                background = draw(background, x, y, width, step, icon, text, font)
                (x, y) = next_step(x, y, width, step, y_max)
            if 'creditsFactor' in unit['modifiers'] and unit['modifiers']['creditsFactor'] != 1.0:
                icon, text = icon_text(reward_icons, unit['modifiers']['creditsFactor'], 'creditsCoeff', step)
                background = draw(background, x, y, width, step, icon, text, font)
                (x, y) = next_step(x, y, width, step, y_max)
            if 'afterBattleRepair' in unit['modifiers'] and unit['modifiers']['afterBattleRepair'] != 1.0:
                icon, text = icon_text(reward_icons, unit['modifiers']['afterBattleRepair'], 'repairCoeff', step)
                background = draw(background, x, y, width, step, icon, text, font)
                (x, y) = next_step(x, y, width, step, y_max)

            if y > 0 or x > 0:
                if os.path.exists(target_image):
                    os.unlink(target_image)
                background.save(target_image, "PNG")


main()
