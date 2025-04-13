        if not os.path.isfile(f"cache/cropped{videoid}.png"):
            im = Image.open(f"cache/chop{videoid}.png").convert("RGBA")
            add_corners(im)
            im.save(f"cache/cropped{videoid}.png")

        crop_img = Image.open(f"cache/cropped{videoid}.png")
        logo = crop_img.convert("RGBA")
        logo.thumbnail((570, 570), Image.LANCZOS)
        width = int((1100 - 10) / 20)
        background = Image.open(f"cache/temp{videoid}.png")
        background.paste(logo, (width + 2, 30), mask=logo)
        background.paste(x, (1012, 440), mask=x)
        background.paste(image3, (0, 0), mask=image3)

        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("AnonX/assets/font2.ttf", 45)
        ImageFont.truetype("AnonX/assets/font2.ttf", 70)
        arial = ImageFont.truetype("AnonX/assets/font2.ttf", 65)
        ImageFont.truetype("AnonX/assets/font.ttf", 30)
        para = textwrap.wrap(title, width=26)

        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        file = f"cache/que{videoid}_{user_id}.png"
        background.save(f"cache/que{videoid}_{user_id}.png")
        return f"cache/que{videoid}_{user_id}.png"
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
